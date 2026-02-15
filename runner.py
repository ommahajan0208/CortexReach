"""
Enhanced Runner - Orchestrates workflow with fake test data
Coordinates all layers and manages the flow from input to output
"""

import sys
import os

# Import Rich console manager
from layers.visualization_layer.console_manager import (
    console,
    print_step,
    print_success,
    print_error,
    print_warning,
    print_info,
    print_hooks_table,
    print_persona_info,
    print_channel_output,
    print_validation_result,
    print_prospect_card,
    print_divider,
    create_progress_bar
)

# Import enhanced loader
from enhanced_prospect_loader import get_enhanced_user_inputs

# Import all layer functions
from layers.input_layer.prospect_loader import merge_prospect_data
from layers.input_layer.linkedin_scraper import scrape_linkedin_profile
from layers.input_layer.website_scraper import scrape_company_website
from layers.input_layer.x_scraper import scrape_x_profile
from layers.input_layer.github_scraper import scrape_github_profile

from layers.analysis_layer.persona_analyzer import analyze_persona
from layers.analysis_layer.hook_extractor import extract_hooks

from layers.context_layer.company_matcher import find_same_company_prospects
from layers.context_layer.insight_reuser import reuse_company_insights, save_company_insights
from layers.context_layer.reference_builder import build_company_reference

from layers.generation_layer.llm_config import get_llm_config
from layers.generation_layer.llm_interface import generate_with_llm, generate_for_channel
from layers.generation_layer.regenerator import regenerate_content

from layers.optimization_layer.critic_optimizer import apply_critic_pass

from layers.validation_layer.privacy_checker import validate_privacy
from layers.validation_layer.ethics_validator import validate_ethics_and_display

from layers.storage_layer.client_manager import get_or_create_client_id
from layers.storage_layer.json_storage import save_prospect


