"""
Fixed News Intelligence System - Addressing Unicode and API Issues
"""

import asyncio
import aiohttp
import json
import logging
import random
import sys
import os
from datetime import datetime
from dataclasses import asdict
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

from core.config import Config
from src.core.models import NewsArticle, ScrapingStats
from src.handlers.http_handler import SmartHTTPHandler
from src.handlers.dynamic_content_handler import DynamicContentHandler
from src.handlers.anti_scraping_handler import AntiScrapingHandler
from src.extractors.intelligent_extractor import IntelligentExtractor, SelectorIntelligence
from src.handlers.error_handler import RobustErrorHandler
from utils.content_processor import ContentProcessor
from handlers.error_handler import ErrorHandler


class NewsIntelligenceSystem:
    """
    Fixed version of the news intelligence system
    """

    def __init__(self):
        self.http_handler = SmartHTTPHandler()
        self.dynamic_handler = DynamicContentHandler()
        self.anti_scraping = AntiScrapingHandler()
        self.extractor = IntelligentExtractor()
        self.error_handler = RobustErrorHandler()
        self.content_processor = ContentProcessor()
        self.stats = ScrapingStats()

        # Setup fixed logging
        self.setup_fixed_logging()

        # News sources to demonstrate different scraping challenges
        self.news_sources = [
            "https://www.bbc.com/news/technology", "https://techcrunch.com/",
            "https://www.reuters.com/technology/"
        ]

    def setup_fixed_logging(self):
        """Setup logging with proper Unicode handling"""
        # Ensure UTF-8 encoding for log files
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        # Create handlers with explicit UTF-8 encoding
        file_handler = logging.FileHandler('news_scraper.log',
                                           encoding='utf-8')
        file_handler.setFormatter(logging.Formatter(log_format))

        # Console handler with safe encoding
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(log_format))

        # Configure root logger
        logging.basicConfig(level=logging.INFO,
                            handlers=[file_handler, console_handler],
                            format=log_format)

        self.logger = logging.getLogger(__name__)

        # Test logging with safe characters
        self.logger.info("Starting Fixed News Intelligence System")

    async def analyze_url_before_scraping(self, url: str) -> Dict[str, Any]:
        """Comprehensive URL analysis before scraping"""
        self.logger.info(f"Analyzing URL: {url}")

        analysis = {
            'url': url,
            'domain': urlparse(url).netloc,
            'timestamp': datetime.now().isoformat()
        }

        # Check URL health
        health_check = await self.http_handler.check_url_health(url)
        analysis['health'] = health_check

        if not health_check.get('accessible', False):
            return analysis

        # Get appropriate headers
        headers = self.http_handler.get_smart_headers(url)
        analysis['headers'] = headers

        # Quick content sample to detect frameworks
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers,
                                       timeout=10) as response:
                    sample_content = await response.text()

                    # Detect SPA frameworks
                    frameworks = self.dynamic_handler.detect_spa_framework(
                        sample_content)
                    analysis['frameworks'] = frameworks

                    # Detect anti-scraping measures
                    measures = self.anti_scraping.detect_anti_scraping_measures(
                        sample_content, dict(response.headers))
                    analysis['anti_scraping'] = measures

        except Exception as e:
            analysis['error'] = str(e)

        return analysis

    async def smart_scrape_article(self, url: str) -> Optional[NewsArticle]:
        """Fixed version of article scraping"""
        self.stats.total_requests += 1

        try:
            # Pre-scraping analysis
            analysis = await self.analyze_url_before_scraping(url)
            domain = analysis['domain']

            if not analysis.get('health', {}).get('accessible', False):
                raise Exception(
                    f"URL not accessible: {analysis.get('health', {}).get('error', 'Unknown error')}"
                )

            # Calculate smart delay
            delay = self.anti_scraping.calculate_smart_delay(domain)
            await asyncio.sleep(delay)

            # Configure crawler based on analysis
            frameworks = analysis.get('frameworks', {})

            # Generate smart JavaScript code
            js_code = self.dynamic_handler.generate_smart_js_code(
                url, frameworks)

            # Create wait condition
            wait_condition = self.dynamic_handler.create_wait_conditions(url)

            # Intelligent configuration based on domain name
            domain = urlparse(url).netloc.lower()

            if 'bbc.com' in domain:
                config = CrawlerRunConfig(
                    cache_mode=CacheMode.ENABLED,
                    css_selector='article, .story-body, .story-content',
                    excluded_tags=['nav', 'footer', 'aside'],
                    excluded_selector='.advertisement, .related-content',
                    word_count_threshold=30,
                    exclude_external_links=True,
                    user_agent_mode='random',
                    verbose=True
                )
            elif 'cnn.com' in domain:
                config = CrawlerRunConfig(
                    cache_mode=CacheMode.ENABLED,
                    css_selector='article, .zn-body',
                    excluded_tags=['nav', 'footer', 'aside'],
                    excluded_selector='.ad, .advertisement',
                    word_count_threshold=30,
                    user_agent_mode='random',
                    verbose=True
                )
            elif 'techcrunch.com' in domain:
                config = CrawlerRunConfig(
                    cache_mode=CacheMode.ENABLED,
                    css_selector='article, .entry-content, .post-content',
                    excluded_tags=['nav', 'footer', 'aside'],
                    excluded_selector='.social-share, .advertisement',
                    word_count_threshold=25,
                    exclude_external_links=True,
                    user_agent_mode='random',
                    verbose=True
                )
            elif 'reuters.com' in domain:
                config = CrawlerRunConfig(
                    cache_mode=CacheMode.ENABLED,
                    css_selector='article, .article-body, [data-testid="paragraph"]',
                    excluded_tags=['nav', 'footer', 'aside'],
                    excluded_selector='.advertisement, .related-content',
                    word_count_threshold=30,
                    exclude_external_links=True,
                    user_agent_mode='random',
                    verbose=True
                )
            else:
                # General configuration
                config = CrawlerRunConfig(
                    # Basic settings
                    cache_mode=CacheMode.ENABLED,
                    word_count_threshold=20,
                    # Content selection - focus on news content
                    css_selector='article, main, .content, .story-body',
                    excluded_tags=['nav', 'footer', 'aside', 'script', 'style'],
                    excluded_selector='.advertisement, .ad, .sidebar, .related-content, .social-share',
                    # Link and image processing
                    exclude_external_links=True,
                    exclude_social_media_links=True,
                    exclude_external_images=True,
                    # Anti-detection
                    user_agent_mode='random',
                    check_robots_txt=True,
                    # Output control
                    only_text=False,
                    verbose=True
                )

            # Execute scraping with retry mechanism
            async def scrape_operation():
                # FIXED: Configure crawler with headers separately
                crawler_config = {
                    'verbose': True,
                    'headers': analysis.get('headers',
                                            {})  # Set headers at crawler level
                }

                async with AsyncWebCrawler(**crawler_config) as crawler:
                    result = await crawler.arun(url, config=config)

                    if not result.success:
                        raise Exception(f"Crawling failed: {result.error}")

                    return result

            # Scrape with retry
            result = await self.error_handler.execute_with_retry(
                scrape_operation)

            # Extract data using multiple strategies
            extraction_results = await self.extractor.extract_with_multiple_strategies(
                url, AsyncWebCrawler())

            # Process and combine extraction results
            article = await self.process_extraction_results(
                url, result, extraction_results)

            self.stats.successful_requests += 1
            self.stats.total_articles += 1

            self.logger.info(f"Successfully scraped: {article.title[:50]}...")
            return article

        except Exception as e:
            self.stats.failed_requests += 1
            self.stats.errors.append({
                'url': url,
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'error_type': type(e).__name__
            })

            self.logger.error(f"Failed to scrape {url}: {e}")

            # Handle specific error types
            if "429" in str(e) or "rate" in str(e).lower():
                await self.anti_scraping.handle_rate_limiting(domain, 429)

            return None

    async def process_extraction_results(
            self, url: str, crawl_result: Any,
            extraction_results: Dict) -> NewsArticle:
        """Process and combine results from multiple extraction strategies"""

        # Start with basic information
        article_data = {
            'url': url,
            'title': '',
            'content': '',
            'author': None,
            'publish_date': None,
            'category': None,
            'tags': [],
            'source_domain': urlparse(url).netloc
        }

        # Extract from CSS-based extraction (most reliable)
        css_data = extraction_results.get('css_extraction', {})
        if isinstance(css_data, list) and len(css_data) > 0:
            css_data = css_data[0]

        if isinstance(css_data, dict) and 'error' not in css_data:
            article_data['title'] = css_data.get('title', '')

            # Handle content (might be list of paragraphs)
            content = css_data.get('content', '')
            if isinstance(content, list):
                content = '\n\n'.join(str(p) for p in content if p)
            article_data['content'] = content

            article_data['author'] = css_data.get('author', '')
            article_data['publish_date'] = css_data.get('date', '')
            article_data['category'] = css_data.get('category', '')

        # Fallback to markdown content if CSS extraction failed
        if not article_data['content'] and hasattr(crawl_result, 'markdown'):
            article_data['content'] = crawl_result.markdown

        # Extract title from metadata if not found
        if not article_data['title']:
            if hasattr(crawl_result, 'metadata') and crawl_result.metadata:
                article_data['title'] = crawl_result.metadata.get('title', '')

        # Enhanced content processing
        article_data[
            'content'] = self.content_processor.clean_and_enhance_content(
                article_data['content'])

        # Extract tags from content and metadata
        article_data['tags'] = self.content_processor.extract_tags(
            article_data['content'], crawl_result)

        # Perform sentiment analysis
        sentiment_score = self.content_processor.analyze_sentiment(
            article_data['content'])

        # Create NewsArticle object
        article = NewsArticle(url=article_data['url'],
                              title=self.content_processor.clean_text(
                                  article_data['title']),
                              content=article_data['content'],
                              author=self.content_processor.clean_text(
                                  article_data.get('author', '')),
                              publish_date=self.content_processor.clean_text(
                                  article_data.get('publish_date', '')),
                              category=self.content_processor.clean_text(
                                  article_data.get('category', '')),
                              tags=article_data['tags'],
                              source_domain=article_data['source_domain'],
                              sentiment_score=sentiment_score)

        return article

    async def run_comprehensive_scraping(self,
                                         urls: List[str] = None
                                         ) -> List[NewsArticle]:
        """Run comprehensive scraping demonstration"""
        if urls is None:
            urls = self.news_sources

        self.logger.info(
            f"Starting comprehensive news scraping of {len(urls)} sources")
        self.stats.start_time = datetime.now()

        articles = []

        for i, url in enumerate(urls, 1):
            self.logger.info(f"Processing {i}/{len(urls)}: {url}")

            try:
                article = await self.smart_scrape_article(url)
                if article:
                    articles.append(article)

                    # Log progress with safe characters
                    self.logger.info(
                        f"Article extracted: {article.title[:60]}...")
                    self.logger.info(
                        f"   Content length: {article.content_length} chars")
                    self.logger.info(
                        f"   Tags: {', '.join(article.tags[:3])}...")
                    self.logger.info(
                        f"   Sentiment: {article.sentiment_score:.2f}")

                # Respectful delay between requests
                if i < len(urls):
                    delay = random.uniform(2, 5)
                    await asyncio.sleep(delay)

            except Exception as e:
                self.logger.error(f"Failed to process {url}: {e}")

        self.stats.end_time = datetime.now()

        # Generate comprehensive report
        self.generate_scraping_report(articles)

        return articles

    def generate_scraping_report(self, articles: List[NewsArticle]):
        """Generate comprehensive scraping report with safe logging"""
        self.logger.info("\n" + "=" * 80)
        self.logger.info("COMPREHENSIVE SCRAPING REPORT")
        self.logger.info("=" * 80)

        runtime = self.stats.end_time - self.stats.start_time

        # Basic statistics
        self.logger.info(f"Total Runtime: {runtime}")
        self.logger.info(f"Total Requests: {self.stats.total_requests}")
        self.logger.info(f"Successful: {self.stats.successful_requests}")
        self.logger.info(f"Failed: {self.stats.failed_requests}")
        self.logger.info(f"Articles Extracted: {len(articles)}")

        if self.stats.total_requests > 0:
            success_rate = (self.stats.successful_requests /
                            self.stats.total_requests) * 100
            self.logger.info(f"Success Rate: {success_rate:.1f}%")

        # Content analysis
        if articles:
            avg_content_length = sum(article.content_length
                                     for article in articles) / len(articles)
            avg_sentiment = sum(article.sentiment_score or 0
                                for article in articles) / len(articles)

            self.logger.info(
                f"Average Content Length: {avg_content_length:.0f} characters")
            self.logger.info(f"Average Sentiment Score: {avg_sentiment:.2f}")

            # Top sources
            source_counts = {}
            for article in articles:
                source_counts[article.source_domain] = source_counts.get(
                    article.source_domain, 0) + 1

            self.logger.info("\nSources Summary:")
            for source, count in sorted(source_counts.items(),
                                        key=lambda x: x[1],
                                        reverse=True):
                self.logger.info(f"   {source}: {count} articles")

            # Top tags
            all_tags = []
            for article in articles:
                all_tags.extend(article.tags)

            if all_tags:
                from collections import Counter
                top_tags = Counter(all_tags).most_common(10)
                self.logger.info("\nTop Tags:")
                for tag, count in top_tags:
                    self.logger.info(f"   {tag}: {count}")

        # Error analysis
        if self.stats.errors:
            self.logger.info(
                f"\nError Analysis ({len(self.stats.errors)} errors):")
            error_types = {}
            for error in self.stats.errors:
                error_type = error.get('error_type', 'Unknown')
                error_types[error_type] = error_types.get(error_type, 0) + 1

            for error_type, count in sorted(error_types.items(),
                                            key=lambda x: x[1],
                                            reverse=True):
                self.logger.info(f"   {error_type}: {count}")

    def save_results(self, articles: List[NewsArticle], filename: str = None):
        """Save scraping results to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_scraping_results_{timestamp}.json"

        # Convert articles to serializable format
        articles_data = []
        for article in articles:
            articles_data.append(asdict(article))

        # Add metadata
        report_data = {
            'metadata': {
                'scraping_timestamp':
                datetime.now().isoformat(),
                'total_articles':
                len(articles),
                'scraping_stats':
                asdict(self.stats),
                'extraction_methods': [
                    'CSS Selector-based extraction',
                    'Intelligent JavaScript handling',
                    'Anti-scraping countermeasures',
                    'Multi-strategy data extraction',
                    'Content cleaning and enhancement'
                ]
            },
            'articles': articles_data
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data,
                      f,
                      indent=2,
                      ensure_ascii=False,
                      default=str)

        self.logger.info(f"Results saved to: {filename}")
        return filename


# FIXED: Updated main execution
async def fixed_main():
    """Fixed main function"""
    print("COMPREHENSIVE WEB SCRAPING MASTERY PROJECT - FIXED VERSION")
    print("="*80)

    # Initialize the fixed news intelligence system
    news_system = NewsIntelligenceSystem()

    # Define target URLs that showcase different challenges
    demo_urls = [
        "https://www.bbc.com/news/technology",     # BBC - Structured content
        "https://techcrunch.com/",                 # TechCrunch - Modern SPA
        "https://www.reuters.com/technology/",     # Reuters - International news
    ]

    print(f"Scraping {len(demo_urls)} diverse news sources...")
    print("This will demonstrate:")
    print("• Intelligent URL analysis and preparation")
    print("• Fixed API compatibility issues")
    print("• Proper Unicode logging handling")
    print("• Real-time error handling and recovery")
    print("• Comprehensive result analysis")

    # Run the comprehensive scraping
    try:
        articles = await news_system.run_comprehensive_scraping(demo_urls)

        # Save results
        filename = news_system.save_results(articles)

        print(f"\nScraping demonstration completed successfully!")
        print(f"Extracted {len(articles)} articles from {len(demo_urls)} sources")
        print(f"Detailed results saved to: {filename}")

        # Display sample results
        if articles:
            print(f"\nSample Article Preview:")
            sample = articles[0]
            print(f"   Title: {sample.title}")
            print(f"   Source: {sample.source_domain}")
            print(f"   Content: {sample.content[:200]}...")
            print(f"   Tags: {', '.join(sample.tags[:5])}")
            print(f"   Sentiment: {sample.sentiment_score:.2f}")

    except Exception as e:
        print(f"Demonstration failed: {e}")
        import logging
        logging.exception("Full error details:")


if __name__ == "__main__":
    import asyncio
    print("Starting fixed comprehensive web scraping demonstration...")
    print("=" * 80)

    # Run the fixed demonstration
    asyncio.run(fixed_main())
