# CortexReach - Offline LLM-Powered Hyper-Personalized Cold Outreach Engine

A beautiful terminal-based tool with Rich TUI that generates hyper-personalized cold outreach messages across multiple channels using offline LLMs and intelligent data analysis.

## Key Features

### 🎨 Beautiful Terminal UI (NEW!)
- **Rich Console** - Color-coded workflow steps with progress bars
- **Elegant Tables** - Beautiful bordered tables for hooks and data
- **Visual Feedback** - Spinners, panels, and professional formatting
- **Hackathon Ready** - Impressive visual presentation

### 📊 Comprehensive Test Data
- **10 Fake Prospects** - Pre-loaded diverse test data (no scraping needed)
- **4 Persona Types** - Technical, Executive, Founders, Researchers
- **Multi-Company** - Tests context reuse with same-company prospects
- **Complete Coverage** - All data sources (LinkedIn, Website, X, GitHub)

### 🧠 Intelligent Analysis
- **Persona Analysis** - Understand communication style and preferences
- **Elite Hook Extraction** - High-signal business hooks with visual table display
- **Company Context** - Reuse insights from previous outreach to the same company
- **ICP Filtering** - Warns when prospect doesn't match product target audience
- **Anti-Hallucination Protection** - No inferred pain points, data-supported only

### 📨 Multi-Channel Output (Elite Quality)
Generate unique, platform-optimized content with:
- **Email** - Sharp insider tone, pattern interrupt (150-200 words) - NO emojis
- **WhatsApp** - Confident conversational (300-400 characters) - 1-2 emojis allowed
- **SMS** - Pattern interrupt, ultra-concise (max 160 characters) - 1-2 emojis allowed
- **LinkedIn DM** - Business-focused professional (200-250 words) - NO emojis
- **Instagram DM** - Confident casual (150-200 words) - 2-3 emojis allowed

**Output Quality Features:**
- ✓ High-signal business hooks (no hobbies/fluff)
- ✓ Sharp positioning (insider voice, not polite)
- ✓ No inferred pain points (data-supported or curiosity-driven)
- ✓ Enhanced cleanup (removes meta-commentary, placeholders)
- ✓ Deliverability protection (spam trigger avoidance)
- ✓ Persona-adaptive pattern interrupts
- ✓ Channel-specific emoji rules (professional vs casual)

### 🔒 Privacy and Ethics
- Privacy validation to prevent sensitive data leaks
- Ethics checking to avoid manipulative language
- Content regeneration with modifications
- Beautiful validation result display

### 🎯 Smart Learning & Auto-Configuration
- **Client-based storage** - Track all outreach by client
- **Company insights reuse** - Leverage previous research
- **Natural referencing** - Optionally mention past contacts
- **Auto-configured** - llama3 model + English language (no prompts)
- **Streamlined UX** - Removed unnecessary configuration steps

## Architecture

```
CortexReach/
├── main_enhanced.py             # Entry point (Rich TUI)
├── enhanced_runner.py           # Workflow orchestrator (Rich UI)
├── enhanced_prospect_loader.py  # Fake data loader
├── fake_data_loader.py          # 10 comprehensive test prospects
├── test_fake_data.py            # Test suite for fake data
├── PROJECT_SUMMARY.py           # Project overview
├── requirements.txt             # Python dependencies (includes rich>=13.7.0)
├── QUICKSTART.md                # Quick start guide
├── README.md                    # Full documentation
├── FAKE_DATA_DOCS.md            # Fake data documentation
├── IMPLEMENTATION_SUMMARY.md    # Implementation details
├── QUICK_REFERENCE.txt          # Quick reference cheat sheet
├── LICENSE                      # Apache 2.0 License
├── config/
│   ├── __init__.py
│   └── prompts.py              # Channel-specific LLM prompts (emoji rules)
├── layers/
│   ├── __init__.py
│   ├── input_layer/            # Data collection (fake data)
│   │   ├── prospect_loader.py  # Menu and input orchestration
│   │   ├── linkedin_scraper.py # LinkedIn data (fake)
│   │   ├── website_scraper.py  # Website data (fake)
│   │   ├── x_scraper.py       # X/Twitter data (fake)
│   │   └── github_scraper.py  # GitHub data (fake)
│   ├── analysis_layer/         # Intelligence analysis
│   │   ├── persona_analyzer.py # Communication style analysis
│   │   └── hook_extractor.py  # Personalization hooks + Rich table display
│   ├── visualization_layer/    # Rich TUI components (NEW!)
│   │   ├── __init__.py
│   │   └── console_manager.py # Rich console utilities
│   ├── context_layer/          # Learning and reuse
│   │   ├── company_matcher.py  # Same-company prospect matching
│   │   ├── insight_reuser.py  # Company knowledge reuse
│   │   └── reference_builder.py# Natural referencing
│   ├── generation_layer/       # Content creation
│   │   ├── llm_config.py      # Model and language configuration
│   │   ├── llm_interface.py   # LLM communication and generation
│   │   ├── product_config.py  # Product configuration
│   │   └── regenerator.py     # Output modification
│   ├── optimization_layer/     # Content optimization
│   │   └── critic_optimizer.py # Automatic critic pass
│   ├── validation_layer/       # Privacy and ethics
│   │   ├── privacy_checker.py # Prevent data leaks
│   │   └── ethics_validator.py# Check for manipulation
│   └── storage_layer/          # Data persistence
│       ├── client_manager.py  # Client ID management
│       └── json_storage.py    # Save/load prospect data
└── data/                       # Client data storage
```

