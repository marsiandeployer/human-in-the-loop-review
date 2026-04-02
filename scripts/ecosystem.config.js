const fs = require('fs');

// Load ~/.env if it exists (shared credentials across all projects)
function loadDotEnv(path) {
  try {
    const lines = fs.readFileSync(path, 'utf8').split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const eq = trimmed.indexOf('=');
      if (eq === -1) continue;
      const key = trimmed.slice(0, eq).trim();
      const val = trimmed.slice(eq + 1).trim();
      if (key && !(key in process.env)) process.env[key] = val;
    }
  } catch (_) {}
}
loadDotEnv(require('path').join(__dirname, '.env'));
loadDotEnv(require('os').homedir() + '/.env');

module.exports = {
  apps: [{
    name: 'vibers-invite-checker',
    script: '/root/vibers.onout.org/scripts/check-invites.py',
    interpreter: 'python3',
    autorestart: false,
    cron_restart: '*/1 * * * *',
    env: {
      TELEGRAM_API_ID: process.env.TELEGRAM_API_ID || '',
      TELEGRAM_SESSION_STRING: process.env.TELEGRAM_SESSION_STRING || '',
      TELEGRAM_API_HASH: process.env.TELEGRAM_API_HASH || '',
      TELEGRAM_CHAT_ID: process.env.TELEGRAM_CHAT_ID || '-5058393445',
    }
  }, {
    name: 'vibers-feedback',
    script: '/root/vibers.onout.org/scripts/feedback-server.py',
    interpreter: 'python3',
    autorestart: true,
    env: {
      TELEGRAM_API_ID: process.env.TELEGRAM_API_ID || '',
      TELEGRAM_SESSION_STRING: process.env.TELEGRAM_SESSION_STRING || '',
      TELEGRAM_API_HASH: process.env.TELEGRAM_API_HASH || '',
      TELEGRAM_CHAT_ID: process.env.TELEGRAM_CHAT_ID || '-5058393445',
      TELEGRAM_REVIEW_CHAT_ID: process.env.TELEGRAM_REVIEW_CHAT_ID || '-5208301843',
      FEEDBACK_PORT: '3847',
      GH_APP_ID: process.env.GH_APP_ID || '',
      GH_APP_PRIVATE_KEY_PATH: process.env.GH_APP_PRIVATE_KEY_PATH || '',
      GH_WEBHOOK_SECRET: process.env.GH_WEBHOOK_SECRET || '',
      GH_APP_SLUG: process.env.GH_APP_SLUG || 'vibers-review',
    }
  }]
};
