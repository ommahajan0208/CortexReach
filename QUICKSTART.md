# Quick Start Guide

## Prerequisites Setup

### 1. Install Ollama

```powershell
# Download from https://ollama.ai/download/windows
# Run the installer.
# Ollama will start automatically.
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

### 3. Verify Ollama Is Running

```bash
# Test the API
curl http://localhost:11434/api/tags
```

## Installation

### 1. Navigate to the Project Directory

```bash
cd CortexReach
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Quick Test with Fake Data (Recommended First Run)

```bash
python main_enhanced.py
```

Choose **Option 1 (Fake Data Mode)** for instant testing:
- No scraping required
- 10 pre-loaded comprehensive prospects
- Tests all features immediately
- Perfect for demonstrations

Select any prospect ID (or type 'random') and channels to see **elite-quality output**.

### Full Production Mode

```bash
python main.py
```

For live scraping with real prospect data.

## First Run Walkthrough

### 1. Welcome Screen
- Review the banner and prerequisites information.
- Press Enter to continue.

### 2. Client Setup
- Choose to create a new client or use an existing one.
- A unique client ID will be generated.

### 3. LLM Configuration
- The system will verify that Ollama is running.
- Select or confirm the model (default: llama2).
- Choose the output language (default: English).

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

Example: 1,4 (for Email + LinkedIn DM)
```

### 7. Wait for Processing
The system will proceed through the following stages:
- [1/8] Client setup - Complete
- [2/8] LLM configuration - Complete
- [3/8] Input collection - Complete
- [4/8] Data scraping - Complete
- [5/8] Persona analysis - Complete
- [6/8] Context check - Complete
- [7/8] Content generation - Complete
- [8/8] Validation and display - Complete

### 8. Review Output
- Each channel's content is displayed.
- Privacy and ethics validation results are shown.
- Content length and characteristics are listed.

### 9. Options
```
1. Regenerate specific channel
2. Save and finish
3. Exit without saving
```

**To regenerate:**
- Select option 1.
- Choose which channel to regenerate.
- Describe the desired changes. For example:
  - "Make it shorter and more casual."
  - "Add more detail about their GitHub projects."
  - "Remove the reference to a past contact."

### 10. Save
- Select option 2 to save.
- All data is stored in the `data/{client_id}/` directory.
- Company insights are saved for future reuse.

## Tips for Best Results

### 1. Elite Output Quality (NEW)
- **High-signal hooks** - System prioritizes business-relevant observations (role changes, scaling, launches)
- **Sharp positioning** - Industry insider tone, not bland/polite
- **No hallucinations** - Only data-supported insights, no inferred pain points
- **Deliverability protection** - Avoids spam trigger words
- **Pattern interrupts** - Persona-specific openings that break through noise

### 2. Provide More Data
- More input sources lead to better personalization.
- Include recent activity when available.
- Mention specific projects or interests.

### 2. Use GitHub for Technical Prospects
- Automatically extracts programming languages and projects.
- No authentication is required.
- Well-suited for developer outreach.

### 3. Company Website Scraping
- Provides company context automatically.
- Detects the technology stack.
- Infers industry classification.

### 4. Leverage Company Context
- A second contact from the same company benefits from richer context.
- Natural references to previous contacts are generated.
- Intelligence is accumulated over time.

### 5. Iterate with Regeneration
- Do not settle for the first output.
- Use specific modification requests.
- Tone and personalization are preserved across regenerations.
