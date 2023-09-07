
# BscScan Telegram bot Django 

Telegram bot for following and searching for transactions by address in BscScan.

# Setup and run

### Set up .env
Create .env file in root directory with following fields:

```
WEB_SECRET_KEY=XXX
WEB_HOST=http://127.0.0.1:8000
DB_NAME=bscscan_bot
DB_USER=bscscan_bot
DB_PASSWORD=123456
DB_PORT=5432
DB_HOST=postgres
LOG_DJANGO=web/logs/django_request.log
BACKEND_QUEUE=backend_queue

TELEGRAM_TOKEN=XXX
TELEGRAM_BOT_NAME=bscscan_bot
TELEGRAM_LOG=web/logs/bot.log

BSCSCAN_URL=https://api-testnet.bscscan.com/api
BSCSCAN_API_KEY=XXX

REDIS_HOST=redis
DJANGO_DEBUG=True
```

### Run with docker
```
docker-compose up
```

