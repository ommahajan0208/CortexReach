"""
CortexReach - Enhanced Main Entry Point
Fake data mode only - 10 comprehensive test prospects with Rich TUI
"""

import os
import sys
from rich.console import Console

console = Console()


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
    
    🎯 TEST DATA MODE - 10 COMPREHENSIVE PROSPECTS
    
    📂 AVAILABLE DATA:
       - 10 diverse test prospects
       - Covers all features (LinkedIn, Website, X, GitHub)
       - Multiple personas (Technical, Executive, Founders, Researchers)
       - Same-company prospects (tests context reuse)
       - Perfect for testing and demonstrations
    
    💡 FEATURES:
       ✓ Multi-source data collection
       ✓ Intelligent persona analysis
       ✓ High-signal hook extraction
       ✓ Company context reuse (learning from past outreach)
       ✓ Multi-channel output (Email, WhatsApp, SMS, LinkedIn, Instagram)
       ✓ Privacy & ethics validation
       ✓ Content regeneration with modifications
       ✓ Offline LLM (complete privacy)
    
    ════════════════════════════════════════════════════════════════════════
    """
    console.print(banner, style="bold cyan")


def check_prerequisites():
    """Check if prerequisites are met"""
    console.print("\n[bold]CHECKING PREREQUISITES...[/bold]")
    console.print("─" * 70)
    
    # Check Python version
    python_version = sys.version_info
    console.print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        console.print("[yellow]⚠ Warning: Python 3.8+ recommended[/yellow]")
    else:
        console.print("[green]✓ Python version OK[/green]")
    
    # Check if Ollama is accessible (optional check)
    try:
        import requests
        response = requests.get('http://localhost:11434/api/tags', timeout=2)
        if response.status_code == 200:
            console.print("[green]✓ Ollama is running[/green]")
        else:
            console.print("[yellow]⚠ Ollama may not be running[/yellow]")
    except:
        console.print("[yellow]⚠ Could not verify Ollama status[/yellow]")
        console.print("  Make sure Ollama is installed and running:")
        console.print("  https://ollama.ai")
    
    # Check for data directory
    if not os.path.exists('data'):
        os.makedirs('data')
        console.print("[green]✓ Created data directory[/green]")
    else:
        console.print("[green]✓ Data directory exists[/green]")
    
    console.print("─" * 70)
    console.print()


def display_quick_help():
    """Display quick help information"""
    help_text = """
    QUICK HELP:
    ──────────
    
    🎯 TEST DATA - 10 COMPREHENSIVE PROSPECTS:
    
    Available fake prospects:
      • 3 Technical professionals (engineers, DevOps)
      • 2 Executives (VP, CTO)
      • 3 Founders/Entrepreneurs (CEOs, CTOs)
      • 2 Researchers/Academics (PhD, research scientists)
    
    Multiple prospects from same companies:
      • TechCorp AI (2 prospects)
      • EcoTrack (2 prospects)
      • QuantumTech Labs (2 prospects)
    
    This tests the company context reuse feature!
    
    ════════════════════════════════════════════════════════════════════════
    """
    console.print(help_text, style="dim")


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
        console.print("\n\n[yellow]⚠ Interrupted by user. Exiting...[/yellow]")
    except Exception as e:
        console.print(f"\n\n[bold red]✗ Fatal error: {str(e)}[/bold red]")
        import traceback
        traceback.print_exc()
        console.print("\n\n[yellow]If you see errors about missing modules:[/yellow]")
        console.print("  [cyan]pip install -r requirements.txt[/cyan]")
        console.print("\n[yellow]If you see Ollama connection errors:[/yellow]")
        console.print("  Make sure Ollama is installed and running")
        console.print("  Visit: [cyan]https://ollama.ai[/cyan]")


if __name__ == "__main__":
    main()
