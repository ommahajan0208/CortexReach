# Fake Data Feature - Documentation

## Overview

The CortexReach system now supports **dual modes** of operation:
1. **FAKE DATA MODE** - Pre-loaded comprehensive test data
2. **LIVE SCRAPING MODE** - Real-time data collection (original functionality)

This enhancement makes testing, demonstrations, and development much easier while preserving full production capabilities.

## Why Fake Data?

### Benefits

✅ **Instant Testing** - No need to scrape real websites or accounts  
✅ **Comprehensive Coverage** - Data designed to test ALL features  
✅ **Reproducible** - Same data every time for consistent testing  
✅ **No Dependencies** - Works offline, no authentication needed  
✅ **Safe** - No risk of rate limiting or blocking  
✅ **Educational** - Perfect for demonstrations and learning  

### Use Cases

- **Development** - Test new features quickly
- **Demonstrations** - Show system capabilities
- **Training** - Teach others how to use the system
- **Debugging** - Isolate issues with known data
- **Feature Testing** - Verify all features work correctly

## Fake Prospect Database

### 10 Comprehensive Prospects

#### Technical Professionals (3)
1. **Sarah Chen** - Senior Software Engineer at TechCorp AI
   - Python, Kubernetes, TensorFlow expertise
   - 3 GitHub projects (847+ stars)
   - Active open source contributor
   - Blog posts and conference talks

2. **Marcus Johnson** - Lead Backend Engineer at TechCorp AI
   - Node.js, GraphQL, API architecture
   - 3 GitHub projects (512+ stars)
   - Performance optimization focus
   - Microservices expert

3. **Priya Sharma** - DevOps Engineer at CloudScale Systems
   - Terraform, AWS, Infrastructure as Code
   - 3 GitHub projects (1234+ stars)
   - CI/CD and automation specialist
   - Very active contributor

#### Executives (2)
4. **David Thompson** - VP of Engineering at FinTech Innovations
   - Engineering leadership (85 person team)
   - Published in Harvard Business Review
   - Conference speaker
   - No GitHub (realistic for executive)

5. **Lisa Martinez** - CTO at HealthTech Solutions
   - Healthcare technology strategy
   - Led Series C fundraising ($50M)
   - Forbes 40 under 40
   - Former Amazon Health VP

#### Founders/Entrepreneurs (3)
6. **Alex Rivera** - Founder & CEO at EcoTrack
   - Y Combinator W23
   - Climate tech startup
   - Seed round: $3M
   - 2 GitHub projects (SDK and data)

7. **James Kim** - Co-Founder & CTO at EcoTrack
   - Ex-Stripe engineer
   - MIT CS graduate
   - 3 GitHub projects (789+ stars)
   - Very active (423 contributions/year)

8. **Nina Patel** - Founder & CEO at EduAI
   - Education technology
   - 100,000+ students on platform
   - Series A: $8M (a16z)
   - Former teacher turned founder

#### Researchers/Academics (2)
9. **Dr. Emily Watson** - Research Scientist at QuantumTech Labs
   - Quantum computing PhD (Stanford)
   - 20+ publications in Nature
   - Quantum ML and chemistry focus
   - 3 GitHub projects (research tools)

10. **Dr. Michael Chang** - Senior Research Engineer at QuantumTech Labs
    - Quantum software infrastructure
    - MIT PhD in compiler design
    - 3 GitHub projects (compiler tools)
    - Active in quantum software community

### Company Grouping (Tests Context Reuse)

Multiple prospects from the same companies to test company context reuse:

- **TechCorp AI** (2 prospects)
  - Sarah Chen (Senior SWE)
  - Marcus Johnson (Lead Backend)
  
- **EcoTrack** (2 prospects)
  - Alex Rivera (CEO)
  - James Kim (CTO)
  
- **QuantumTech Labs** (2 prospects)
  - Dr. Emily Watson (Research Scientist)
  - Dr. Michael Chang (Research Engineer)

