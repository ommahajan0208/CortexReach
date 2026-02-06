# 🚀 Offline LLM-Powered Hyper-Personalized Cold Outreach Engine

A terminal-based tool that generates hyper-personalized cold outreach messages across multiple channels using offline LLMs and intelligent data analysis.

## ✨ Key Features

### Multi-Source Data Collection
- **LinkedIn** - Extract professional profile data
- **Company Website** - Scrape company information and tech stack
- **Twitter/X** - Gather social insights and interests
- **GitHub** - Analyze technical projects and contributions

### Intelligent Analysis
- **Persona Analysis** - Understand communication style and preferences
- **Engagement Scoring** - Predict likelihood of response (0-100)
- **Hook Extraction** - Identify personalization opportunities
- **Company Context** - Reuse insights from previous outreach to same company

### Multi-Channel Output
Generate unique, platform-optimized content for:
- **Email** - Professional, structured (150-200 words)
- **WhatsApp** - Conversational, brief (~300-400 chars)
- **SMS** - Ultra-short, punchy (max 160 chars)
- **LinkedIn DM** - Professional-casual (~200-250 words)
- **Instagram DM** - Casual, friendly (~150-200 words)

### Privacy & Ethics
- Privacy validation (no sensitive data leaks)
- Ethics checking (no manipulative language)
- Content regeneration with modifications

### Smart Learning
- **Client-based storage** - Track all outreach by client
- **Company insights reuse** - Leverage previous research
- **Natural referencing** - Optionally mention past contacts

## 🏗️ Architecture

```
omanu/
├── main.py                      # Entry point
├── runner.py                    # Workflow orchestrator
├── config/
│   └── prompts.py              # Channel-specific LLM prompts
├── layers/
│   ├── input_layer/            # Data collection
│   ├── analysis_layer/         # Intelligence & scoring
│   ├── context_layer/          # Learning & reuse
│   ├── generation_layer/       # Content creation
│   ├── validation_layer/       # Privacy & ethics
│   └── storage_layer/          # Data persistence
└── data/                       # Client data storage
```

## 🚀 Quick Start

### Prerequisites

1. **Install Python 3.8+**

2. **Install Ollama** (Offline LLM)
   ```bash
   # Visit https://ollama.ai and install for your OS
   
   # Pull a model (choose one):
   ollama pull llama2        # Fast, good quality
   ollama pull mistral       # Better quality
   ollama pull llama3        # Best quality, slower
   ```

3. **Start Ollama**
   ```bash
   # Ollama should start automatically
   # Or start manually (check Ollama docs for your OS)
   ```

### Installation

1. **Clone/Download the project**
   ```bash
   cd omanu
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Run

```bash
python main.py
```

## 📖 Usage Guide

### Step-by-Step Workflow

1. **Client Selection**
   - Choose existing client or create new
   - Each client gets isolated data storage

2. **LLM Configuration**
   - Select model (llama2, mistral, llama3, etc.)
   - Choose language (English, Spanish, French, etc.)

3. **Input Selection**
   - Select data sources (LinkedIn, Website, X, GitHub)
   - Provide URLs for selected sources
   - Select output channels (Email, WhatsApp, etc.)

4. **Data Collection**
   - Automatic scraping (where possible)
   - Manual input for authenticated platforms
   - Data merging from all sources

5. **Analysis**
   - Persona analysis
   - Engagement score calculation
   - Personalization hook extraction

6. **Context & Learning**
   - Check for previous contacts at same company
   - Reuse company insights
   - Build natural references

7. **Content Generation**
   - Generate content for each selected channel
   - Channel-specific formatting and tone

8. **Validation & Review**
   - Privacy check
   - Ethics validation
   - Content display

9. **Regeneration (Optional)**
   - Modify specific channels
   - Specify desired changes
   - Regenerate while preserving tone

10. **Save**
    - Store prospect data
    - Save company insights for reuse

### Example Session

```
# User selects:
- Input: LinkedIn + Company Website
- Channels: Email + LinkedIn DM
- Provides URLs

# System:
[1/8] Client Management ✓
[2/8] LLM Configuration ✓
[3/8] Input Collection ✓
[4/8] Data Collection ✓
[5/8] Prospect Analysis ✓
[6/8] Context & Learning ✓
[7/8] Content Generation ✓
[8/8] Validation & Output ✓

# Displays generated content for review
# User can regenerate with modifications
# Finally saves everything
```

## 🎯 Creative Approaches

### What Makes This Different

1. **Multi-dimensional personalization**
   - Not just name/company insertion
   - Deep analysis of persona and context
   - Platform-specific optimization

2. **Company context reuse**
   - Learn from previous outreach to same company
   - Natural referencing to past contacts
   - Cumulative intelligence

3. **Engagement prediction**
   - Data quality scoring
   - Response likelihood prediction
   - Helps prioritize outreach

4. **Privacy-first design**
   - All processing happens locally
   - No data sent to external APIs
   - Full control over your data

5. **Iterative refinement**
   - Regenerate with specific modifications
   - Preserve tone while making changes
   - Quick iteration workflow

## 🔧 Configuration

### Supported Languages

- English (default)
- Spanish
- French
- German
- Any language your LLM supports

### Recommended Models

| Model | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| llama2 | Fast | Good | Testing, high volume |
| mistral | Medium | Better | Production use |
| llama3 | Slow | Best | Premium outreach |

### Channel Specifications

| Channel | Length | Tone | Special Features |
|---------|--------|------|------------------|
| Email | 150-200 words | Professional | Subject line included |
| WhatsApp | 300-400 chars | Conversational | Emoji-friendly |
| SMS | Max 160 chars | Ultra-concise | Punchy CTAs |
| LinkedIn | 200-250 words | Professional-casual | Platform-native |
| Instagram | 150-200 words | Casual | Authentic, friendly |

## 📊 Data Storage

Data is organized by client:

```
data/
└── client_20240201_143022_a1b2c3d4/
    ├── prospects.json          # All prospects
    └── company_insights.json   # Reusable insights
```

### Prospect Data Structure

```json
{
  "prospect_data": {
    "name": "Jane Smith",
    "company": "TechCorp",
    "role": "VP Engineering",
    ...
  },
  "generated_outputs": {
    "email": "...",
    "linkedin": "..."
  },
  "timestamp": "2024-02-01T14:30:22"
}
```

## 🛠️ Troubleshooting

### Ollama Connection Issues

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama (OS-specific)
# Check Ollama documentation
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Slow Generation

- Use a faster model (llama2 instead of llama3)
- Reduce max_tokens in llm_interface.py
- Ensure Ollama has sufficient resources

## 🚧 Future Enhancements

- [ ] Advanced web scraping (Selenium/Playwright)
- [ ] Email sending integration
- [ ] Response tracking and analytics
- [ ] A/B testing framework
- [ ] Fine-tuning on successful outreach
- [ ] CRM integration
- [ ] Batch processing
- [ ] Web UI (Gradio/Streamlit)

## 📝 License

Apache 2.0 License 