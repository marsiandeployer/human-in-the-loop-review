#!/usr/bin/env python3
"""
Check GitHub repository invitations for marsiandeployer.
Accept them and send Telegram notification.

Run via PM2 cron every 60 seconds.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# --- Config ---
STATE_FILE = Path(__file__).parent / ".invite-state.json"
TELEGRAM_API_ID = 20663119
TELEGRAM_API_HASH = "0735e154f4ee0ea6bcfe3d972de467b9"
TELEGRAM_SESSION = os.environ.get("TELEGRAM_SESSION_STRING", "")
TELEGRAM_CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "-5058393445"))


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"processed": []}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_invitations():
    """Get pending repo invitations via gh CLI."""
    result = subprocess.run(
        ["gh", "api", "/user/repository_invitations"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error fetching invitations: {result.stderr}", file=sys.stderr)
        return []
    return json.loads(result.stdout)


def accept_invitation(invite_id):
    """Accept a repository invitation."""
    result = subprocess.run(
        ["gh", "api", "-X", "PATCH", f"/user/repository_invitations/{invite_id}"],
        capture_output=True, text=True
    )
    return result.returncode == 0


def send_telegram(text):
    """Send message via Pyrogram (userbot session)."""
    if not TELEGRAM_SESSION:
        print(f"No TELEGRAM_SESSION_STRING, printing instead:\n{text}")
        return

    try:
        from pyrogram import Client

        app = Client(
            "vibers_notifier",
            api_id=TELEGRAM_API_ID,
            api_hash=TELEGRAM_API_HASH,
            session_string=TELEGRAM_SESSION,
            in_memory=True
        )
        with app:
            app.send_message(TELEGRAM_CHAT_ID, text)
        print(f"Telegram sent to {TELEGRAM_CHAT_ID}")
    except Exception as e:
        print(f"Telegram send failed: {e}", file=sys.stderr)


def main():
    invitations = get_invitations()
    if not invitations:
        return

    state = load_state()
    processed = set(state["processed"])

    for inv in invitations:
        inv_id = inv["id"]
        if inv_id in processed:
            continue

        repo = inv.get("repository", {})
        repo_name = repo.get("full_name", "unknown")
        repo_url = repo.get("html_url", "")
        inviter = inv.get("inviter", {}).get("login", "unknown")
        permissions = inv.get("permissions", "unknown")
        created = inv.get("created_at", "")

        # Accept the invitation
        accepted = accept_invitation(inv_id)
        status = "accepted" if accepted else "FAILED to accept"

        # Build message
        msg = (
            f"🔔 **Vibers: New repo invitation!**\n\n"
            f"📦 Repo: [{repo_name}]({repo_url})\n"
            f"👤 Invited by: @{inviter}\n"
            f"🔑 Permissions: {permissions}\n"
            f"📅 Date: {created}\n"
            f"✅ Status: {status}\n\n"
            f"Next: check repo for spec/docs and start review."
        )

        print(f"[{datetime.now().isoformat()}] Invitation from {inviter} for {repo_name} — {status}")
        send_telegram(msg)

        processed.add(inv_id)

    state["processed"] = list(processed)[-100:]  # keep last 100
    save_state(state)


if __name__ == "__main__":
    main()
