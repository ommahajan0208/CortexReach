"""
Test Fake Data - Quick test utility to verify fake data loader
"""

from fake_data_loader import (
    list_fake_prospects,
    get_fake_prospect,
    get_fake_prospect_with_sources,
    get_company_prospects,
    FAKE_PROSPECTS
)


def test_all_fake_prospects():
    """Test loading all fake prospects"""
    print("="*70)
    print("TESTING ALL FAKE PROSPECTS")
    print("="*70)
    
    prospects = list_fake_prospects()
    print(f"\nTotal prospects: {len(prospects)}")
    
    for p in prospects:
        print(f"\n[{p['id']}] Testing {p['name']}...")
        
        # Get merged data
        prospect_data = get_fake_prospect(p['id'])
        
        # Get source-separated data
        linkedin_data, website_data, x_data, github_data = get_fake_prospect_with_sources(p['id'])
        
        # Verify data integrity
        assert prospect_data['name'] == FAKE_PROSPECTS[p['id']]['name'], f"Name mismatch for {p['id']}"
        assert prospect_data['company'] == FAKE_PROSPECTS[p['id']]['company'], f"Company mismatch for {p['id']}"
        assert linkedin_data is not None, f"LinkedIn data missing for {p['id']}"
        assert website_data is not None, f"Website data missing for {p['id']}"
        
        print(f"  ✓ Name: {prospect_data['name']}")
        print(f"  ✓ Company: {prospect_data['company']}")
        print(f"  ✓ Role: {prospect_data['role']}")
        print(f"  ✓ Skills: {len(prospect_data['skills'])} skills")
        print(f"  ✓ Activities: {len(prospect_data['recent_activity'])} activities")
        print(f"  ✓ Projects: {len(prospect_data['projects'])} projects")
        print(f"  ✓ LinkedIn data: Available")
        print(f"  ✓ Website data: Available")
        print(f"  ✓ X data: {'Available' if x_data else 'N/A'}")
        print(f"  ✓ GitHub data: {'Available' if github_data else 'N/A'}")
    
    print("\n" + "="*70)
    print("✓ ALL PROSPECTS TESTED SUCCESSFULLY")
    print("="*70)


def test_company_grouping():
    """Test company grouping feature"""
    print("\n" + "="*70)
    print("TESTING COMPANY GROUPING")
    print("="*70)
    
    companies = {}
    for prospect_id, data in FAKE_PROSPECTS.items():
        company = data['company']
        if company not in companies:
            companies[company] = []
        companies[company].append((prospect_id, data['name']))
    
    print(f"\nTotal unique companies: {len(companies)}")
    
    for company, prospects in companies.items():
        print(f"\n{company}:")
        for prospect_id, name in prospects:
            print(f"  - [{prospect_id}] {name}")
        
        # Verify get_company_prospects function
        company_prospect_ids = get_company_prospects(company)
        assert len(company_prospect_ids) == len(prospects), f"Company prospect count mismatch for {company}"
        print(f"  ✓ get_company_prospects returns {len(company_prospect_ids)} prospects")
    
    # Find companies with multiple prospects (good for testing context reuse)
    multi_prospect_companies = {k: v for k, v in companies.items() if len(v) > 1}
    
    print("\n" + "="*70)
    print("COMPANIES WITH MULTIPLE PROSPECTS (for context reuse testing):")
    print("="*70)
    for company, prospects in multi_prospect_companies.items():
        print(f"\n{company} ({len(prospects)} prospects):")
        for prospect_id, name in prospects:
            print(f"  - [{prospect_id}] {name}")


