"""
Main execution script for the comprehensive web scraping project
"""

import asyncio
import nest_asyncio
import logging
import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Apply nest_asyncio for Jupyter compatibility
nest_asyncio.apply()

# Fixed imports
try:
    from src.system.news_intelligence_system import NewsIntelligenceSystem
except ImportError:
    # Fallback for simpler import structure
    from examples.simple_news_system import SimpleNewsSystem as NewsIntelligenceSystem

from examples.demo_functions import (
    demonstrate_http_mastery,
    demonstrate_dynamic_content_handling,
    demonstrate_anti_scraping_intelligence
)


async def main():
    """Main function demonstrating comprehensive web scraping mastery"""
    print("🕷️ COMPREHENSIVE WEB SCRAPING MASTERY PROJECT")
    print("="*80)
    print("This project demonstrates complete understanding of:")
    print("• HTTP Protocol and Headers Management")
    print("• HTML Structure Analysis and CSS Selectors")
    print("• JavaScript and Dynamic Content Processing")
    print("• Anti-Scraping Detection and Countermeasures")
    print("• Advanced Data Extraction Strategies")
    print("• Robust Error Handling and Retry Mechanisms")
    print("• Performance Optimization and Monitoring")
    print("="*80)

    # Run individual demonstrations
    try:
        await demonstrate_http_mastery()
        await demonstrate_dynamic_content_handling()
        await demonstrate_anti_scraping_intelligence()
    except Exception as e:
        print(f"Demo functions failed: {e}")

    # Main scraping demonstration
    print("\n🚀 MAIN SCRAPING DEMONSTRATION")
    print("="*60)

    # Initialize the news intelligence system
    news_system = NewsIntelligenceSystem()

    # Define target URLs that showcase different challenges
    demo_urls = [
        "https://www.bbc.com/news/technology",     # BBC - Structured content
        "https://techcrunch.com/",                 # TechCrunch - Modern SPA
        "https://www.reuters.com/technology/",     # Reuters - International news
    ]

    print(f"📰 Scraping {len(demo_urls)} diverse news sources...")
    print("This will demonstrate:")
    print("• Intelligent URL analysis and preparation")
    print("• Adaptive extraction schema generation")
    print("• Multi-strategy data extraction")
    print("• Real-time error handling and recovery")
    print("• Comprehensive result analysis")

    # Run the comprehensive scraping
    try:
        articles = await news_system.run_comprehensive_scraping(demo_urls)

        # Save results
        filename = news_system.save_results(articles)

        print(f"\n🎉 Scraping demonstration completed successfully!")
        print(f"📊 Extracted {len(articles)} articles from {len(demo_urls)} sources")
        print(f"💾 Detailed results saved to: {filename}")

        # Display sample results
        if articles:
            print(f"\n📰 Sample Article Preview:")
            sample = articles[0]
            print(f"   🏷️  Title: {sample.title}")
            print(f"   🌐 Source: {sample.source_domain}")
            print(f"   📝 Content: {sample.content[:200]}...")
            print(f"   🏷️  Tags: {', '.join(sample.tags[:5])}")
            print(f"   😊 Sentiment: {sample.sentiment_score:.2f}")

    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        logging.exception("Full error details:")


if __name__ == "__main__":
    print("🚀 Starting comprehensive web scraping demonstration...")
    print("=" * 80)

    # Run the main demonstration
    asyncio.run(main())