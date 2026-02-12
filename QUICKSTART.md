# 🚀 Quick Start Guide

## Prerequisites Setup

### 1. Install Ollama

**Windows:**
```powershell
# Download from https://ollama.ai/download/windows
# Run the installer
# Ollama will start automatically
```

**Mac:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Pull an LLM Model

```bash
# Recommended for testing (fast)
ollama pull llama2

# Recommended for production (better quality)
ollama pull mistral

# Best quality (slower)
ollama pull llama3
```

### 3. Verify Ollama is Running

```bash
# Test the API
curl http://localhost:11434/api/tags
```

## Installation

### 1. Navigate to Project

```bash
cd omanu
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Engine

```bash
python main.py
```

## First Run Walkthrough

### 1. Welcome Screen
- Read the banner and prerequisites
- Press Enter to continue

### 2. Client Setup
- Choose to create a new client or use existing
- A unique client ID will be generated

### 3. LLM Configuration
- System checks if Ollama is running
- Select or confirm the model (default: llama2)
- Choose output language (default: English)

### 4. Input Selection
```
Available input sources:
  1. LinkedIn URL
  2. Company Website URL
  3. Twitter/X URL
  4. GitHub URL

Example: 1,2,4 (for LinkedIn + Website + GitHub)
```

### 5. Provide URLs
```
LinkedIn URL: https://linkedin.com/in/johndoe
Company Website URL: https://example.com
GitHub URL: https://github.com/johndoe
```

**Note:** LinkedIn and Twitter require manual data entry due to authentication requirements.

### 6. Select Output Channels
```
Available channels:
  1. Email
  2. WhatsApp
  3. SMS
  4. LinkedIn DM
  5. Instagram DM

Example: 1,4 (for Email + LinkedIn)
```

### 7. Wait for Processing
The system will:
- [1/8] Setup client ✓
- [2/8] Configure LLM ✓
- [3/8] Collect inputs ✓
- [4/8] Scrape data ✓
- [5/8] Analyze persona ✓
- [6/8] Check context ✓
- [7/8] Generate content ✓
- [8/8] Validate & display ✓

### 8. Review Output
- Each channel's content is displayed
- Privacy and ethics validation results shown
- Content length and characteristics listed

### 9. Options
```
1. Regenerate specific channel
2. Save and finish
3. Exit without saving
```

**To regenerate:**
- Select option 1
- Choose which channel
- Describe your desired changes
  - Example: "Make it shorter and more casual"
  - Example: "Add more about their GitHub projects"
  - Example: "Remove the reference to past contact"

### 10. Save
- Select option 2 to save
- All data stored in `data/{client_id}/`
- Company insights saved for future reuse

## Example Session

```
# Input
Sources: LinkedIn + GitHub
Channels: Email + LinkedIn DM

LinkedIn: https://linkedin.com/in/jane-tech
GitHub: https://github.com/janetech

# Manual entry for LinkedIn
Name: Jane Smith
Role: Senior Developer
Company: TechCorp
Skills: Python, React, AWS

# Output
✅ Generated Email (182 words)
✅ Generated LinkedIn DM (215 words)
📊 Engagement Score: 75/100

# Review, regenerate if needed, then save
```

## Tips for Best Results

### 1. Provide More Data
- More input sources = better personalization
- Include recent activity when available
- Mention specific projects or interests

### 2. Use GitHub for Technical Prospects
- Automatically extracts languages and projects
- No authentication required
- Great for developer outreach

### 3. Company Website Scraping
- Provides company context automatically
- Detects tech stack
- Infers industry

### 4. Leverage Company Context
- Second person from same company gets better context
- Natural references to previous contacts
- Cumulative intelligence

### 5. Iterate with Regeneration
- Don't settle for first output
- Use specific modification requests
- Tone and personalization are preserved

## Common Issues

### "Ollama not running"
```bash
# Windows: Open Ollama app from Start menu
# Mac/Linux: ollama serve
```

### "Model not found"
```bash
ollama pull llama2
# or whichever model you want to use
```

### Slow generation
- Use llama2 instead of llama3
- Ollama needs adequate RAM (8GB+ recommended)
- Close other applications

### Import errors
```bash
pip install -r requirements.txt --force-reinstall
```

## Next Steps

1. **Try different models**
   - Compare llama2 vs mistral vs llama3
   - Find the right speed/quality balance

2. **Experiment with channels**
   - See how each channel adapts content
   - Notice tone and length differences

3. **Build company context**
   - Contact multiple people from same company
   - Watch how insights accumulate

4. **Test languages**
   - Try Spanish, French, German
   - LLM adapts content naturally

5. **Refine with regeneration**
   - Practice giving modification instructions
   - Learn what works best

## Support

For issues or questions:
- Check README.md for detailed documentation
- Review architecture in code comments
- Examine prompts in config/prompts.py

---

**Happy outreaching! 🚀**
