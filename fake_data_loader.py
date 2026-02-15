"""
Fake Data Loader - Comprehensive Sample Data for Testing All Features
======================================================================

Provides rich, realistic fake data covering:
- Multiple data sources (LinkedIn, Website, X, GitHub)
- Diverse personas (Technical, Executive, Founders, Researchers)
- Multiple prospects from same companies (for context reuse testing)
- All analysis features (persona, engagement, hooks)
- Privacy and ethics edge cases

Usage:
    from fake_data_loader import get_fake_prospect, list_fake_prospects, load_fake_prospect_by_id
"""

import random
from datetime import datetime, timedelta


# ============================================================================
# FAKE PROSPECT DATABASE
# ============================================================================

FAKE_PROSPECTS = {
    
    # -------------------------------------------------------------------------
    # TECHNICAL PERSONAS
    # -------------------------------------------------------------------------
    
    "tech_001": {
        "name": "Sarah Chen",
        "role": "Senior Software Engineer",
        "company": "TechCorp AI",
        "bio": "Building the future of AI infrastructure. Ex-Google, passionate about distributed systems and open source.",
        "skills": ["Python", "Kubernetes", "TensorFlow", "Go", "System Design", "AWS"],
        "recent_activity": [
            "Just shipped our new ML training pipeline - 40% faster!",
            "Speaking at PyData conference next month about distributed training",
            "Contributed to TensorFlow Extended framework",
            "Wrote a blog post on optimizing K8s for ML workloads"
        ],
        "interests": ["Machine Learning", "Cloud Architecture", "Open Source", "Rock Climbing"],
        "tech_stack": ["Python", "Kubernetes", "TensorFlow", "PostgreSQL", "Redis", "AWS"],
        "projects": [
            {"name": "ml-pipeline-optimizer", "description": "Tool to optimize ML training pipelines", "stars": 847, "language": "Python"},
            {"name": "k8s-ml-toolkit", "description": "Kubernetes operators for ML workloads", "stars": 324, "language": "Go"},
            {"name": "distributed-training-guide", "description": "Best practices for distributed ML", "stars": 156, "language": "Markdown"}
        ],
        "industry": "Artificial Intelligence",
        "company_description": "TechCorp AI builds enterprise AI infrastructure solutions, helping companies deploy and scale ML models in production.",
        "github_username": "sarahchen",
        "twitter_handle": "@sarahchen_dev",
        "linkedin_url": "https://linkedin.com/in/sarahchen",
        "website_url": "https://techcorp.ai",
        "github_url": "https://github.com/sarahchen",
        "x_url": "https://twitter.com/sarahchen_dev",
        "contribution_activity": "245 contributions in the last year - very active on ML and infrastructure projects"
    },
    
    "tech_002": {
        "name": "Marcus Johnson",
        "role": "Lead Backend Engineer",
        "company": "TechCorp AI",  # Same company as Sarah
        "bio": "API architect and performance enthusiast. Building scalable systems that don't break at 3am.",
        "skills": ["Node.js", "GraphQL", "PostgreSQL", "Redis", "System Design", "API Design"],
        "recent_activity": [
            "Reduced API latency by 60% using connection pooling",
            "Migrated our monolith to microservices - lessons learned",
            "Published article on API versioning best practices",
            "Mentoring junior engineers on system design"
        ],
        "interests": ["Backend Architecture", "Performance Optimization", "Jazz Music", "Coffee"],
        "tech_stack": ["Node.js", "GraphQL", "PostgreSQL", "Redis", "Docker", "AWS"],
        "projects": [
            {"name": "graphql-optimizer", "description": "GraphQL query optimization toolkit", "stars": 512, "language": "JavaScript"},
            {"name": "api-performance-monitor", "description": "Real-time API performance monitoring", "stars": 289, "language": "TypeScript"},
            {"name": "microservices-patterns", "description": "Microservices design patterns in Node.js", "stars": 678, "language": "JavaScript"}
        ],
        "industry": "Artificial Intelligence",
        "company_description": "TechCorp AI builds enterprise AI infrastructure solutions, helping companies deploy and scale ML models in production.",
        "github_username": "marcusjohnson",
        "twitter_handle": "@marcus_codes",
        "linkedin_url": "https://linkedin.com/in/marcusjohnson",
        "website_url": "https://techcorp.ai",
        "github_url": "https://github.com/marcusjohnson",
        "x_url": "https://twitter.com/marcus_codes",
        "contribution_activity": "187 contributions in the last year - focused on backend tooling"
    },
    
    "tech_003": {
        "name": "Priya Sharma",
        "role": "DevOps Engineer",
        "company": "CloudScale Systems",
        "bio": "Infrastructure as Code evangelist. Making deployments boring (in a good way). AWS & Terraform certified.",
        "skills": ["Terraform", "AWS", "Docker", "Kubernetes", "Python", "CI/CD", "Monitoring"],
        "recent_activity": [
            "Automated our entire infrastructure provisioning process",
            "Reduced deployment time from 2 hours to 15 minutes",
            "Gave a talk on Infrastructure as Code best practices",
            "Built custom monitoring dashboard with Grafana"
        ],
        "interests": ["DevOps", "Automation", "Cloud Computing", "Yoga", "Travel"],
        "tech_stack": ["Terraform", "AWS", "Docker", "Kubernetes", "Python", "Jenkins", "Prometheus"],
        "projects": [
            {"name": "terraform-aws-modules", "description": "Reusable Terraform modules for AWS", "stars": 1234, "language": "HCL"},
            {"name": "deployment-automation", "description": "Zero-downtime deployment toolkit", "stars": 456, "language": "Python"},
            {"name": "infra-monitoring", "description": "Infrastructure monitoring and alerting", "stars": 234, "language": "Go"}
        ],
        "industry": "Cloud Infrastructure",
        "company_description": "CloudScale Systems provides cloud infrastructure automation and optimization services for enterprise clients.",
        "github_username": "priyasharma",
        "twitter_handle": "@priya_devops",
        "linkedin_url": "https://linkedin.com/in/priyasharma",
        "website_url": "https://cloudscale.io",
        "github_url": "https://github.com/priyasharma",
        "x_url": "https://twitter.com/priya_devops",
        "contribution_activity": "312 contributions in the last year - heavily involved in IaC projects"
    },
    
    # -------------------------------------------------------------------------
    # EXECUTIVE PERSONAS
    # -------------------------------------------------------------------------
    
    "exec_001": {
        "name": "David Thompson",
        "role": "VP of Engineering",
        "company": "FinTech Innovations",
        "bio": "Leading engineering teams at scale. 15+ years building products that matter. Strong believer in servant leadership.",
        "skills": ["Engineering Leadership", "Product Strategy", "Team Building", "Agile", "Stakeholder Management"],
        "recent_activity": [
            "Grew our engineering team from 20 to 85 in 18 months",
            "Published article on scaling engineering culture in HBR",
            "Speaking at LeadDev conference on technical leadership",
            "Implemented OKRs across all engineering teams"
        ],
        "interests": ["Leadership", "Product Development", "Golf", "Mentorship"],
        "tech_stack": ["Python", "React", "AWS", "Microservices"],  # High-level understanding
        "projects": [],  # Executives typically don't have GitHub projects
        "industry": "Financial Technology",
        "company_description": "FinTech Innovations is revolutionizing banking with AI-powered financial services, serving over 5 million customers globally.",
        "github_username": None,
        "twitter_handle": "@davidthompson",
        "linkedin_url": "https://linkedin.com/in/davidthompson",
        "website_url": "https://fintechinnovations.com",
        "github_url": None,
        "x_url": "https://twitter.com/davidthompson",
        "contribution_activity": None
    },
    
    "exec_002": {
        "name": "Lisa Martinez",
        "role": "Chief Technology Officer",
        "company": "HealthTech Solutions",
        "bio": "Transforming healthcare through technology. Former VP at Amazon Health. Board member at 2 healthcare startups.",
        "skills": ["Technology Strategy", "Digital Transformation", "Healthcare IT", "M&A", "Board Advisory"],
        "recent_activity": [
            "Led successful Series C fundraising - $50M raised",
            "Acquired 2 healthcare AI startups",
            "Keynote at HIMSS on AI in healthcare",
            "Featured in Forbes 40 under 40"
        ],
        "interests": ["Healthcare Innovation", "AI Ethics", "Women in Tech", "Marathon Running"],
        "tech_stack": ["Cloud Architecture", "AI/ML", "HIPAA Compliance", "Healthcare APIs"],
        "projects": [],
        "industry": "Healthcare Technology",
        "company_description": "HealthTech Solutions delivers AI-powered diagnostic tools and patient management systems to hospitals and clinics worldwide.",
        "github_username": None,
        "twitter_handle": "@lisamartinez_cto",
        "linkedin_url": "https://linkedin.com/in/lisamartinez",
        "website_url": "https://healthtechsolutions.com",
        "github_url": None,
        "x_url": "https://twitter.com/lisamartinez_cto",
        "contribution_activity": None
    },
    
    # -------------------------------------------------------------------------
    # FOUNDER/ENTREPRENEUR PERSONAS
    # -------------------------------------------------------------------------
    
    "founder_001": {
        "name": "Alex Rivera",
        "role": "Founder & CEO",
        "company": "EcoTrack",
        "bio": "Building tools to fight climate change. Y Combinator W23. Previously sold startup to Salesforce. Angel investor.",
        "skills": ["Entrepreneurship", "Product Management", "Fundraising", "Climate Tech", "Go-to-Market"],
        "recent_activity": [
            "Just closed our seed round - $3M from top climate VCs",
            "Launched carbon tracking API - 100+ companies signed up",
            "Speaking at TechCrunch Disrupt about climate tech",
            "Hired our first 10 employees"
        ],
        "interests": ["Climate Change", "Startups", "Sustainability", "Hiking"],
        "tech_stack": ["Python", "React", "PostgreSQL", "AWS"],
        "projects": [
            {"name": "ecotrack-sdk", "description": "Carbon tracking SDK for developers", "stars": 234, "language": "Python"},
            {"name": "climate-data", "description": "Open climate data APIs", "stars": 567, "language": "JavaScript"}
        ],
        "industry": "Climate Technology",
        "company_description": "EcoTrack helps businesses measure, reduce, and offset their carbon footprint with AI-powered tracking and recommendations.",
        "github_username": "alexrivera",
        "twitter_handle": "@alexrivera",
        "linkedin_url": "https://linkedin.com/in/alexrivera",
        "website_url": "https://ecotrack.io",
        "github_url": "https://github.com/alexrivera",
        "x_url": "https://twitter.com/alexrivera",
        "contribution_activity": "89 contributions in the last year - mostly on EcoTrack projects"
    },
    
    "founder_002": {
        "name": "James Kim",
        "role": "Co-Founder & CTO",
        "company": "EcoTrack",  # Same company as Alex
        "bio": "Building the technical foundation for climate action. Ex-Stripe engineer. MIT CS grad. Open source contributor.",
        "skills": ["Full Stack Development", "System Architecture", "Team Leadership", "Climate Data", "APIs"],
        "recent_activity": [
            "Built our carbon calculation engine from scratch",
            "Open sourced our emissions factor database",
            "Hiring engineers - we're growing fast!",
            "Integrated with 15 major data providers"
        ],
        "interests": ["Climate Tech", "Open Data", "System Design", "Basketball"],
        "tech_stack": ["Python", "TypeScript", "PostgreSQL", "Redis", "Docker", "AWS"],
        "projects": [
            {"name": "emissions-calculator", "description": "Accurate carbon emissions calculator", "stars": 789, "language": "Python"},
            {"name": "climate-api-client", "description": "Universal climate data API client", "stars": 345, "language": "TypeScript"},
            {"name": "carbon-intelligence", "description": "ML models for carbon reduction recommendations", "stars": 123, "language": "Python"}
        ],
        "industry": "Climate Technology",
        "company_description": "EcoTrack helps businesses measure, reduce, and offset their carbon footprint with AI-powered tracking and recommendations.",
        "github_username": "jameskim",
        "twitter_handle": "@jameskim_dev",
        "linkedin_url": "https://linkedin.com/in/jameskim",
        "website_url": "https://ecotrack.io",
        "github_url": "https://github.com/jameskim",
        "x_url": "https://twitter.com/jameskim_dev",
        "contribution_activity": "423 contributions in the last year - very active on EcoTrack and open source"
    },
    
    "founder_003": {
        "name": "Nina Patel",
        "role": "Founder & CEO",
        "company": "EduAI",
        "bio": "Democratizing education with AI. Former teacher turned founder. Forbes 30 under 30. Passionate about EdTech.",
        "skills": ["Education Technology", "Product Design", "Fundraising", "AI/ML", "Community Building"],
        "recent_activity": [
            "Reached 100,000 students using our platform!",
            "Partnered with 50 schools across 3 countries",
            "Raised Series A - $8M led by Andreessen Horowitz",
            "Won Best EdTech Startup award at EdSurge"
        ],
        "interests": ["Education", "AI for Good", "Reading", "Social Impact"],
        "tech_stack": ["Python", "React", "AI/ML", "Mobile Development"],
        "projects": [
            {"name": "adaptive-learning", "description": "Adaptive learning algorithm for personalized education", "stars": 456, "language": "Python"}
        ],
        "industry": "Education Technology",
        "company_description": "EduAI creates AI-powered personalized learning experiences that adapt to each student's unique needs and learning style.",
        "github_username": "ninapatel",
        "twitter_handle": "@nina_eduai",
        "linkedin_url": "https://linkedin.com/in/ninapatel",
        "website_url": "https://eduai.com",
        "github_url": "https://github.com/ninapatel",
        "x_url": "https://twitter.com/nina_eduai",
        "contribution_activity": "67 contributions in the last year - focused on education projects"
    },
    
    # -------------------------------------------------------------------------
    # RESEARCHER/ACADEMIC PERSONAS
    # -------------------------------------------------------------------------
    
    "research_001": {
        "name": "Dr. Emily Watson",
        "role": "Research Scientist",
        "company": "QuantumTech Labs",
        "bio": "Quantum computing researcher. PhD from Stanford. 20+ publications. Working on quantum algorithms for drug discovery.",
        "skills": ["Quantum Computing", "Python", "Research", "Scientific Writing", "Teaching"],
        "recent_activity": [
            "Published paper in Nature on quantum error correction",
            "Presented at Q2B conference on quantum ML",
            "Received NSF grant for quantum chemistry research",
            "Teaching quantum computing course at Stanford"
        ],
        "interests": ["Quantum Physics", "Drug Discovery", "Scientific Education", "Classical Piano"],
        "tech_stack": ["Python", "Qiskit", "Julia", "MATLAB", "TensorFlow Quantum"],
        "projects": [
            {"name": "quantum-chemistry-toolkit", "description": "Quantum algorithms for molecular simulation", "stars": 234, "language": "Python"},
            {"name": "qml-tutorials", "description": "Quantum machine learning tutorials", "stars": 567, "language": "Jupyter Notebook"},
            {"name": "error-correction-sim", "description": "Quantum error correction simulator", "stars": 189, "language": "Python"}
        ],
        "industry": "Quantum Computing",
        "company_description": "QuantumTech Labs is pioneering quantum computing applications in pharmaceuticals, developing algorithms for drug discovery and molecular modeling.",
        "github_username": "emilywatson",
        "twitter_handle": "@dr_emilywatson",
        "linkedin_url": "https://linkedin.com/in/emilywatson",
        "website_url": "https://quantumtechlabs.com",
        "github_url": "https://github.com/emilywatson",
        "x_url": "https://twitter.com/dr_emilywatson",
        "contribution_activity": "156 contributions in the last year - research-focused projects"
    },
    
    "research_002": {
        "name": "Dr. Michael Chang",
        "role": "Senior Research Engineer",
        "company": "QuantumTech Labs",  # Same company as Emily
        "bio": "Building quantum software infrastructure. MIT PhD. Passionate about making quantum computing accessible to developers.",
        "skills": ["Quantum Software", "Compiler Design", "Python", "C++", "System Architecture"],
        "recent_activity": [
            "Developed new quantum compiler optimization technique",
            "Open sourced our quantum debugging toolkit",
            "Co-authored paper on quantum programming languages",
            "Speaking at PLDI on quantum compiler design"
        ],
        "interests": ["Quantum Software", "Programming Languages", "Compilers", "Photography"],
        "tech_stack": ["Python", "C++", "Qiskit", "Cirq", "Compiler Design"],
        "projects": [
            {"name": "quantum-compiler", "description": "High-performance quantum compiler", "stars": 678, "language": "C++"},
            {"name": "q-debugger", "description": "Debugging tools for quantum programs", "stars": 345, "language": "Python"},
            {"name": "quantum-lang", "description": "Domain-specific language for quantum computing", "stars": 234, "language": "Python"}
        ],
        "industry": "Quantum Computing",
        "company_description": "QuantumTech Labs is pioneering quantum computing applications in pharmaceuticals, developing algorithms for drug discovery and molecular modeling.",
        "github_username": "michaelchang",
        "twitter_handle": "@michael_quantum",
        "linkedin_url": "https://linkedin.com/in/michaelchang",
        "website_url": "https://quantumtechlabs.com",
        "github_url": "https://github.com/michaelchang",
        "x_url": "https://twitter.com/michael_quantum",
        "contribution_activity": "278 contributions in the last year - active in quantum software community"
    },
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def list_fake_prospects():
    """List all available fake prospects with basic info"""
    prospects = []
    for prospect_id, data in FAKE_PROSPECTS.items():
        prospects.append({
            'id': prospect_id,
            'name': data['name'],
            'role': data['role'],
            'company': data['company'],
            'category': prospect_id.split('_')[0]
        })
    return prospects


def get_fake_prospect(prospect_id):
    """
    Get a fake prospect by ID
    
    Args:
        prospect_id: str - prospect ID (e.g., 'tech_001')
    
    Returns:
        dict: prospect data in the format expected by the system
    """
    if prospect_id not in FAKE_PROSPECTS:
        return None
    
    data = FAKE_PROSPECTS[prospect_id]
    
    # Return in the merged format expected by the system
    return {
        'name': data['name'],
        'role': data['role'],
        'company': data['company'],
        'bio': data['bio'],
        'skills': data['skills'],
        'recent_activity': data['recent_activity'],
        'interests': data['interests'],
        'tech_stack': data['tech_stack'],
        'projects': data['projects'],
        'industry': data['industry'],
        'company_description': data['company_description']
    }


def get_fake_prospect_with_sources(prospect_id):
    """
    Get a fake prospect with individual source data separated
    
    Args:
        prospect_id: str
    
    Returns:
        tuple: (linkedin_data, website_data, x_data, github_data)
    """
    if prospect_id not in FAKE_PROSPECTS:
        return None, None, None, None
    
    data = FAKE_PROSPECTS[prospect_id]
    
    # LinkedIn data
    linkedin_data = {
        'name': data['name'],
        'role': data['role'],
        'company': data['company'],
        'bio': data['bio'],
        'skills': data['skills'],
        'recent_posts': data['recent_activity'][:2] if data['recent_activity'] else []
    }
    
    # Website data
    website_data = {
        'company_name': data['company'],
        'description': data['company_description'],
        'industry': data['industry'],
        'tech_stack': data['tech_stack'][:3] if data['tech_stack'] else []
    }
    
    # X/Twitter data
    x_data = {
        'handle': data.get('twitter_handle'),
        'interests': data['interests'],
        'recent_tweets': data['recent_activity'][2:4] if len(data['recent_activity']) > 2 else []
    }
    
    # GitHub data
    github_data = None
    if data.get('github_username') and data.get('projects'):
        github_data = {
            'username': data['github_username'],
            'projects': data['projects'],
            'languages': list(set([p['language'] for p in data['projects'] if p.get('language')])),
            'contribution_activity': data.get('contribution_activity')
        }
    
    return linkedin_data, website_data, x_data, github_data


def display_prospect_menu():
    """Display menu of all available fake prospects"""
    print("\n" + "="*70)
    print("FAKE PROSPECT DATABASE")
    print("="*70)
    
    categories = {
        'tech': 'Technical Professionals',
        'exec': 'Executives',
        'founder': 'Founders/Entrepreneurs',
        'research': 'Researchers/Academics'
    }
    
    for category_key, category_name in categories.items():
        prospects = [(pid, data) for pid, data in FAKE_PROSPECTS.items() if pid.startswith(category_key)]
        if prospects:
            print(f"\n{category_name}:")
            for prospect_id, data in prospects:
                print(f"  [{prospect_id}] {data['name']} - {data['role']} at {data['company']}")
    
    print("\n" + "="*70)


def get_company_prospects(company_name):
    """
    Get all prospects from a specific company
    
    Args:
        company_name: str
    
    Returns:
        list: list of prospect IDs from that company
    """
    return [
        prospect_id for prospect_id, data in FAKE_PROSPECTS.items()
        if data['company'].lower() == company_name.lower()
    ]


def interactive_prospect_selector():
    """
    Interactive menu for selecting a fake prospect
    
    Returns:
        str: selected prospect ID or None
    """
    display_prospect_menu()
    
    print("\nEnter prospect ID (e.g., 'tech_001') or 'random' for random selection:")
    choice = input("> ").strip().lower()
    
    if choice == 'random':
        prospect_id = random.choice(list(FAKE_PROSPECTS.keys()))
        print(f"\nRandomly selected: {FAKE_PROSPECTS[prospect_id]['name']}")
        return prospect_id
    
    if choice in FAKE_PROSPECTS:
        return choice
    
    print(f"Invalid prospect ID: {choice}")
    return None


# ============================================================================
# MAIN - For Testing
# ============================================================================

if __name__ == "__main__":
    print("Fake Data Loader - Testing")
    print("-" * 70)
    
    # List all prospects
    print("\nAvailable prospects:")
    for p in list_fake_prospects():
        print(f"  {p['id']}: {p['name']} ({p['category']})")
    
    # Test getting a prospect
    print("\nTesting get_fake_prospect('tech_001'):")
    prospect = get_fake_prospect('tech_001')
    print(f"  Name: {prospect['name']}")
    print(f"  Company: {prospect['company']}")
    print(f"  Skills: {', '.join(prospect['skills'][:3])}")
    
    # Test company grouping
    print("\nProspects from TechCorp AI:")
    techcorp_prospects = get_company_prospects('TechCorp AI')
    for pid in techcorp_prospects:
        print(f"  {pid}: {FAKE_PROSPECTS[pid]['name']}")
    
    print("\nProspects from EcoTrack:")
    ecotrack_prospects = get_company_prospects('EcoTrack')
    for pid in ecotrack_prospects:
        print(f"  {pid}: {FAKE_PROSPECTS[pid]['name']}")
    
    print("\nProspects from QuantumTech Labs:")
    quantum_prospects = get_company_prospects('QuantumTech Labs')
    for pid in quantum_prospects:
        print(f"  {pid}: {FAKE_PROSPECTS[pid]['name']}")