## Quick Start

### Prerequisites

1. **Install Python 3.12** (Avoid 3.13+)

2. **Install Ollama** (Offline LLM)
   ```bash
   # Visit https://ollama.ai and install for your operating system

   # Pull llama3 (required - auto-configured):
   ollama pull llama3
   ```

3. **Start Ollama**
   ```bash
   # Ollama should start automatically after installation.
   ```

### Installation

1. **Clone or download the project**
   ```bash
   cd CortexReach
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   # OR
   source venv/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Includes: requests, beautifulsoup4, lxml, rich
   ```

### Run

```bash
python main_enhanced.py
```

**Features:**
- Beautiful Rich TUI with color-coded output
- 10 comprehensive test prospects (no scraping needed)
- Auto-configured (llama3 + English)
- Instant testing and demonstrations

## Usage Guide

### Step-by-Step Workflow

1. **Client Selection** (Beautiful Rich Panel)
   - Choose an existing client or create a new one
   - Each client receives isolated data storage

2. **LLM Configuration** (Auto-Configured)
   - Model: llama3 (auto-selected)
   - Language: English (auto-selected)
   - No prompts needed!

3. **Prospect Selection** (Fake Data Mode)
   - Choose from 10 comprehensive test prospects
   - Or type 'random' for surprise selection
   - Select output channels (Email, WhatsApp, SMS, LinkedIn, Instagram)

4. **Data Display** (Beautiful Prospect Card)
   - Visual display of prospect profile
   - Company, role, and persona information
   - Manual input for authenticated platforms.
   - Data merging from all sources.

5. **Analysis**
   - Persona analysis.
   - Engagement score calculation.
   - Personalization hook extraction.

6. **Context and Learning**
   - Check for previous contacts at the same company.
   - Reuse company insights from prior outreach.
   - Build natural references.

7. **Content Generation**
   - Generate content for each selected channel.
   - Apply channel-specific formatting and tone.

8. **Validation and Review**
   - Privacy check.
   - Ethics validation.
   - Content display.

9. **Regeneration (Optional)**
   - Modify specific channels.
   - Specify desired changes.
   - Regenerate while preserving tone.

10. **Save**
    - Store prospect data.
    - Save company insights for reuse.

## Differentiating Factors

1. **Elite-level personalization**
   - Goes beyond simple name/company insertion.
   - High-signal business hook extraction (role changes, scaling, launches).
   - Sharp insider positioning (not bland/polite).
   - Platform-specific optimization.
   - Anti-hallucination protection (no inferred pain points).

2. **Company context reuse**
   - Learns from previous outreach to the same company.
   - Natural referencing to past contacts.
   - Cumulative intelligence.

3. **Engagement prediction**
   - Data quality scoring.
   - Response likelihood prediction.
   - Helps prioritize outreach efforts.

4. **Privacy-first design**
   - All processing is performed locally.
   - No data is sent to external APIs.
   - Full control over your data.

5. **Iterative refinement**
   - Regenerate with specific modifications.
   - Preserve tone while making changes.
   - Rapid iteration workflow.

## Configuration

### Supported Languages

- English (default)
- Spanish
- French
- German
- Any language supported by the configured LLM

### Recommended Models

| Model   | Speed  | Quality | Use Case                |
|---------|--------|---------|-------------------------|
| llama2  | Fast   | Good    | Testing, high volume    |
| mistral | Medium | Better  | Production use          |
| llama3  | Slow   | Best    | Premium outreach        |

### Channel Specifications

| Channel   | Length          | Tone                | Special Features       |
|-----------|----------------|---------------------|------------------------|
| Email     | 150-200 words  | Professional        | Subject line included  |
| WhatsApp  | 300-400 chars  | Conversational      | Informal tone          |
| SMS       | Max 160 chars  | Ultra-concise       | Direct call-to-action  |
| LinkedIn  | 200-250 words  | Professional-casual | Platform-native        |
| Instagram | 150-200 words  | Casual              | Authentic, friendly    |

## Data Storage

Data is organized by client:

```
data/
└── client_20260201_143022_a1b2c3d4/
    ├── prospects.json          # All prospects
    └── company_insights.json   # Reusable insights
```

### Prospect Data Structure

```json
{
  "prospect_data": {
    "name": "Jane Smith",
    "company": "TechCorp",
    "role": "VP Engineering"
  },
  "generated_outputs": {
    "email": "...",
    "linkedin": "..."
  },
  "timestamp": "2026-02-01T14:30:22"
}
```

## Troubleshooting

### Ollama Connection Issues

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama (refer to platform-specific documentation)
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Slow Generation

- Use a faster model (llama2 instead of llama3).
- Reduce max_tokens in llm_interface.py.
- Ensure Ollama has sufficient system resources.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.
