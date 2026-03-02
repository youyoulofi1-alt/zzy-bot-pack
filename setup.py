#!/usr/bin/env python3
"""
Setup Guide - Djezzy Tool
"""

import os
import sys
import subprocess
import platform


def print_header(title):
    """Print section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def check_python_version():
    """Check if Python version is compatible"""
    print_header("1️⃣  Checking Python Version")
    
    version = sys.version_info
    print(f"Current Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Version is compatible!")
        return True
    else:
        print("❌ Python 3.8 or later is required")
        return False


def install_requirements():
    """Install required packages"""
    print_header("2️⃣  Installing Required Libraries")
    
    requirements_file = "requirements.txt"
    
    if not os.path.exists(requirements_file):
        print(f"❌ {requirements_file} not found")
        return False
    
    try:
        print("Installing libraries...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("\n✅ All libraries installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Installation failed: {e}")
        return False


def check_files():
    """Check if all required files exist"""
    print_header("3️⃣  Checking Required Files")
    
    required_files = {
        "djezzy_utils.py": "Core utility module",
        "djezzy_bot.py": "Telegram bot",
        "cli_runner.py": "Command line interface",
        "requirements.txt": "Library list",
    }
    
    all_exist = True
    for filename, description in required_files.items():
        if os.path.exists(filename):
            print(f"✅ {filename:<20} - {description}")
        else:
            print(f"❌ {filename:<20} - {description} (Missing)")
            all_exist = False
    
    return all_exist


def setup_environment():
    """Setup environment"""
    print_header("4️⃣  Setting up Environment")
    
    # Create logs directory if needed
    log_dir = os.path.dirname("djezzy_tool.log")
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"✅ Logs directory created")
    
    # Check permissions
    if not os.access(".", os.W_OK):
        print("❌ No write permissions in the current directory")
        return False
    
    print("✅ Environment is ready")
    return True


def show_usage_guide():
    """Show usage guide"""
    print_header("📖 Usage Guide")
    
    print("""
1️⃣  Run the Telegram Bot:
    python djezzy_bot.py
    
    (Make sure to set the Telegram Bot Token before running)

2️⃣  Run the Command Line Interface (CLI):
    python cli_runner.py
    
    (Interactive interface without needing Telegram)

3️⃣  Use the module in another project:
    
    from djezzy_utils import *
    
    # Request OTP
    response = request_otp("213770123456")
    
    # Login
    token = login_with_otp("213770123456", "123456")
    
    # Register number
    success, message, data = register_with_number(
        "213770123456", 
        "123456"
    )
""")


def show_telegram_setup():
    """Show Telegram bot setup instructions"""
    print_header("🤖 Telegram Bot Setup")
    
    print("""
Steps:

1. Open Telegram and search for @BotFather
2. Send /newbot
3. Follow the instructions:
   - Choose a bot name (e.g., Djezzy Bot)
   - Choose a username (e.g., djezzy_algo_bot)
4. Telegram will send you a message with your Token
5. Copy the Token and save it
6. Open djezzy_bot.py and place the Token in the designated location:
   
   TOKEN = "YOUR_ACTUAL_BOT_TOKEN"

7. Run:
   python djezzy_bot.py

8. Start a conversation with the bot on Telegram
   Send /start
""")


def create_config_template():
    """Create config file template"""
    print_header("⚙️  Creating Config File (Optional)")
    
    config_content = """{
    "telegram": {
        "token": "YOUR_BOT_TOKEN_HERE",
        "debug": false
    },
    "djezzy": {
        "max_attempts": 50,
        "timeout": 10,
        "retry_delay": 1
    },
    "logging": {
        "level": "INFO",
        "file": "djezzy_tool.log"
    }
}
"""
    
    config_file = "config.json"
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_content)
        print(f"✅ {config_file} created")
        print("   Settings can be modified in this file")
    else:
        print(f"ℹ️  {config_file} already exists")


def final_checklist():
    """Show final checklist"""
    print_header("✅ Final Checklist")
    
    checklist = [
        ("Python 3.8+", "Python Version"),
        ("python-telegram-bot", "Telegram Library"),
        ("requests", "Requests Library"),
        ("djezzy_utils.py", "Core File"),
        ("djezzy_bot.py", "Bot File"),
        ("cli_runner.py", "Command Line Interface"),
    ]
    
    print("Check the following:")
    for item, desc in checklist:
        print(f"  ☐ {item:<30} - {desc}")
    
    print("\n" + "="*60)
    print("🎉 You are ready to start!")
    print("="*60)


def main():
    """Main setup process"""
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  Setup Guide - Djezzy Tool".center(58) + "█")
    print("█" + "  Djezzy Tool - Setup Guide".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    # Run checks
    if not check_python_version():
        print("\n❌ Setup stopped: Incompatible Python version")
        return False
    
    if not check_files():
        print("\n⚠️  Warning: Some files are missing")
    
    if input("\n🔧 Install requirements? (y/n): ").lower() == 'y':
        if not install_requirements():
            print("\n❌ Installation failed")
            return False
    
    if not setup_environment():
        print("\n❌ Setup failed")
        return False
    
    show_usage_guide()
    
    if input("\n📖 Show Telegram Bot Setup Guide? (y/n): ").lower() == 'y':
        show_telegram_setup()
    
    if input("\n⚙️  Create Config File? (y/n): ").lower() == 'y':
        create_config_template()
    
    final_checklist()
    
    print("\n" + "="*60)
    print("\n💡 Tips:")
    print("  • Keep your Bot Token secure")
    print("  • Do not share your Bot Token with anyone")
    print("  • Use environment variables for the Token in production")
    print("  • Read README.md for more information")
    print("  • Check 'djezzy_tool.log' logs for errors")
    
    print("\n" + "="*60)
    print("\n👋 Goodbye:")
    print("  • Run the bot: python djezzy_bot.py")
    print("  • Command line interface: python cli_runner.py")
    
    print("\n" + "="*60 + "\n")
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)