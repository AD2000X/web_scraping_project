"""
测试具体文章URL而不是主页
保存为: test_specific_urls.py
"""

import asyncio
from simple_news_system import SimpleNewsSystem

async def test_specific_articles():
    """测试具体的新闻文章URL而不是主页"""
    print("🧪 Testing Specific Article URLs...")
    
    system = SimpleNewsSystem()
    
    # 使用具体的文章URL而不是主页
    test_urls = [
        # BBC具体文章
        "https://www.bbc.com/news/articles/cz9j2k8k2nko",
        
        # 更容易抓取的科技新闻网站
        "https://arstechnica.com/",
        
        # The Verge (也是科技新闻，但可能更容易抓取)
        "https://www.theverge.com/",
        
        # Hacker News (通常较容易抓取)
        "https://news.ycombinator.com/"
    ]
    
    print(f"🔍 Testing {len(test_urls)} diverse URLs...")
    
    all_articles = []
    
    for i, url in enumerate(test_urls, 1):
        print(f"\n--- Testing {i}/{len(test_urls)}: {url} ---")
        
        articles = await system.run_comprehensive_scraping([url])
        
        if articles and articles[0].content_length > 100:
            print(f"✅ Success: {articles[0].content_length} characters")
            print(f"   Title: {articles[0].title[:60]}...")
            all_articles.extend(articles)
        else:
            print(f"⚠️ Limited content extracted")
    
    if all_articles:
        filename = system.save_results(all_articles)
        print(f"\n🎉 Total successful extractions: {len(all_articles)}")
        print(f"📁 Results saved to: {filename}")
    else:
        print("\n❌ No substantial content extracted from any URL")

if __name__ == "__main__":
    asyncio.run(test_specific_articles())