def run_enhanced_outreach_engine():
    """
    Enhanced orchestrator function - runs the complete workflow with fake/live data support
    """
    
    # Step 1: Get or create client ID
    print_step("Client Management", 1)
    client_id = get_or_create_client_id()
    
    # Step 2: Configure LLM
    print_step("LLM Configuration", 2)
    llm_config = get_llm_config()
    
    if not llm_config:
        print_error("LLM configuration failed. Exiting.")
        return
    
    # Step 3: Get user inputs
    print_step("Input Collection", 3)
    user_inputs = get_enhanced_user_inputs()
    
    if not user_inputs:
        print_error("Input collection failed. Exiting.")
        return
    
    # Step 4: Get prospect data from fake data
    print_step("Data Collection", 4)
    
    prospect_data = user_inputs['prospect_data']
    
    # Show prospect card
    print_prospect_card(prospect_data)
    
    # Show what data sources are included
    console.print("\n[bold]Data sources included:[/bold]")
    print_success("LinkedIn (name, role, company, bio, skills)")
    print_success("Website (company info, industry, tech stack)")
    print_success(f"Twitter/X ({len(prospect_data['recent_activity'])} activities)")
    if prospect_data['projects']:
        print_success(f"GitHub ({len(prospect_data['projects'])} projects)")
    
    print_success(f"Prospect data ready: {prospect_data.get('name', 'Unknown')}")
    
    # Step 5: Analyze prospect
    print_step("Prospect Analysis", 5)
    
    # Analyze persona
    console.print("\n[bold blue]→[/bold blue] Analyzing persona...")
    persona = analyze_persona(prospect_data, generate_with_llm, llm_config)
    print_persona_info(persona)
    
    # Extract hooks (this will now display the hooks table automatically)
    console.print("\n[bold blue]→[/bold blue] Extracting personalization hooks...")
    hooks = extract_hooks(prospect_data, generate_with_llm, llm_config)
    
    # Step 6: Context & Learning
    print_step("Context & Learning", 6)
    
    company_name = prospect_data.get('company')
    same_company_prospects = find_same_company_prospects(company_name, client_id)
    
    company_context = reuse_company_insights(
        company_name, 
        same_company_prospects, 
        client_id
    )
    
    reference = build_company_reference(same_company_prospects)
    
    # Step 7: Generate content for selected channels
    print_step("Content Generation & Optimization", 7)
    
    generated_outputs = {}
    
    # Create progress bar
    with create_progress_bar("Generating content...") as progress:
        task = progress.add_task("Processing channels", total=len(user_inputs['selected_channels']))
        
        for channel in user_inputs['selected_channels']:
            try:
                progress.update(task, description=f"[cyan]Generating {channel.upper()}...")
                
                # Generate initial content
                content = generate_for_channel(
                    prospect_data,
                    persona,
                    hooks,
                    company_context,
                    reference,
                    channel,
                    llm_config
                )
                
                # Apply critic pass automatically
                if content:
                    progress.update(task, description=f"[yellow]Optimizing {channel.upper()}...")
                    optimized_content = apply_critic_pass(
                        content,
                        channel,
                        prospect_data,
                        persona,
                        llm_config,
                        generate_with_llm
                    )
                    generated_outputs[channel] = optimized_content
                    print_success(f"{channel.upper()} generated ({len(optimized_content)} chars)")
                else:
                    generated_outputs[channel] = None
                
                progress.advance(task)
                
            except Exception as e:
                print_error(f"Error generating {channel} content: {str(e)}")
                generated_outputs[channel] = None
                progress.advance(task)
    
    # Step 8: Validate and display results
    print_step("Validation & Output", 8)
    
    # Display each channel's output
    for channel, content in generated_outputs.items():
        if content:
            display_channel_output(channel, content, prospect_data)
    
    # Regeneration loop
    while True:
        print_divider()
        console.print("\n[bold yellow]OPTIONS:[/bold yellow]")
        console.print("  [cyan]1.[/cyan] Regenerate specific channel")
        console.print("  [green]2.[/green] Save and finish")
        console.print("  [red]3.[/red] Exit without saving")
        print_divider()
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            # Regeneration
            channel_to_regen = select_channel_for_regeneration(user_inputs['selected_channels'])
            
            if channel_to_regen and channel_to_regen in generated_outputs:
                modifications = input("\nWhat changes do you want? (be specific): ").strip()
                
                if modifications:
                    console.print(f"\n[bold cyan]→[/bold cyan] Regenerating {channel_to_regen.upper()} with modifications...")
                    regenerated = regenerate_content(
                        generated_outputs[channel_to_regen],
                        modifications,
                        channel_to_regen,
                        llm_config,
                        generate_with_llm
                    )
                    
                    # Validate regenerated content
                    console.print("\n[bold]Validating regenerated content...[/bold]")
                    privacy_ok = validate_privacy(regenerated, prospect_data)
                    ethics_ok = validate_ethics_and_display(regenerated)
                    
                    if privacy_ok and ethics_ok:
                        generated_outputs[channel_to_regen] = regenerated
                        print_success(f"Regenerated {channel_to_regen.upper()} successfully validated!")
                        display_channel_output(channel_to_regen, regenerated, prospect_data)
                    else:
                        print_warning("Regenerated content has issues. Keeping original.")
        
        elif choice == '2':
            # Save and finish
            console.print("\n[bold cyan]→[/bold cyan] Saving results...")
            save_prospect(prospect_data, generated_outputs, client_id)
            
            # Save company insights for future reuse
            save_company_insights(company_name, company_context, prospect_data, client_id)
            
            print_divider()
            console.print("\n[bold green]✓ OUTREACH GENERATION COMPLETE![/bold green]")
            print_divider()
            console.print(f"\n[bold]Prospect:[/bold] [cyan]{prospect_data.get('name', 'Unknown')}[/cyan]")
            console.print(f"[bold]Company:[/bold] [green]{prospect_data.get('company', 'Unknown')}[/green]")
            console.print(f"[bold]Channels Generated:[/bold] [yellow]{len(user_inputs['selected_channels'])}[/yellow]")
            console.print(f"  • {', '.join(user_inputs['selected_channels'])}")
            console.print(f"\n[bold]Client ID:[/bold] [dim]{client_id}[/dim]")
            
            if user_inputs.get('mode') == 'fake' and user_inputs.get('prospect_id'):
                console.print(f"[bold]Data Mode:[/bold] [magenta]FAKE[/magenta] (Prospect ID: {user_inputs['prospect_id']})")
            
            print_success("Results saved successfully!")
            print_divider()
            break
        
        elif choice == '3':
            console.print("\n[yellow]Exiting without saving...[/yellow]")
            break


def display_channel_output(channel, content, prospect_data):
    """Display output for a specific channel with validation and clear formatting"""
    
    # Use rich console for beautiful output
    print_channel_output(channel, content)
    
    # Validation
    console.print("\n[bold]VALIDATION:[/bold]")
    privacy_ok = validate_privacy(content, prospect_data)
    print_validation_result("Privacy check", privacy_ok)
    
    ethics_ok = validate_ethics_and_display(content)
    print_validation_result("Ethics check", ethics_ok)
    
    if privacy_ok and ethics_ok:
        print_success("All validation checks passed")
    else:
        print_warning("Some validation issues found (see above)")


def select_channel_for_regeneration(available_channels):
    """Let user select which channel to regenerate"""
    console.print("\n[bold]Select channel to regenerate:[/bold]")
    for i, channel in enumerate(available_channels, 1):
        console.print(f"  [cyan]{i}.[/cyan] {channel.upper()}")
    
    choice = input("\nEnter channel number: ").strip()
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(available_channels):
            return available_channels[idx]
    except:
        pass
    
    print_error("Invalid selection.")
    return None


if __name__ == "__main__":
    try:
        run_enhanced_outreach_engine()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]⚠ Interrupted by user. Exiting...[/yellow]")
    except Exception as e:
        console.print(f"\n\n[bold red]✗ Fatal error: {str(e)}[/bold red]")
        import traceback
        traceback.print_exc()
