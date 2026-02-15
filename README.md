# CortexReach - Offline LLM-Powered Hyper-Personalized Cold Outreach Engine

A terminal-based tool that generates hyper-personalized cold outreach messages across multiple channels using offline LLMs and intelligent data analysis.

## Key Features

### Multi-Source Data Collection
- **LinkedIn** - Extract professional profile data
- **Company Website** - Scrape company information and technology stack
- **Twitter/X** - Gather social insights and interests
- **GitHub** - Analyze technical projects and contributions

### Intelligent Analysis
- **Persona Analysis** - Understand communication style and preferences
- **Engagement Scoring** - Predict likelihood of response (0-100)
- **Elite Hook Extraction** - High-signal business hooks (role changes, scaling, launches)
- **Company Context** - Reuse insights from previous outreach to the same company
- **Anti-Hallucination Protection** - No inferred pain points, data-supported only

### Multi-Channel Output (Elite Quality)
Generate unique, platform-optimized content with:
- **Email** - Sharp insider tone, pattern interrupt (150-200 words)
- **WhatsApp** - Confident conversational (approximately 300-400 characters)
- **SMS** - Pattern interrupt, ultra-concise (maximum 160 characters)
- **LinkedIn DM** - Business-focused professional (approximately 200-250 words)
- **Instagram DM** - Confident casual (approximately 150-200 words)

**Output Quality Features:**
- ✓ High-signal business hooks (no hobbies/fluff)
- ✓ Sharp positioning (insider voice, not polite)
- ✓ No inferred pain points (data-supported or curiosity-driven)
- ✓ Deliverability protection (spam trigger avoidance)
- ✓ Persona-adaptive pattern interrupts

### Privacy and Ethics
- Privacy validation to prevent sensitive data leaks
- Ethics checking to avoid manipulative language
- Content regeneration with modifications

### Smart Learning
- **Client-based storage** - Track all outreach by client
- **Company insights reuse** - Leverage previous research
- **Natural referencing** - Optionally mention past contacts

## Architecture

```
CortexReach/
├── main.py                      # Entry point
├── runner.py                    # Workflow orchestrator
├── PROJECT_SUMMARY.py           # Project overview and documentation
├── requirements.txt             # Python dependencies
├── QUICKSTART.md                # Quick start guide
├── README.md                    # Full documentation
├── LICENSE                      # Apache 2.0 License
├── .gitignore                   # Git ignore rules
├── config/
│   ├── __init__.py
│   └── prompts.py              # Channel-specific LLM prompts
├── layers/
│   ├── __init__.py
│   ├── input_layer/            # Data collection
│   │   ├── prospect_loader.py  # Menu and input orchestration
│   │   ├── linkedin_scraper.py # LinkedIn data collection
│   │   ├── website_scraper.py  # Company website scraping
│   │   ├── x_scraper.py       # Twitter/X data collection
│   │   └── github_scraper.py  # GitHub profile analysis
│   ├── analysis_layer/         # Intelligence and scoring
│   │   ├── persona_analyzer.py # Communication style analysis
│   │   ├── engagement_scorer.py# Response likelihood prediction
│   │   └── hook_extractor.py  # Personalization opportunities
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

1. **Install Python 3.12 Avoid 3.13+**

2. **Install Ollama** (Offline LLM)
   ```bash
   # Visit https://ollama.ai and install for your operating system

   # Pull a model (choose one):
   ollama pull llama2        # Fast- good quality
   ollama pull mistral       # Better quality
   ollama pull llama3        # Best quality, slower
   ```

3. **Start Ollama**
   ```bash
   # Ollama should start automatically after installation.
   # Refer to the Ollama documentation for platform-specific instructions.
   ```

### Installation

1. **Clone or download the project**
   ```bash
   cd CortexReach
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Run

```bash
python main.py
```

## Usage Guide

### Step-by-Step Workflow

1. **Client Selection**
   - Choose an existing client or create a new one.
   - Each client receives isolated data storage.

2. **LLM Configuration**
   - Select a model (llama2, mistral, llama3, etc.).
   - Choose a language (English, Spanish, French, etc.).

3. **Input Selection**
   - Select data sources (LinkedIn, Website, X, GitHub).
   - Provide URLs for each selected source.
   - Select output channels (Email, WhatsApp, etc.).

4. **Data Collection**
   - Automatic scraping where applicable.
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
