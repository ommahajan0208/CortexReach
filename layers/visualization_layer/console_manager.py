"""
Console Manager - Beautiful terminal output using Rich library
"""

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.text import Text
from rich import box
from rich.markdown import Markdown

# Global console instance
console = Console()


def print_step(step_name, step_number, total_steps=8):
    """
    Print a beautiful step header
    
    Args:
        step_name: str - Name of the step
        step_number: int - Current step number
        total_steps: int - Total number of steps
    """
    title = f"[bold cyan][{step_number}/{total_steps}] {step_name.upper()}[/bold cyan]"
    console.print(Panel(title, border_style="cyan", box=box.DOUBLE))


def print_success(message):
    """Print success message with green checkmark"""
    console.print(f"[bold green]✓[/bold green] {message}")


def print_error(message):
    """Print error message with red X"""
    console.print(f"[bold red]✗[/bold red] {message}")


def print_warning(message):
    """Print warning message with yellow triangle"""
    console.print(f"[bold yellow]⚠[/bold yellow]  {message}")


def print_info(message):
    """Print info message with blue dot"""
    console.print(f"[bold blue]•[/bold blue] {message}")


def print_section_header(title):
    """Print a section header"""
    console.print(f"\n[bold magenta]{title}[/bold magenta]")
    console.print("[dim]" + "─" * 70 + "[/dim]")


def print_data_table(title, data_dict):
    """
    Print data as a formatted table
    
    Args:
        title: str - Table title
        data_dict: dict - Key-value pairs to display
    """
    table = Table(title=title, show_header=True, header_style="bold cyan", border_style="blue", box=box.ROUNDED)
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")
    
    for key, value in data_dict.items():
        # Truncate long values
        value_str = str(value)
        if len(value_str) > 80:
            value_str = value_str[:77] + "..."
        table.add_row(key, value_str)
    
    console.print(table)


def print_hooks_table(hooks):
    """
    Print personalization hooks as a beautiful table
    
    Args:
        hooks: list - List of hook dictionaries
    """
    if not hooks:
        print_warning("No hooks extracted")
        return
    
    table = Table(
        title="[bold cyan]🎯 Personalization Hooks[/bold cyan]",
        show_header=True,
        header_style="bold yellow",
        border_style="green",
        box=box.ROUNDED
    )
    
    table.add_column("#", justify="right", style="cyan", width=3)
    table.add_column("Type", style="magenta", width=15)
    table.add_column("Hook", style="white")
    
    for i, hook in enumerate(hooks, 1):
        hook_text = hook.get('hook_text', '')
        hook_type = hook.get('hook_type', 'general')
        
        # Truncate long hooks
        if len(hook_text) > 70:
            hook_text = hook_text[:67] + "..."
        
        table.add_row(str(i), hook_type, hook_text)
    
    console.print(table)


def print_persona_info(persona):
    """
    Print persona analysis information
    
    Args:
        persona: dict - Persona analysis data
    """
    style = persona.get('communication_style', 'unknown')
    
    style_colors = {
        'technical': 'cyan',
        'executive': 'magenta',
        'casual': 'green',
        'formal': 'blue'
    }
    
    color = style_colors.get(style, 'white')
    
    console.print(f"\n[bold]Persona:[/bold] [{color}]{style.upper()}[/{color}]")


def print_channel_output(channel, content):
    """
    Print generated content for a channel
    
    Args:
        channel: str - Channel name
        content: str - Generated content
    """
    channel_emoji = {
        'email': '📧',
        'whatsapp': '💬',
        'sms': '📱',
        'linkedin': '💼',
        'instagram': '📸'
    }
    
    emoji = channel_emoji.get(channel.lower(), '📨')
    
    panel = Panel(
        content,
        title=f"[bold yellow]{emoji} {channel.upper()}[/bold yellow]",
        border_style="yellow",
        box=box.HEAVY,
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(panel)
    
    # Print stats
    char_count = len(content)
    word_count = len(content.split())
    console.print(f"[dim]Length: {char_count} characters | {word_count} words[/dim]")


def create_progress_bar(description):
    """
    Create a progress bar with spinner
    
    Args:
        description: str - Description of the progress
    
    Returns:
        Progress object
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(complete_style="green", finished_style="bold green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    )


def print_validation_result(check_name, passed, message=None):
    """
    Print validation check result
    
    Args:
        check_name: str - Name of the validation check
        passed: bool - Whether the check passed
        message: str - Optional message
    """
    if passed:
        console.print(f"  [bold green]✓[/bold green] {check_name} [dim]passed[/dim]")
    else:
        console.print(f"  [bold red]✗[/bold red] {check_name} [dim]failed[/dim]")
        if message:
            console.print(f"    [yellow]{message}[/yellow]")


def print_divider():
    """Print a visual divider"""
    console.print("[dim]" + "═" * 70 + "[/dim]")


def print_prospect_card(prospect_data):
    """
    Print prospect information as a card
    
    Args:
        prospect_data: dict - Prospect information
    """
    name = prospect_data.get('name', 'Unknown')
    role = prospect_data.get('role', 'Unknown')
    company = prospect_data.get('company', 'Unknown')
    industry = prospect_data.get('industry', 'Unknown')
    
    card_text = f"""
[bold cyan]{name}[/bold cyan]
[yellow]{role}[/yellow] at [green]{company}[/green]
[dim]Industry: {industry}[/dim]
"""
    
    panel = Panel(
        card_text.strip(),
        title="[bold magenta]👤 Prospect Profile[/bold magenta]",
        border_style="magenta",
        box=box.DOUBLE,
        padding=(1, 2)
    )
    
    console.print("\n")
    console.print(panel)
