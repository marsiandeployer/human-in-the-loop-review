#!/usr/bin/env python3
"""
Smoke-tests for feedback-server.py endpoints.

Run:
    python3 tests/test_server.py

Requirements: server running on localhost:3847
"""

import hashlib
import hmac
import json
import sys
import time
import urllib.request
import urllib.error

BASE = "http://localhost:3847"


def _post(path, body, headers=None):
    data = json.dumps(body).encode()
    h = {"Content-Type": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(BASE + path, data=data, headers=h, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())


def _get(path):
    req = urllib.request.Request(BASE + path)
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def _make_sig(secret: str, body: bytes) -> str:
    return "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


WEBHOOK_SECRET = None  # loaded from .env below

def _load_secret():
    global WEBHOOK_SECRET
    # Try both relative (run from repo root) and absolute path
    _candidates = [
        "scripts/.env",
        "/root/vibers.onout.org/scripts/.env",
    ]
    for path in _candidates:
        try:
            with open(path) as f:
                for line in f:
                    if line.startswith("GH_WEBHOOK_SECRET="):
                        WEBHOOK_SECRET = line.split("=", 1)[1].strip()
            if WEBHOOK_SECRET:
                return
        except Exception:
            pass


# ─── Tests ──────────────────────────────────────────────────────────────────

PASS = 0
FAIL = 0


def ok(name):
    global PASS
    PASS += 1
    print(f"  ✓  {name}")


def fail(name, reason):
    global FAIL
    FAIL += 1
    print(f"  ✗  {name}: {reason}")


def check(name, condition, reason=""):
    if condition:
        ok(name)
    else:
        fail(name, reason or "assertion failed")


# --- /health ---

def test_health():
    code, body = _get("/health")
    check("/health returns 200", code == 200, f"got {code}")
    try:
        data = json.loads(body)
        check("/health has status field", "status" in data, str(data))
    except Exception:
        pass  # already checked above


# --- /feedback ---

def test_feedback_missing_how_to_test():
    code, body = _post("/feedback", {"message": "just a message", "repo": "owner/repo"})
    check("/feedback rejects without how-to-test", code == 400, f"got {code}: {body}")


def test_feedback_missing_repo():
    code, body = _post("/feedback", {"message": "How to test: open /", "repo": ""})
    check("/feedback rejects empty repo", code == 400, f"got {code}: {body}")


def test_feedback_missing_message():
    code, body = _post("/feedback", {"message": "", "repo": "owner/repo"})
    check("/feedback rejects empty message", code == 400, f"got {code}: {body}")


def test_feedback_rate_limit():
    # Hit /feedback 6 times quickly — 6th should 429
    for i in range(5):
        _post("/feedback", {"message": "How to test: x", "repo": "o/r"})
    code, body = _post("/feedback", {"message": "How to test: x", "repo": "o/r"})
    # Rate limit is 5/min, so after 5 hits the 6th should be 429
    check("/feedback rate limit triggers at 6th request", code == 429, f"got {code}: {body}")


# --- /github/webhook ---

def test_webhook_invalid_sig():
    body = json.dumps({"action": "ping"}).encode()
    code, resp = _post("/github/webhook", {}, headers={"X-Hub-Signature-256": "sha256=invalid", "X-GitHub-Event": "ping"})
    check("/github/webhook rejects invalid sig", code == 401, f"got {code}: {resp}")


def test_webhook_missing_sig():
    code, resp = _post("/github/webhook", {})
    check("/github/webhook rejects missing sig", code == 401, f"got {code}: {resp}")


def test_webhook_ping_with_valid_sig():
    if not WEBHOOK_SECRET:
        print("  -  /github/webhook ping (skip — no secret)")
        return
    payload = json.dumps({"zen": "ok"}).encode()
    sig = _make_sig(WEBHOOK_SECRET, payload)
    req = urllib.request.Request(
        BASE + "/github/webhook",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Hub-Signature-256": sig,
            "X-GitHub-Event": "ping",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    check("/github/webhook accepts valid sig ping", code == 200, f"got {code}")


def test_webhook_push_without_how_to_test():
    """Push without 'how to test' should be silently accepted (200) but not send to Telegram."""
    if not WEBHOOK_SECRET:
        print("  -  /github/webhook push gate (skip — no secret)")
        return
    payload = json.dumps({
        "ref": "refs/heads/main",
        "repository": {"full_name": "owner/repo"},
        "pusher": {"name": "testuser"},
        "head_commit": {"id": "abc1234", "message": "just a commit", "url": ""},
        "commits": [],
    }).encode()
    sig = _make_sig(WEBHOOK_SECRET, payload)
    req = urllib.request.Request(
        BASE + "/github/webhook",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Hub-Signature-256": sig,
            "X-GitHub-Event": "push",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=5) as r:
        code = r.status
    check("/github/webhook push without how-to-test returns 200 (silently skipped)", code == 200, f"got {code}")


# --- /github/setup ---

def test_setup_unknown_installation():
    code, body = _post("/github/setup", {"installation_id": 99999999, "telegram": "@test"})
    check("/github/setup rejects unknown installation_id", code == 403, f"got {code}: {body}")


def test_setup_invalid_id():
    code, body = _post("/github/setup", {"installation_id": "not-a-number"})
    check("/github/setup rejects non-numeric installation_id", code == 403, f"got {code}: {body}")


# --- 404 ---

def test_404():
    code, _ = _get("/nonexistent-path")
    check("unknown path returns 404", code == 404, f"got {code}")


# ─── Run all ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    _load_secret()
    print(f"Testing {BASE}\n")

    test_health()
    test_feedback_missing_how_to_test()
    test_feedback_missing_repo()
    test_feedback_missing_message()
    # Note: rate limit test consumes quota — run last in feedback group
    # test_feedback_rate_limit()  # skip by default (affects other tests)
    test_webhook_invalid_sig()
    test_webhook_missing_sig()
    test_webhook_ping_with_valid_sig()
    test_webhook_push_without_how_to_test()
    test_setup_unknown_installation()
    test_setup_invalid_id()
    test_404()

    print(f"\n{PASS + FAIL} tests: {PASS} passed, {FAIL} failed")
    sys.exit(0 if FAIL == 0 else 1)
