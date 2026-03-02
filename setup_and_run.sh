#!/bin/bash
set -e

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    echo "⚡ Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install libraries
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check required environment variables
if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ -z "$TELEGRAM_CHAT_ID" ]; then
    echo "❌ TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set"
    echo "Example:"
    echo "export TELEGRAM_BOT_TOKEN='your_token'"
    echo "export TELEGRAM_CHAT_ID='your_chat_id'"
    exit 1
fi

# Start the bot
echo "🚀 Starting the bot..."
./run.sh