This tests the system's ability to:
- Reuse company insights
- Build natural references between prospects
- Accumulate intelligence over time

## Data Richness

Each fake prospect includes:

### Personal Information
- ✓ Name
- ✓ Role/Title
- ✓ Company
- ✓ Bio (detailed)

### Skills & Expertise
- ✓ 5-7 specific skills
- ✓ Tech stack (varies by persona)
- ✓ Industry classification

### Activity & Engagement
- ✓ 4+ recent activities
- ✓ Interests (3-5)
- ✓ Projects (for technical personas)

### Company Context
- ✓ Company description
- ✓ Industry
- ✓ Tech stack
- ✓ Company size/stage (implied)

### Social Profiles (simulated)
- ✓ LinkedIn URL
- ✓ Website URL
- ✓ Twitter/X handle
- ✓ GitHub username (where applicable)

### GitHub Data (for technical prospects)
- ✓ 2-3 projects per person
- ✓ Project descriptions
- ✓ Star counts
- ✓ Programming languages
- ✓ Contribution activity

## Usage

### Quick Start

1. **Run the enhanced main**:
   ```bash
   python main_enhanced.py
   ```

2. **Choose FAKE DATA mode** (option 1)

3. **Select a prospect** (or type 'random'):
   ```
   tech_001    - Sarah Chen (technical)
   exec_001    - David Thompson (executive)
   founder_001 - Alex Rivera (founder)
   research_001- Dr. Emily Watson (researcher)
   ```

4. **Select output channels** as usual

5. **Generate and review** - instant results!

### Testing Company Context Reuse

To test the company context reuse feature:

1. **First run** - Select `tech_001` (Sarah Chen at TechCorp AI)
   - System will generate content
   - Save the results

2. **Second run** - Select `tech_002` (Marcus Johnson at TechCorp AI)
   - System will detect previous TechCorp AI contact
   - Reuse company insights
   - Build natural reference to Sarah
   - Generate content with company context

### Testing All Personas

Use different prospects to test persona analysis:

```bash
# Technical persona
python main_enhanced.py
> 1 (fake data)
> tech_001 (Sarah Chen)

# Executive persona  
python main_enhanced.py
> 1 (fake data)
> exec_001 (David Thompson)

# Founder persona
python main_enhanced.py
> 1 (fake data)
> founder_001 (Alex Rivera)
```

## File Structure

```
CortexReach/
├── fake_data_loader.py           # Fake prospect database
├── enhanced_prospect_loader.py   # Dual-mode input loader
├── enhanced_runner.py            # Dual-mode orchestrator
├── main_enhanced.py              # Enhanced main entry point
├── test_fake_data.py             # Comprehensive test suite
└── FAKE_DATA_DOCS.md            # This file
```

## Testing

### Run the test suite:

```bash
python test_fake_data.py
```

This will:
- ✓ Test all 10 prospects load correctly
- ✓ Verify company grouping works
- ✓ Check data richness
- ✓ Validate persona diversity
- ✓ Ensure all features are testable

### Expected output:
```
TESTING ALL FAKE PROSPECTS
══════════════════════════════════════════════════════════════════════
Total prospects: 10

[tech_001] Testing Sarah Chen...
  ✓ Name: Sarah Chen
  ✓ Company: TechCorp AI
  ✓ Role: Senior Software Engineer
  ...

✓✓✓ ALL TESTS PASSED ✓✓✓
```

## API Reference

### fake_data_loader.py

```python
# List all prospects
prospects = list_fake_prospects()
# Returns: [{'id': 'tech_001', 'name': 'Sarah Chen', ...}, ...]

# Get a specific prospect
prospect = get_fake_prospect('tech_001')
# Returns: {'name': 'Sarah Chen', 'role': '...', ...}

# Get prospect with separated sources
linkedin_data, website_data, x_data, github_data = \
    get_fake_prospect_with_sources('tech_001')

# Get all prospects from a company
prospects = get_company_prospects('TechCorp AI')
# Returns: ['tech_001', 'tech_002']

# Interactive selector
prospect_id = interactive_prospect_selector()
```

