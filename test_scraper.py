#!/usr/bin/env python3
"""
Test script for the Twitter scraper to verify basic functionality.
"""

import sys
import importlib.util

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import pandas as pd
        print("✓ pandas imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pandas: {e}")
        return False
    
    try:
        from ntscraper import Nitter
        print("✓ ntscraper imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ntscraper: {e}")
        return False
    
    try:
        import config
        print("✓ config imported successfully")
        print(f"  - Found {len(config.USERNAMES)} usernames to scrape")
        print(f"  - Output file: {config.OUTPUT_FILE}")
        print(f"  - Tweets per user: {config.TWEETS_PER_USER}")
    except ImportError as e:
        print(f"✗ Failed to import config: {e}")
        return False
    
    return True

def test_scraper_import():
    """Test if the main scraper module can be imported."""
    print("\nTesting scraper module...")
    
    try:
        import scraper
        print("✓ scraper module imported successfully")
        
        # Test if main functions exist
        if hasattr(scraper, 'scrape_twitter_users'):
            print("✓ scrape_twitter_users function found")
        else:
            print("✗ scrape_twitter_users function not found")
            return False
            
        if hasattr(scraper, 'main'):
            print("✓ main function found")
        else:
            print("✗ main function not found")
            return False
            
        return True
        
    except ImportError as e:
        print(f"✗ Failed to import scraper: {e}")
        return False
    except Exception as e:
        print(f"✗ Error testing scraper module: {e}")
        return False

def main():
    """Run all tests."""
    print("Twitter Scraper Test Suite")
    print("=" * 30)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test scraper module
    if not test_scraper_import():
        all_passed = False
    
    print("\n" + "=" * 30)
    if all_passed:
        print("✓ All tests passed! The scraper should work correctly.")
        print("\nTo run the scraper:")
        print("  python3 scraper.py")
    else:
        print("✗ Some tests failed. Please install missing dependencies:")
        print("  pip install -r requirements.txt")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())