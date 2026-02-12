"""
Runner - Orchestrates the entire workflow
Coordinates all layers and manages the flow from input to output
"""

# Import all layer functions
from layers.input_layer.prospect_loader import get_user_inputs, merge_prospect_data
from layers.input_layer.linkedin_scraper import scrape_linkedin_profile
from layers.input_layer.website_scraper import scrape_company_website
from layers.input_layer.x_scraper import scrape_x_profile
from layers.input_layer.github_scraper import scrape_github_profile

from layers.analysis_layer.persona_analyzer import analyze_persona
from layers.analysis_layer.engagement_scorer import calculate_engagement_score
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


def run_outreach_engine():
    """
    Main orchestrator function - runs the complete workflow
    """
    
    # Step 1: Get or create client ID
    print("\n[STEP 1/8] Client Management")
    client_id = get_or_create_client_id()
    
    # Step 2: Configure LLM
    print("\n[STEP 2/8] LLM Configuration")
    llm_config = get_llm_config()
    
    if not llm_config:
        print("\nLLM configuration failed. Exiting.")
        return
    
    # Step 3: Get user inputs (sources + channels)
    print("\n[STEP 3/8] Input Collection")
    user_inputs = get_user_inputs()
    
    if not user_inputs:
        print("\nInput collection failed. Exiting.")
        return
    
    # Step 4: Scrape data from selected sources
    print("\n[STEP 4/8] Data Collection")
    
    
    linkedin_data = None
    website_data = None
    x_data = None
    github_data = None
    
    if user_inputs['linkedin_url']:
        linkedin_data = scrape_linkedin_profile(user_inputs['linkedin_url'])
    
    if user_inputs['website_url']:
        website_data = scrape_company_website(user_inputs['website_url'])
    
    if user_inputs['x_url']:
        x_data = scrape_x_profile(user_inputs['x_url'])
    
    if user_inputs['github_url']:
        github_data = scrape_github_profile(user_inputs['github_url'])
    
    # Merge all data
    print("\n[INPUT] Merging data from all sources...")
    prospect_data = merge_prospect_data(linkedin_data, website_data, x_data, github_data)
    print(f"Prospect data merged: {prospect_data.get('name', 'Unknown')}")
    
    # Step 5: Analyze prospect
    print("\n[STEP 5/8] Prospect Analysis")
    
    
    # Analyze persona
    persona = analyze_persona(prospect_data, generate_with_llm, llm_config)
    
    # Calculate engagement score
    engagement_score = calculate_engagement_score(prospect_data, persona)
    
    # Extract hooks
    hooks = extract_hooks(prospect_data, generate_with_llm, llm_config)
    
    # Step 6: Context & Learning
    print("\n[STEP 6/8] Context & Learning")
    
    
    company_name = prospect_data.get('company')
    same_company_prospects = find_same_company_prospects(company_name, client_id)
    
    company_context = reuse_company_insights(
        company_name, 
        same_company_prospects, 
        client_id
    )
    
    reference = build_company_reference(same_company_prospects)
    
    # Step 7: Generate content for selected channels
    print("\n[STEP 7/8] Content Generation & Optimization")
    
    
    generated_outputs = {}
    
    for channel in user_inputs['selected_channels']:
        try:
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
                print(f"[CRITIC] Optimizing {channel.upper()}...")
                optimized_content = apply_critic_pass(
                    content,
                    channel,
                    prospect_data,
                    persona,
                    llm_config,
                    generate_with_llm
                )
                generated_outputs[channel] = optimized_content
            else:
                generated_outputs[channel] = None
            
        except Exception as e:
            print(f"Error generating {channel} content: {str(e)}")
            generated_outputs[channel] = None
    
    # Step 8: Validate and display results
    print("\n[STEP 8/8] Validation & Output")
    
    
    # Display each channel's output
    for channel, content in generated_outputs.items():
        if content:
            display_channel_output(channel, content, prospect_data)
    
    # Regeneration loop
    while True:
        print("OPTIONS:")
        print("  1. Regenerate specific channel")
        print("  2. Save and finish")
        print("  3. Exit without saving")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            # Regeneration
            channel_to_regen = select_channel_for_regeneration(user_inputs['selected_channels'])
            
            if channel_to_regen and channel_to_regen in generated_outputs:
                modifications = input("\nWhat changes do you want? (be specific): ").strip()
                
                if modifications:
                    regenerated = regenerate_content(
                        generated_outputs[channel_to_regen],
                        modifications,
                        channel_to_regen,
                        llm_config,
                        generate_with_llm
                    )
                    
                    # Validate regenerated content
                    privacy_ok = validate_privacy(regenerated, prospect_data)
                    ethics_ok = validate_ethics_and_display(regenerated)
                    
                    if privacy_ok and ethics_ok:
                        generated_outputs[channel_to_regen] = regenerated
                        display_channel_output(channel_to_regen, regenerated, prospect_data)
                    else:
                        print("\nRegenerated content has issues. Keeping original.")
        
        elif choice == '2':
            # Save and finish
            print("\n[STORAGE] Saving results...")
            save_prospect(prospect_data, generated_outputs, client_id)
            
            # Save company insights for future reuse
            save_company_insights(company_name, company_context, prospect_data, client_id)
            
            print("\nOUTREACH GENERATION COMPLETE!")
            print(f"\nEngagement Score: {engagement_score}/100")
            print(f"Channels Generated: {', '.join(user_inputs['selected_channels'])}")
            print(f"Client ID: {client_id}")
            print("\nResults saved successfully!")
            break
        
        elif choice == '3':
            print("\nExiting without saving...")
            break


def display_channel_output(channel, content, prospect_data):
    """Display output for a specific channel with validation and clear formatting"""
    
    # Header with clear separator
    print("\n")
    print("=" * 80)
    print(f"{channel.upper()}:")
    print("=" * 80)
    
    # Validation
    print("\n[VALIDATION] Checking privacy...")
    privacy_ok = validate_privacy(content, prospect_data)
    if privacy_ok:
        print("Privacy check passed")
    
    print("\n[VALIDATION] Checking ethics...")
    ethics_ok = validate_ethics_and_display(content)
    if ethics_ok:
        print("Ethics check passed")
    
    if privacy_ok and ethics_ok:
        print("\nAll validation checks passed")
    else:
        print("\nSome validation issues found (see above)")
    
    # Content with separator
    print("\n" + "-" * 80)
    print(content)
    print("-" * 80)
    
    # Metadata
    print(f"\nLength: {len(content)} characters")
    print("=" * 80)


def select_channel_for_regeneration(available_channels):
    """Let user select which channel to regenerate"""
    print("\nSelect channel to regenerate:")
    for i, channel in enumerate(available_channels, 1):
        print(f"  {i}. {channel}")
    
    choice = input("\nEnter channel number: ").strip()
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(available_channels):
            return available_channels[idx]
    except:
        pass
    
    return None


if __name__ == "__main__":
    try:
        run_outreach_engine()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()
