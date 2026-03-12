module.exports = {
  apps: [{
    name: 'vibers-invite-checker',
    script: '/root/vibers.onout.org/scripts/check-invites.py',
    interpreter: 'python3',
    cron_restart: '*/1 * * * *',  // every minute
    autorestart: false,
    env: {
      TELEGRAM_SESSION_STRING: process.env.TELEGRAM_SESSION_STRING || '',
      TELEGRAM_CHAT_ID: '-5058393445',
    }
  }]
};
