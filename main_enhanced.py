"""
CortexReach - Enhanced Main Entry Point
Supports both fake data (for testing) and live scraping (for production)
"""

import os
import sys


def display_banner():
    """Display welcome banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║                          CORTEXREACH                                 ║
    ║         Hyper-Personalized Cold Outreach Engine                      ║
    ║                                                                      ║
    ║                 Powered by Offline LLMs                              ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    
    ✨ NEW: DUAL MODE SUPPORT ✨
    
    🎯 FAKE DATA MODE:
       - 10 comprehensive test prospects
       - Covers all features (LinkedIn, Website, X, GitHub)
       - Diverse personas (Technical, Executive, Founders, Researchers)
       - Multiple prospects from same companies (tests context reuse)
       - Perfect for testing and demonstrations
    
    🌐 LIVE SCRAPING MODE:
       - Real-time data collection
       - LinkedIn, Website, Twitter/X, GitHub
       - Production-ready outreach generation
    
    📊 FEATURES:
       ✓ Multi-source data collection
       ✓ Intelligent persona analysis
       ✓ Engagement scoring (0-100)
       ✓ Hook extraction for personalization
       ✓ Company context reuse (learning from past outreach)
       ✓ Multi-channel output (Email, WhatsApp, SMS, LinkedIn, Instagram)
       ✓ Privacy & ethics validation
       ✓ Content regeneration with modifications
       ✓ Offline LLM (complete privacy)
    
    ════════════════════════════════════════════════════════════════════════
    """
    print(banner)


def check_prerequisites():
    """Check if prerequisites are met"""
    print("CHECKING PREREQUISITES...")
    print("─" * 70)
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("⚠ Warning: Python 3.8+ recommended")
    else:
        print("✓ Python version OK")
    
    # Check if Ollama is accessible (optional check)
    try:
        import requests
        response = requests.get('http://localhost:11434/api/tags', timeout=2)
        if response.status_code == 200:
            print("✓ Ollama is running")
        else:
            print("⚠ Ollama may not be running")
    except:
        print("⚠ Could not verify Ollama status")
        print("  Make sure Ollama is installed and running:")
        print("  https://ollama.ai")
    
    # Check for data directory
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✓ Created data directory")
    else:
        print("✓ Data directory exists")
    
    print("─" * 70)
    print()


def display_quick_help():
    """Display quick help information"""
    help_text = """
    QUICK HELP:
    ──────────
    
    When to use FAKE DATA mode:
      • Testing the system
      • Demonstrating features
      • Learning how it works
      • Quick iterations
      • No internet/scraping needed
    
    When to use LIVE SCRAPING mode:
      • Production use
      • Real prospects
      • Actual outreach campaigns
      • Need fresh data
    
    Available fake prospects:
      • 3 Technical professionals (engineers, DevOps)
      • 2 Executives (VP, CTO)
      • 3 Founders/Entrepreneurs (CEOs, CTOs)
      • 2 Researchers/Academics (PhD, research scientists)
    
    Multiple prospects from:
      • TechCorp AI (2 prospects)
      • EcoTrack (2 prospects)
      • QuantumTech Labs (2 prospects)
    
    This tests the company context reuse feature!
    
    ════════════════════════════════════════════════════════════════════════
    """
    print(help_text)


def main():
    """Main entry point"""
    # Clear screen (optional)
    # os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display banner
    display_banner()
    
    # Optional: Display help
    show_help = input("Show detailed help? (y/n, default: n): ").strip().lower()
    if show_help == 'y':
        display_quick_help()
    
    # Check prerequisites
    check_prerequisites()
    
    # Ask if ready to continue
    input("Press ENTER to start...")
    
    # Import and run the enhanced runner
    try:
        from enhanced_runner import run_enhanced_outreach_engine
        run_enhanced_outreach_engine()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        print("\n\nIf you see errors about missing modules:")
        print("  pip install -r requirements.txt")
        print("\nIf you see Ollama connection errors:")
        print("  Make sure Ollama is installed and running")
        print("  Visit: https://ollama.ai")


if __name__ == "__main__":
    main()
