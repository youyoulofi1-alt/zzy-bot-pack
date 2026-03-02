#!/usr/bin/env python3
"""
Standalone CLI Runner - Use the tool without the bot
You can use djezzy_utils.py independently from anywhere

Usage:
    python cli_runner.py
"""

import sys
import os
from datetime import datetime

try:
    import djezzy_utils
except ImportError:
    print("❌ Error: djezzy_utils.py not found")
    print("Make sure the file is in the same directory")
    sys.exit(1)


def print_banner():
    """Print welcome banner"""
    print("\n" + "=" * 50)
    print("     Djezzy 1GB Registration Tool")
    print("     (Standalone Version - CLI)")
    print("=" * 50 + "\n")


def print_menu():
    """Print main menu"""
    print("\n" + "-" * 50)
    print("Main Menu:")
    print("1. Register a new number")
    print("2. View statistics")
    print("3. View recent registrations")
    print("4. Exit")
    print("-" * 50)


def register_new_number():
    """Register a new number"""
    print("\n📱 Register a new number")
    print("-" * 50)
    
    while True:
        sender = input("\n📱 Enter Djezzy number (e.g., 0770123456): ").strip()
        if not sender:
            print("❌ Number is required")
            continue
        
        try:
            sender_f = djezzy_utils.format_num(sender)
            break
        except Exception as e:
            print(f"❌ Error in number format: {e}")
            continue
    
    print(f"✓ Formatted number: {sender_f}")
    print("\n🔄 Sending OTP code...")
    
    otp_response = djezzy_utils.request_otp(sender_f)
    
    if otp_response and otp_response.status_code in [200, 201]:
        print("✅ OTP sent successfully")
        otp = input("\n📨 Enter the code you received: ").strip()
        
        if not otp:
            print("❌ Code is required")
            return
        
        print("\n🔄 Processing the request...")
        print("📡 Trying until a valid number is found...\n")
        
        def progress(msg):
            print(f"  {msg}")
        
        success, message, data = djezzy_utils.register_with_number(
            sender_f,
            otp,
            max_attempts=50,
            callback=progress
        )
        
        if success:
            print("\n" + "=" * 50)
            print("✅✅✅ Registration successful! ✅✅✅")
            print("=" * 50)
            print(f"\nSent number: {data['sender']}")
            print(f"Target number: {data['target']}")
            print(f"Time: {data['timestamp']}")
            print(f"\n🎉 You have received 1GB for free!")
        else:
            print(f"\n❌ Operation failed")
            print(f"Message: {message}")
    else:
        print("❌ OTP sending failed")
        print("Check the number and try again")


def show_statistics():
    """Show statistics"""
    count = djezzy_utils.get_registered_count()
    print("\n" + "=" * 50)
    print("📊 Statistics")
    print("=" * 50)
    print(f"\n✅ Number of registered numbers: {count}")
    print(f"📅 Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()


def show_recent():
    """Show recent registrations"""
    recent = djezzy_utils.get_recent_registrations(limit=20)
    
    print("\n" + "=" * 50)
    print("📋 Recent Registrations")
    print("=" * 50)
    
    if not recent:
        print("\n❌ No registrations found yet")
    else:
        print(f"\n📊 Number of registrations: {len(recent)}\n")
        print(f"{'#':<4} {'Sender Number':<15} {'Target Number':<15} {'Time':<20}")
        print("-" * 54)
        
        for i, reg in enumerate(recent[::-1], 1):
            sender = reg['sender'][-10:] if len(reg['sender']) > 10 else reg['sender']
            target = reg['target'][-10:] if len(reg['target']) > 10 else reg['target']
            timestamp = reg['timestamp']
            print(f"{i:<4} {sender:<15} {target:<15} {timestamp:<20}")
    print()


def main():
    """Main function"""
    print_banner()
    
    registered = djezzy_utils.load_registered_numbers()
    if registered:
        print(f"📊 Previously registered numbers: {len(registered)}\n")
    
    while True:
        print_menu()
        choice = input("\n👉 Choose operation number (1-4): ").strip()
        
        if choice == "1":
            register_new_number()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            show_recent()
        elif choice == "4":
            print("\n👋 Thank you for using the tool. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Try again")
        
        input("\n👈 Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)