"""
Data models for the web scraping system
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any, Optional
from urllib.parse import urlparse


@dataclass
class NewsArticle:
    """Structured data model for news articles"""
    url: str
    title: str
    content: str
    author: Optional[str] = None
    publish_date: Optional[str] = None
    category: Optional[str] = None
    tags: List[str] = None
    source_domain: str = ""
    extraction_timestamp: str = ""
    content_length: int = 0
    language: str = "en"
    sentiment_score: Optional[float] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if not self.extraction_timestamp:
            self.extraction_timestamp = datetime.now().isoformat()
        if not self.content_length:
            self.content_length = len(self.content)
        if not self.source_domain and self.url:
            self.source_domain = urlparse(self.url).netloc


@dataclass
class ScrapingStats:
    """Statistics tracking for scraping operations"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_articles: int = 0
    start_time: datetime = None
    end_time: datetime = None
    errors: List[Dict] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.start_time is None:
            self.start_time = datetime.now()