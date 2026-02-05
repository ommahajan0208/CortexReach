"""
Main Entry Point - Offline LLM-Powered Hyper-Personalized Cold Outreach Engine

Run this file to start the application:
    python main.py
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from runner import run_outreach_engine


def display_welcome():
    """Display welcome banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                   WELCOME TO CORTEXREACH ENGINE                      ║
║                                                                      ║
║   Generate highly personalized outreach messages across multiple     ║
║   channels using offline LLMs and intelligent data analysis.         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

Features:
  -> Multi-source data collection (LinkedIn, Website, Twitter/X, GitHub)
  -> AI-powered persona analysis and hook extraction
  -> Company context reuse and smart referencing
  -> Multi-channel output (Email, WhatsApp, SMS, LinkedIn, Instagram)
  -> Privacy and ethics validation
  -> Client-based data storage and learning

"""
    print(banner)


def check_requirements():
    """Check if required packages are installed"""
    try:
        import requests
        import bs4
    except ImportError:
        print("Missing required packages. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Packages installed successfully!\n")


def main():
    """Main entry point"""
    display_welcome()
    
    # Check requirements
    check_requirements()
    
    input("\nPress Enter to start...")
    print("CortexReach Engine Initialized")
    # Run the engine
    try:
        run_outreach_engine()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
