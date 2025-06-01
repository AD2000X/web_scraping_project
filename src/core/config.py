"""
Configuration settings for the web scraping system
"""

from typing import List, Dict


class Config:
    """Main configuration class for scraping settings"""
    
    # Default news sources
    DEFAULT_NEWS_SOURCES: List[str] = [
        "https://www.bbc.com/news/technology",
        "https://edition.cnn.com/business",
        "https://www.reuters.com/technology/",
        "https://techcrunch.com/",
        "https://www.theguardian.com/technology"
    ]
    
    # HTTP settings
    DEFAULT_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    BASE_DELAY: float = 1.0
    MAX_DELAY: float = 60.0
    BACKOFF_FACTOR: float = 2.0
    
    # User agents for rotation
    USER_AGENTS: List[str] = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    
    # Domain-specific delays
    DOMAIN_DELAYS: Dict[str, float] = {
        'bbc.com': 2.0,
        'cnn.com': 1.5,
        'reuters.com': 2.0,
        'nytimes.com': 3.0,
        'wsj.com': 4.0,
        'techcrunch.com': 2.5,
        'theguardian.com': 2.0
    }
    
    # Content filtering settings
    MIN_CONTENT_LENGTH: int = 50
    MIN_WORD_THRESHOLD: int = 20
    CONTENT_FILTER_THRESHOLD: float = 0.48
    
    # Extraction settings
    MAX_TAGS: int = 10
    MAX_SCROLL_ATTEMPTS: int = 5
    WAIT_TIMEOUT: int = 30000
    
    # Logging settings
    LOG_FILE: str = 'news_scraper.log'
    LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Output settings
    OUTPUT_ENCODING: str = 'utf-8'
    JSON_INDENT: int = 2
    
    # Sentiment analysis keywords
    POSITIVE_KEYWORDS: List[str] = [
        'success', 'growth', 'innovation', 'breakthrough', 'advance', 'improve',
        'excellent', 'outstanding', 'remarkable', 'positive', 'benefit', 'gain',
        'achievement', 'progress', 'development', 'enhancement', 'optimization'
    ]
    
    NEGATIVE_KEYWORDS: List[str] = [
        'failure', 'decline', 'crisis', 'problem', 'issue', 'concern',
        'worry', 'threat', 'risk', 'danger', 'loss', 'decrease',
        'setback', 'challenge', 'difficulty', 'obstacle', 'controversy'
    ]
    
    # Tech-related keywords for tag extraction
    TECH_KEYWORDS: List[str] = [
        'artificial intelligence', 'ai', 'machine learning', 'blockchain',
        'cryptocurrency', 'cybersecurity', 'data privacy', 'cloud computing',
        'software', 'hardware', 'startup', 'innovation', 'digital transformation',
        'automation', 'robotics', 'internet of things', 'iot', '5g', 'quantum computing'
    ]


# Create alias for backward compatibility
ScrapingConfig = Config