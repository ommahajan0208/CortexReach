"""
Regenerator - Regenerate content with user modifications
"""

from config.prompts import get_regeneration_prompt, get_channel_requirements
from layers.generation_layer.llm_interface import clean_llm_output


def regenerate_content(original_content, user_modifications, channel, config, llm_generate_func):
    """
    Regenerate content with user's requested modifications
    
    Args:
        original_content: str - original generated content
        user_modifications: str - what user wants changed
        channel: str - channel name
        config: dict - LLM configuration
        llm_generate_func: function - LLM generation function
    
    Returns:
        str: regenerated content
    """
    print(f"\n[REGENERATION] Regenerating {channel.upper()} content...")
    print(f"   Modifications: {user_modifications[:100]}...")
    
    # Get regeneration prompt
    prompt_template = get_regeneration_prompt()
    channel_reqs = get_channel_requirements(channel)
    
    # Build prompt
    prompt = prompt_template.format(
        channel=channel,
        original_content=original_content,
        user_modifications=user_modifications,
        channel_requirements=channel_reqs,
        language=config['language']
    )
    
    # Generate
    try:
        regenerated = llm_generate_func(prompt, config)
        
        # Clean up any meta-commentary
        regenerated = clean_llm_output(regenerated)
        
        print(f"Content regenerated successfully")
        return regenerated
    except Exception as e:
        print(f"Error regenerating content: {str(e)}")
        return original_content  # Return original if regeneration fails
