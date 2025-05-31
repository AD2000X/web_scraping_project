"""
Simplified News System for Examples
"""

import asyncio
import json
import logging
import random
import sys
import os
from datetime import datetime
from typing import List, Optional
from urllib.parse import urlparse

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from src.core.models import NewsArticle, ScrapingStats
from src.utils.content_processor import ContentProcessor


class SimpleNewsSystem:
    """
    Simplified news scraping system for demonstration purposes
    """
    
    def __init__(self):
        self.content_processor = ContentProcessor()
        self.stats = ScrapingStats()
        self.setup_simple_logging()
        
        # Default test URLs
        self.test_urls = [
            "https://www.bbc.com/news/technology",
            "https://techcrunch.com/",
            "https://www.reuters.com/technology/"
        ]
    
    def setup_simple_logging(self):
        """Setup basic logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler('simple_scraper.log', encoding='utf-8')
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    async def scrape_single_url(self, url: str) -> Optional[NewsArticle]:
        """Scrape a single URL with basic configuration"""
        self.logger.info(f"Scraping: {url}")
        self.stats.total_requests += 1
        
        try:
            # Create basic configuration
            config = CrawlerRunConfig(
                cache_mode=CacheMode.ENABLED,
                word_count_threshold=20,
                css_selector='article, main, .content',
                excluded_tags=['nav', 'footer', 'aside', 'script', 'style'],
                excluded_selector='.advertisement, .ad, .sidebar',
                exclude_external_links=True,
                user_agent_mode='random',
                verbose=True
            )
            
            # Scrape the URL
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(url, config=config)
                
                if not result.success:
                    raise Exception(f"Scraping failed: {result.error}")
                
                # Extract basic information
                title = ""
                content = result.markdown or ""
                
                # Try to extract title from metadata
                if hasattr(result, 'metadata') and result.metadata:
                    title = result.metadata.get('title', '')
                
                # Clean the content
                content = self.content_processor.clean_and_enhance_content(content)
                
                # Extract tags
                tags = self.content_processor.extract_tags(content, result)
                
                # Analyze sentiment
                sentiment = self.content_processor.analyze_sentiment(content)
                
                # Create article object
                article = NewsArticle(
                    url=url,
                    title=self.content_processor.clean_text(title),
                    content=content,
                    tags=tags,
                    source_domain=urlparse(url).netloc,
                    sentiment_score=sentiment
                )
                
                self.stats.successful_requests += 1
                self.logger.info(f"Successfully extracted: {article.title[:50]}...")
                return article
                
        except Exception as e:
            self.stats.failed_requests += 1
            self.logger.error(f"Failed to scrape {url}: {e}")
            return None
    
    async def run_comprehensive_scraping(self, urls: List[str] = None) -> List[NewsArticle]:
        """Run scraping on multiple URLs"""
        if urls is None:
            urls = self.test_urls
        
        self.logger.info(f"Starting scraping of {len(urls)} URLs")
        self.stats.start_time = datetime.now()
        
        articles = []
        
        for i, url in enumerate(urls, 1):
            self.logger.info(f"Processing {i}/{len(urls)}: {url}")
            
            article = await self.scrape_single_url(url)
            if article:
                articles.append(article)
            
            # Add delay between requests
            if i < len(urls):
                delay = random.uniform(2, 4)
                await asyncio.sleep(delay)
        
        self.stats.end_time = datetime.now()
        self.generate_simple_report(articles)
        
        return articles
    
    def generate_simple_report(self, articles: List[NewsArticle]):
        """Generate a simple scraping report"""
        self.logger.info("\n" + "=" * 60)
        self.logger.info("SIMPLE SCRAPING REPORT")
        self.logger.info("=" * 60)
        
        runtime = self.stats.end_time - self.stats.start_time
        
        self.logger.info(f"Runtime: {runtime}")
        self.logger.info(f"Total Requests: {self.stats.total_requests}")
        self.logger.info(f"Successful: {self.stats.successful_requests}")
        self.logger.info(f"Failed: {self.stats.failed_requests}")
        self.logger.info(f"Articles Extracted: {len(articles)}")
        
        if articles:
            avg_length = sum(len(a.content) for a in articles) / len(articles)
            avg_sentiment = sum(a.sentiment_score or 0 for a in articles) / len(articles)
            
            self.logger.info(f"Average Content Length: {avg_length:.0f} chars")
            self.logger.info(f"Average Sentiment: {avg_sentiment:.2f}")
    
    def save_results(self, articles: List[NewsArticle], filename: str = None) -> str:
        """Save results to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"simple_scraping_results_{timestamp}.json"
        
        # Convert to dict format
        data = {
            'timestamp': datetime.now().isoformat(),
            'total_articles': len(articles),
            'articles': []
        }
        
        for article in articles:
            data['articles'].append({
                'url': article.url,
                'title': article.title,
                'content': article.content[:500] + "..." if len(article.content) > 500 else article.content,
                'tags': article.tags,
                'source_domain': article.source_domain,
                'sentiment_score': article.sentiment_score,
                'content_length': article.content_length
            })
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"Results saved to: {filename}")
        return filename


# Test function
async def test_simple_system():
    """Test the simple news system"""
    print("Testing Simple News System...")
    
    system = SimpleNewsSystem()
    
    # Test with a few URLs
    test_urls = [
        "https://www.bbc.com/news/technology",
        "https://techcrunch.com/"
    ]
    
    articles = await system.run_comprehensive_scraping(test_urls)
    
    if articles:
        filename = system.save_results(articles)
        print(f"\nTest completed. Results saved to: {filename}")
        print(f"Extracted {len(articles)} articles")
    else:
        print("No articles were extracted")


if __name__ == "__main__":
    asyncio.run(test_simple_system())