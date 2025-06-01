# src/core/__init__.py
"""
Core components for the web scraping system
"""

from .config import Config
from .models import NewsArticle, ScrapingStats

__all__ = ['Config', 'NewsArticle', 'ScrapingStats']

# ================================================================

# src/handlers/__init__.py
"""
Handler modules for web scraping operations
"""

from .http_handler import SmartHTTPHandler
from .dynamic_content_handler import DynamicContentHandler
from .anti_scraping_handler import AntiScrapingHandler
from .error_handler import ErrorHandler

__all__ = [
    'SmartHTTPHandler',
    'DynamicContentHandler', 
    'AntiScrapingHandler',
    'ErrorHandler'
]

# ================================================================

# src/extractors/__init__.py
"""
Data extraction components
"""

from .intelligent_extractor import IntelligentExtractor
from .selector_intelligence import SelectorIntelligence

__all__ = ['IntelligentExtractor', 'SelectorIntelligence']

# ================================================================

# src/utils/__init__.py
"""
Utility functions and classes
"""

from .content_processor import ContentProcessor

__all__ = ['ContentProcessor']

# ================================================================

# src/system/__init__.py
"""
Main system components
"""

from .news_intelligence_system import NewsIntelligenceSystem

__all__ = ['NewsIntelligenceSystem']

# ================================================================

# examples/__init__.py
"""
Example scripts and demonstrations
"""

# This file allows the examples directory to be treated as a Python package