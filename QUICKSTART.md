# Quick Start Guide

## Prerequisites Setup

### 1. Install Ollama

```powershell
# Download from https://ollama.ai/download/windows
# Run the installer.
# Ollama will start automatically.
```

### 2. Pull llama3 Model (Required)

```bash
# This is the auto-configured model
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

### 2. Create Virtual Environment (Recommended)

```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
# Installs: requests, beautifulsoup4, lxml, rich (for beautiful UI)
```

## Running the Application

### 🎉 Main Application (Beautiful Rich TUI)

```bash
python main_enhanced.py
```

**Features:**
- 🎨 Beautiful terminal UI with Rich library
- 📊 Color-coded workflow steps (1/8, 2/8, etc.)
- 🔄 Progress bars with spinners during generation
- 📋 Elegant tables for personalization hooks
- ✨ Professional formatting for hackathon demos

**Test Data:**
- 10 comprehensive fake prospects (no scraping needed)
- 4 persona types: Technical, Executive, Founders, Researchers
- Multiple prospects from same companies (tests context reuse)
- All data sources covered (LinkedIn, Website, X, GitHub)

**Auto-Configured:**
- Model: llama3 (no selection needed)
- Language: English (no selection needed)
- Streamlined workflow for faster demos

Select any prospect ID (or type 'random') and channels to see **elite-quality output**.

## First Run Walkthrough

### 1. Welcome Screen (Rich Banner)
- Beautiful cyan banner with project info
- Color-coded prerequisite checks (✓ green for success)
- Press Enter to continue

### 2. Client Setup (Rich Panel)
- Create new client or select existing
- Unique client ID generated automatically
- Visual confirmation with colors

### 3. Prospect Selection (No Configuration Needed!)
- **Model:** llama3 (auto-selected)
- **Language:** English (auto-selected)
- Choose prospect from list of 10 test prospects
- Or type 'random' for surprise selection

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
