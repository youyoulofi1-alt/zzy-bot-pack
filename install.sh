#!/bin/bash

# Termux installation helper for Djezzy Bot
# Usage example:
#   git clone https://github.com/youyoulofi1-alt/zzy-bot-pack.git
#   cd zzy-bot-pack
#   chmod +x install.sh
#   BOT_TOKEN="..." CHAT_ID="123456" ./install.sh

set -e

# ensure we are running inside Termux
if [[ -z "$PREFIX" || ! -d "$PREFIX" ]]; then
    echo "⚠️  It looks like you are not running inside Termux. Please open Termux and run the script again."
    exit 1
fi

echo "📦 Updating packages..."
pkg update -y && pkg upgrade -y

# install python and git if needed
pkg install -y python git

# create virtual environment
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment (venv)..."
    python3 -m venv venv
fi

# activate virtual environment
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# write .env file from provided variables
if [ -z "$BOT_TOKEN" ]; then
    echo "❌ BOT_TOKEN variable is not set. Define it before running the script, for example: BOT_TOKEN=..."
    exit 1
fi

cat > .env <<EOF
TELEGRAM_BOT_TOKEN=$BOT_TOKEN
# optional administrator/user allowed to see stats
ADMIN_ID=${CHAT_ID:-}
EOF

echo "✅ .env file has been created."

# create data directories just in case
mkdir -p data logs config

# finally start
echo "🚀 Starting the bot..."
python3 run.sh