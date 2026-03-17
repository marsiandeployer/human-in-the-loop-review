# Vibers Review Runbook

How to do a code review after receiving a Telegram notification.

## 1. New Invite Notification

You get: "Vibers: New repo invitation!" in Telegram.

Action:
1. Open repo link from the message
2. Check if repo has `.github/workflows/vibers.yml` — if not, the client only added collaborator but didn't set up the Action. Nothing to do until they push.
3. Check if repo has a spec (look for links in README, CLAUDE.md, or vibers.yml `spec_url`)
4. Note the repo for when commits start coming

## 2. Review Request Notification

You get: "Vibers: Review Request" in Telegram with commit details.

Action:
1. Read the commit message — especially "How to test" section
2. Clone/pull the repo:
   ```bash
   cd /root/reviews
   gh repo clone <owner/repo> || (cd <repo> && git pull)
   ```
3. Read the spec (if spec_url provided)
4. Review changed files from the notification

## 3. What to Check

Priority order:
1. **Spec compliance** — does the code do what the spec says?
2. **Security** — hardcoded secrets, SQL injection, XSS, missing auth
3. **AI hallucinations** — non-existent APIs, deprecated methods, fake imports
4. **Logic bugs** — edge cases, off-by-one, null handling, race conditions
5. **UI issues** — if deploy URL provided, open and check visually

## 4. Submit the Review

1. Fork the repo (if not already forked)
2. Create a branch: `vibers/review-<date>`
3. Make fixes directly in code
4. Push and create PR:
   ```bash
   gh pr create --title "Vibers: code review fixes" --body "..."
   ```
5. Message the client on Telegram (if contact provided)

## 5. Monitoring

- Check Telegram chat periodically for missed notifications
- Health check: `curl https://vibers.onout.org/health` should return `{"status": "ok"}`
- PM2 status: `pm2 show vibers-feedback` and `pm2 show vibers-invite-checker`
- If no heartbeat in Telegram for >2 hours, SSH to server and check `pm2 logs`

## 6. Common Issues

| Problem | Fix |
|---------|-----|
| No notifications coming | Check `pm2 status vibers-feedback` — should be online |
| Telegram "send failed" | Pyrogram session may have expired. Regenerate session string |
| invite-checker errored | Normal — it's a PM2 cron, exits after each run. Check error logs if `pm2 logs vibers-invite-checker --err` shows real errors |
| Client spec is private | Message client on Telegram to make spec publicly accessible |