def test_data_richness():
    """Test that data is rich enough for all features"""
    print("\n" + "="*70)
    print("TESTING DATA RICHNESS")
    print("="*70)
    
    categories = {
        'tech': [],
        'exec': [],
        'founder': [],
        'research': []
    }
    
    for prospect_id, data in FAKE_PROSPECTS.items():
        category = prospect_id.split('_')[0]
        if category in categories:
            categories[category].append((prospect_id, data))
    
    for category, prospects in categories.items():
        if not prospects:
            continue
            
        print(f"\n{category.upper()} CATEGORY ({len(prospects)} prospects):")
        
        for prospect_id, data in prospects:
            print(f"\n  [{prospect_id}] {data['name']}:")
            
            # Check data richness
            checks = {
                'Has bio': bool(data.get('bio')),
                'Has skills (3+)': len(data.get('skills', [])) >= 3,
                'Has activities (3+)': len(data.get('recent_activity', [])) >= 3,
                'Has interests': len(data.get('interests', [])) > 0,
                'Has tech stack': len(data.get('tech_stack', [])) > 0,
                'Has company desc': bool(data.get('company_description')),
                'Has industry': bool(data.get('industry')),
            }
            
            for check, passed in checks.items():
                status = "✓" if passed else "✗"
                print(f"    {status} {check}")
            
            # Category-specific checks
            if category == 'tech':
                has_github = bool(data.get('projects'))
                print(f"    {'✓' if has_github else '✗'} Has GitHub projects")
                
                has_tech_skills = any(skill in ['Python', 'JavaScript', 'Go', 'Java'] 
                                     for skill in data.get('skills', []))
                print(f"    {'✓' if has_tech_skills else '✗'} Has technical skills")
            
            elif category == 'exec':
                has_leadership = any(word in data.get('role', '').lower() 
                                    for word in ['vp', 'cto', 'ceo', 'chief', 'lead'])
                print(f"    {'✓' if has_leadership else '✗'} Has leadership role")
            
            elif category == 'founder':
                has_founder = 'founder' in data.get('role', '').lower() or 'ceo' in data.get('role', '').lower()
                print(f"    {'✓' if has_founder else '✗'} Has founder/CEO role")


def test_persona_diversity():
    """Test that we have diverse personas"""
    print("\n" + "="*70)
    print("TESTING PERSONA DIVERSITY")
    print("="*70)
    
    stats = {
        'total': len(FAKE_PROSPECTS),
        'with_github': 0,
        'without_github': 0,
        'technical': 0,
        'non_technical': 0,
        'industries': set(),
        'companies': set(),
    }
    
    for prospect_id, data in FAKE_PROSPECTS.items():
        if data.get('projects'):
            stats['with_github'] += 1
        else:
            stats['without_github'] += 1
        
        if any(skill in str(data.get('skills', [])) + str(data.get('tech_stack', []))
               for skill in ['Python', 'JavaScript', 'Go', 'Java', 'AWS', 'Docker']):
            stats['technical'] += 1
        else:
            stats['non_technical'] += 1
        
        if data.get('industry'):
            stats['industries'].add(data['industry'])
        
        if data.get('company'):
            stats['companies'].add(data['company'])
    
    print(f"\nTotal Prospects: {stats['total']}")
    print(f"With GitHub: {stats['with_github']}")
    print(f"Without GitHub: {stats['without_github']}")
    print(f"Technical: {stats['technical']}")
    print(f"Non-Technical: {stats['non_technical']}")
    print(f"Unique Industries: {len(stats['industries'])}")
    print(f"Unique Companies: {len(stats['companies'])}")
    
    print(f"\nIndustries represented:")
    for industry in sorted(stats['industries']):
        print(f"  - {industry}")
    
    print(f"\nCompanies represented:")
    for company in sorted(stats['companies']):
        count = len(get_company_prospects(company))
        print(f"  - {company} ({count} prospect{'s' if count > 1 else ''})")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("FAKE DATA LOADER - COMPREHENSIVE TEST SUITE")
    print("="*70)
    
    try:
        # Run all tests
        test_all_fake_prospects()
        test_company_grouping()
        test_data_richness()
        test_persona_diversity()
        
        print("\n" + "="*70)
        print("✓✓✓ ALL TESTS PASSED ✓✓✓")
        print("="*70)
        print("\nFake data is ready for use!")
        print("Run enhanced_runner.py or main to use the data.")
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {str(e)}")
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