### enhanced_prospect_loader.py

```python
# Get user inputs (fake or live)
inputs = get_enhanced_user_inputs()

# Returns for FAKE mode:
{
    'mode': 'fake',
    'prospect_id': 'tech_001',
    'prospect_data': {...},
    'linkedin_data': {...},
    'website_data': {...},
    'x_data': {...},
    'github_data': {...},
    'selected_channels': ['email', 'linkedin']
}

# Returns for LIVE mode:
{
    'mode': 'live',
    'linkedin_url': 'https://...',
    'website_url': 'https://...',
    ...
    'selected_channels': ['email', 'linkedin']
}
```

## Comparison: Fake vs Live

| Feature | Fake Data Mode | Live Scraping Mode |
|---------|---------------|-------------------|
| Speed | ⚡ Instant | ⏱️ 10-30 seconds |
| Internet Required | ❌ No | ✅ Yes |
| Authentication | ❌ No | ✅ Sometimes (LinkedIn, X) |
| Data Quality | ⭐⭐⭐⭐⭐ Comprehensive | ⭐⭐⭐⭐ Varies |
| Reproducible | ✅ Yes | ❌ No (data changes) |
| Rate Limiting | ❌ None | ⚠️ Possible |
| Best For | Testing, demos, learning | Production, real prospects |

## Migration Guide

### From Original to Enhanced

If you have existing code using the original system:

**Before:**
```python
from runner import run_outreach_engine

run_outreach_engine()
```

**After (still works):**
```python
from enhanced_runner import run_enhanced_outreach_engine

run_enhanced_outreach_engine()
# Just select "Live Scraping Mode" when prompted
```

**Or use new main:**
```bash
python main_enhanced.py
# Choose option 2 for live scraping
```

## Tips & Best Practices

### 1. Start with Fake Data
Always test new features with fake data first before using live scraping.

### 2. Use Company Grouping
Test company context reuse by running prospects from the same company sequentially.

### 3. Test All Personas
Different personas test different code paths. Run all types:
- Technical (has GitHub)
- Executive (no GitHub, leadership focus)
- Founder (startup context, funding)
- Researcher (academic, publications)

### 4. Iterate Quickly
Use fake data for rapid iteration:
1. Generate with fake data
2. Test modifications
3. Refine prompts
4. Test again instantly

### 5. Switch to Live for Production
Once satisfied with fake data results, switch to live mode for actual prospects.

## Troubleshooting

### "Prospect ID not found"
- Make sure to use exact ID: `tech_001`, not `Tech_001` or `TECH_001`
- Type `random` to get a random prospect
- Run `python test_fake_data.py` to see all available IDs

### "Import error: fake_data_loader"
- Make sure all files are in the same directory
- Check that `fake_data_loader.py` exists

### "Mode selection doesn't work"
- Enter `1` for fake data or `2` for live scraping
- No other characters or spaces

## Future Enhancements

Potential additions to fake data:

1. **More prospects** - Expand to 20-30 prospects
2. **Industry variety** - Add more industries (retail, manufacturing, etc.)
3. **Geographic diversity** - Add location data
4. **Company sizes** - Startups to enterprises
5. **Custom prospect builder** - Let users create custom fake prospects
6. **Prospect scenarios** - Pre-built test scenarios (cold outreach, warm intro, etc.)

## Contributing

To add new fake prospects:

1. Edit `fake_data_loader.py`
2. Add to `FAKE_PROSPECTS` dictionary
3. Follow existing format
4. Include all required fields
5. Run `python test_fake_data.py` to verify
6. Update counts in documentation

## License

Same as CortexReach - Apache 2.0

---

**Questions or Issues?**

Check the test suite:
```bash
python test_fake_data.py
```

Or run the main with detailed help:
```bash
python main_enhanced.py
> y (show detailed help)
```
