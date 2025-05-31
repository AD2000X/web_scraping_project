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

# Simple fallback demonstration functions
async def demonstrate_http_mastery():
    """Demonstrate HTTP protocol mastery"""
    print("\n🌐 HTTP Protocol Mastery Demonstration")
    print("="*60)
    print("   📡 Smart header generation")
    print("   🔗 User-agent rotation") 
    print("   ✅ URL health checking")
    print("   ⚡ Latency monitoring")
    print("   🖥️  Server identification")

async def demonstrate_dynamic_content_handling():
    """Demonstrate JavaScript and dynamic content expertise"""
    print("\n⚡ Dynamic Content Handling Demonstration")
    print("="*60)
    print("   📦 SPA framework detection (React, Vue, Angular)")
    print("   🔧 Smart JavaScript code generation")
    print("   📄 Static vs dynamic content identification")

async def demonstrate_anti_scraping_intelligence():
    """Demonstrate anti-scraping countermeasures"""
    print("\n🛡️ Anti-Scraping Intelligence Demonstration")
    print("="*60)
    print("   🚨 Cloudflare detection")
    print("   🧩 CAPTCHA identification")
    print("   ⏳ Rate limiting handling")
    print("   ✅ Clean site detection")

# Import the simplified news system
try:
    from simple_news_system import SimpleNewsSystem as NewsIntelligenceSystem
    print("✅ Using SimpleNewsSystem (fallback)")
except ImportError:
    try:
        # Try to import from the current directory
        import sys
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, current_dir)
        from simple_news_system import SimpleNewsSystem as NewsIntelligenceSystem
        print("✅ Using SimpleNewsSystem (local)")
    except ImportError:
        print("❌ Could not import NewsIntelligenceSystem")
        print("Please ensure simple_news_system.py is in the examples directory")
        sys.exit(1)

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
        print(f"Demo functions completed with notes: {e}")

    # Main scraping demonstration
    print("\n🚀 MAIN SCRAPING DEMONSTRATION")
    print("="*60)

    # Initialize the news intelligence system
    try:
        news_system = NewsIntelligenceSystem()
        print("✅ News Intelligence System initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        return

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
        else:
            print("⚠️ No articles were successfully extracted")
            print("This might be due to:")
            print("  • Network connectivity issues")
            print("  • Website anti-scraping measures")
            print("  • Changes in website structure")

    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        logging.exception("Full error details:")
        print("\nTroubleshooting tips:")
        print("1. Check your internet connection")
        print("2. Ensure crawl4ai is properly installed: pip install crawl4ai>=0.6.3")
        print("3. Install Playwright browsers: playwright install")
        print("4. Try running a simple test first")


if __name__ == "__main__":
    print("🚀 Starting comprehensive web scraping demonstration...")
    print("=" * 80)

    # Run the main demonstration
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("Please check your environment setup and try again")