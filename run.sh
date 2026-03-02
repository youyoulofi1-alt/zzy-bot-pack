#!/bin/bash

# Djezzy Bot - Linux/macOS Launcher
# Runtime launcher for Linux and macOS

set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}"
echo "╔════════════════════════════════════════╗"
echo "║        Welcome to Djezzy Bot          ║"
echo "║      Djezzy Bot - Standalone          ║"
echo "╚════════════════════════════════════════╝"
echo -e "${NC}"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Error: Python 3 is not installed${NC}"
    echo "Please install Python 3 from: https://www.python.org"
    exit 1
fi

echo -e "${GREEN}✅ Python 3 is installed${NC}"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}📦 Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${YELLOW}🔄 Activating virtual environment...${NC}"
source venv/bin/activate

# Load environment variables from .env if the file exists
if [ -f ".env" ]; then
    echo -e "${YELLOW}📄 Loading environment variables from .env...${NC}"
    # export all variables defined in .env
    set -a
    # shellcheck disable=SC1091
    source .env
    set +a

    # simple sanity check in shell to catch default placeholder
    if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ "$TELEGRAM_BOT_TOKEN" = "YOUR_TELEGRAM_BOT_TOKEN_HERE" ]; then
        echo -e "${RED}❌ TELEGRAM_BOT_TOKEN is not set or still has the default value!${NC}"
        echo "Make sure to set it in .env or export it before running."
        exit 1
    fi
fi

# Install requirements
echo -e "${YELLOW}📥 Installing libraries...${NC}"
pip install -q -r requirements.txt

# Create necessary directories
mkdir -p data logs config

echo ""
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo -e "${GREEN}Select operating mode:${NC}"
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo ""
echo "1️⃣  🤖 Telegram Bot"
echo "2️⃣  💻 Command Line Interface (CLI)"
echo "3️⃣  🔧 Setup Program"
echo "4️⃣  📖 View Index"
echo "5️⃣  ❌ Exit"
echo ""

read -p "(1-5): Choose an option: " choice

case $choice in
    1)
        echo -e "${YELLOW}🤖 Starting Telegram Bot...${NC}"
        echo ""
        python3 djezzy_bot.py
        ;;
    2)
        echo -e "${YELLOW}💻 Starting Command Line Interface...${NC}"
        echo ""
        python3 cli_runner.py
        ;;
    3)
        echo -e "${YELLOW}🔧 Starting setup program...${NC}"
        echo ""
        python3 setup.py
        ;;
    4)
        echo -e "${YELLOW}📖 Displaying index...${NC}"
        echo ""
        python3 INDEX.py
        ;;
    5)
        echo -e "${GREEN}👋 Thank you for using the tool!${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}❌ Invalid selection${NC}"
        exit 1
        ;;
esac

# Deactivate virtual environment on exit
deactivate 2>/dev/null || true