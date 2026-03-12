#!/usr/bin/env python3
"""
Vibers Feedback API — accepts user feedback and sends to Telegram.

POST /feedback
Body: {"message": "...", "repo": "https://github.com/user/repo"}

Run via PM2.
"""

import json
import os
import sys
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
# Single-threaded: pyrogram requires main thread event loop

TELEGRAM_API_ID = int(os.environ.get("TELEGRAM_API_ID", "20663119"))
TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH", "")
TELEGRAM_SESSION = os.environ.get("TELEGRAM_SESSION_STRING", "")
TELEGRAM_CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "-5058393445"))
PORT = int(os.environ.get("FEEDBACK_PORT", "3847"))

# Rate limiting: max 5 requests per minute per IP
RATE_LIMIT = {}
RATE_WINDOW = 60
RATE_MAX = 5


def send_telegram(text):
    if not TELEGRAM_SESSION:
        print(f"No TELEGRAM_SESSION_STRING, printing instead:\n{text}")
        return False
    if not TELEGRAM_API_HASH:
        print("No TELEGRAM_API_HASH set, skipping telegram", file=sys.stderr)
        return False

    try:
        from pyrogram import Client

        app = Client(
            "vibers_feedback",
            api_id=TELEGRAM_API_ID,
            api_hash=TELEGRAM_API_HASH,
            session_string=TELEGRAM_SESSION,
            in_memory=True
        )
        with app:
            for _ in app.get_dialogs():
                pass
            app.send_message(TELEGRAM_CHAT_ID, text)
        print(f"Telegram sent to {TELEGRAM_CHAT_ID}")
        return True
    except Exception as e:
        print(f"Telegram send failed: {e}", file=sys.stderr)
        return False


def check_rate_limit(ip):
    now = time.time()
    if ip in RATE_LIMIT:
        timestamps = [t for t in RATE_LIMIT[ip] if now - t < RATE_WINDOW]
        RATE_LIMIT[ip] = timestamps
        if len(timestamps) >= RATE_MAX:
            return False
    else:
        RATE_LIMIT[ip] = []
    RATE_LIMIT[ip].append(now)
    return True


class FeedbackHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self._cors_headers()
        self.end_headers()

    def _read_json_body(self, max_size=10000):
        """Read and parse JSON body. Returns (data, error_sent) tuple."""
        # Rate limiting
        client_ip = self.headers.get("X-Real-IP", self.client_address[0])
        if not check_rate_limit(client_ip):
            self.send_response(429)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "too many requests, try again later"}')
            return None, True

        try:
            content_length = int(self.headers.get("Content-Length", 0))
        except (ValueError, TypeError):
            self.send_response(400)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "invalid content-length"}')
            return None, True

        if content_length < 0 or content_length > max_size:
            self.send_response(413)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "invalid or too large body"}')
            return None, True

        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self.send_response(400)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "invalid json"}')
            return None, True

        if not isinstance(data, dict):
            self.send_response(400)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "expected json object"}')
            return None, True

        return data, False

    def _send_and_respond(self, tg_text):
        """Send to Telegram and write HTTP response."""
        sent = send_telegram(tg_text)
        if sent:
            self.send_response(200)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"status": "accepted"}')
        else:
            self.send_response(502)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "failed to deliver, contact @onoutnoxon on Telegram"}')

    def do_POST(self):
        if self.path == "/feedback":
            self._handle_feedback()
        elif self.path == "/review":
            self._handle_review()
        else:
            self.send_response(404)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "not found"}')

    def _handle_feedback(self):
        data, err = self._read_json_body()
        if err:
            return

        message = data.get("message") if isinstance(data.get("message"), str) else None
        repo = data.get("repo") if isinstance(data.get("repo"), str) else None

        if not message or not message.strip():
            self.send_response(400)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "message is required (string)"}')
            return

        if not repo or not repo.strip():
            self.send_response(400)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "repo is required (string)"}')
            return

        message = message.strip()[:2000]
        repo = repo.strip()[:500]

        tg_text = (
            f"**Vibers Feedback**\n\n"
            f"Repo: {repo}\n"
            f"Message: {message}"
        )
        self._send_and_respond(tg_text)

    def _str_field(self, data, key, max_len=500, default=""):
        """Extract string field from data safely."""
        val = data.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()[:max_len]
        return default

    def _handle_review(self):
        data, err = self._read_json_body(max_size=50000)
        if err:
            return

        repo = self._str_field(data, "repo")
        if not repo:
            self.send_response(400)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(b'{"error": "repo is required"}')
            return

        branch = self._str_field(data, "branch", 100, "unknown")
        sha = self._str_field(data, "sha", 40)
        author = self._str_field(data, "author", 100, "unknown")
        spec_url = self._str_field(data, "spec_url", 500)
        contact = self._str_field(data, "contact", 100)
        commit_msg = self._str_field(data, "commit_msg", 200)
        commit_body = self._str_field(data, "commit_body", 2000)
        diff_stat = self._str_field(data, "diff_stat", 200)
        deploy_url = self._str_field(data, "deploy_url", 500)
        stack = self._str_field(data, "stack", 200)
        creds = self._str_field(data, "creds", 1000)
        files = self._str_field(data, "changed_files", 3000)
        file_count = len([f for f in files.split("\n") if f.strip()]) if files else 0

        repo_url = f"https://github.com/{repo}" if "/" in repo and not repo.startswith("http") else repo
        commit_url = f"{repo_url}/commit/{sha}" if sha else ""

        # Build Telegram message — compact, useful
        tg_text = f"**Vibers: Review Request**\n\n"
        tg_text += f"[{repo}]({repo_url}) | [{sha[:8]}]({commit_url})\n"
        tg_text += f"Author: {author} | Branch: `{branch}`\n"

        if commit_msg:
            tg_text += f"\n**{commit_msg}**\n"

        if commit_body:
            tg_text += f"\n{commit_body}\n"

        if diff_stat:
            tg_text += f"\n`{diff_stat}`\n"

        if stack:
            tg_text += f"Stack: {stack}\n"

        if spec_url:
            tg_text += f"Spec: {spec_url}\n"
        if contact:
            tg_text += f"Contact: {contact}\n"
        if deploy_url:
            tg_text += f"Deploy: {deploy_url}\n"

        if creds:
            tg_text += f"\n**Credentials:**\n```\n{creds[:500]}\n```\n"

        if files:
            tg_text += f"\n**Files ({file_count}):**\n```\n{files[:800]}\n```"

        self._send_and_respond(tg_text)

    def _cors_headers(self):
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def log_message(self, format, *args):
        print(f"[feedback-server] {args[0]}")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), FeedbackHandler)
    print(f"Feedback server listening on 127.0.0.1:{PORT}")
    server.serve_forever()
