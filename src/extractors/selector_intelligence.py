"""
Intelligent CSS selector generation for different websites
"""

from typing import Dict, List, Any


class SelectorIntelligence:
    """
    HTML structure analysis and CSS selector expertise
    """
    
    @staticmethod
    def generate_news_selectors() -> Dict[str, Dict[str, Any]]:
        """Generate intelligent selectors for different news websites"""
        return {
            'bbc.com': {
                'title': [
                    'h1[data-testid="headline"]',
                    'h1.story-headline',
                    'h1',
                    '.headline h1'
                ],
                'content': [
                    '[data-component="text-block"] p',
                    '.story-body p',
                    '.entry-content p',
                    'article p'
                ],
                'author': [
                    '[data-testid="byline"]',
                    '.byline',
                    '.author',
                    '.journalist'
                ],
                'date': [
                    '[data-testid="timestamp"]',
                    'time',
                    '.date',
                    '.published'
                ],
                'category': [
                    '.category',
                    '.section',
                    '.topic'
                ]
            },
            
            'cnn.com': {
                'title': [
                    'h1.headline__text',
                    'h1[data-analytics="headline"]',
                    'h1',
                    '.headline h1'
                ],
                'content': [
                    '.zn-body__paragraph',
                    '.zn-body p',
                    '.article-content p',
                    'article p'
                ],
                'author': [
                    '.byline__name',
                    '.metadata__byline',
                    '.byline',
                    '.author'
                ],
                'date': [
                    '.timestamp',
                    '.update-time',
                    'time',
                    '.date'
                ],
                'category': [
                    '.metadata__section',
                    '.section',
                    '.category'
                ]
            },
            
            'reuters.com': {
                'title': [
                    '[data-testid="Heading"]',
                    'h1[data-module="ArticleHeader"]',
                    'h1',
                    '.article-header h1'
                ],
                'content': [
                    '[data-testid="paragraph"]',
                    '.article-body p',
                    '.content p',
                    'article p'
                ],
                'author': [
                    '[data-testid="byline"]',
                    '.author',
                    '.byline'
                ],
                'date': [
                    '[data-testid="dateTime"]',
                    'time',
                    '.date'
                ],
                'category': [
                    '.kicker',
                    '.section',
                    '.category'
                ]
            },
            
            # Generic fallback selectors for unknown sites
            'generic': {
                'title': [
                    'h1',
                    '.title h1',
                    '.headline h1',
                    '.entry-title',
                    '.article-title',
                    '[itemprop="headline"]'
                ],
                'content': [
                    'article p',
                    '.content p',
                    '.entry-content p',
                    '.article-content p',
                    '.post-content p',
                    '.story p',
                    '[itemprop="articleBody"] p'
                ],
                'author': [
                    '.author',
                    '.byline',
                    '.writer',
                    '[rel="author"]',
                    '[itemprop="author"]',
                    '.journalist'
                ],
                'date': [
                    'time',
                    '.date',
                    '.published',
                    '.publish-date',
                    '[datetime]',
                    '[itemprop="datePublished"]'
                ],
                'category': [
                    '.category',
                    '.section',
                    '.topic',
                    '.tag'
                ]
            }
        }
    
    @staticmethod
    def get_selectors_for_domain(domain: str) -> Dict[str, List[str]]:
        """Get appropriate selectors for a specific domain"""
        selectors = SelectorIntelligence.generate_news_selectors()
        
        # Find matching domain pattern
        for pattern, domain_selectors in selectors.items():
            if pattern in domain or pattern == 'generic':
                return domain_selectors
        
        return selectors['generic']