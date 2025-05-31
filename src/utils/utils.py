"""
Utility functions for content processing and analysis
"""

import re
from typing import List, Any
from collections import Counter


class ContentProcessor:
    """Utility class for content processing and analysis"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and normalize text content"""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', str(text))
        
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\"\']+', '', text)
        
        # Remove common noise patterns
        noise_patterns = [
            r'Share this article.*',
            r'Follow us on.*',
            r'Subscribe to.*',
            r'Click here.*',
            r'Read more:.*',
            r'Related:.*'
        ]
        
        for pattern in noise_patterns:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
        return text.strip()
    
    @staticmethod
    def clean_and_enhance_content(content: str) -> str:
        """Clean and enhance article content"""
        if not content:
            return ""
        
        # Split into paragraphs
        paragraphs = content.split('\n\n')
        cleaned_paragraphs = []
        
        for para in paragraphs:
            para = para.strip()
            
            # Skip very short paragraphs (likely noise)
            if len(para) < 50:
                continue
            
            # Skip paragraphs that are likely navigation or ads
            skip_patterns = [
                r'share this',
                r'follow us',
                r'subscribe',
                r'advertisement',
                r'related articles',
                r'more from',
                r'trending now'
            ]
            
            should_skip = any(re.search(pattern, para, re.IGNORECASE) for pattern in skip_patterns)
            if should_skip:
                continue
            
            cleaned_paragraphs.append(ContentProcessor.clean_text(para))
        
        return '\n\n'.join(cleaned_paragraphs)
    
    @staticmethod
    def extract_tags(content: str, crawl_result: Any) -> List[str]:
        """Extract relevant tags from content and metadata"""
        tags = set()
        
        # Extract from metadata keywords
        if hasattr(crawl_result, 'metadata') and crawl_result.metadata:
            meta_keywords = crawl_result.metadata.get('keywords', '')
            if meta_keywords:
                tags.update(tag.strip() for tag in meta_keywords.split(','))
        
        # Extract key phrases from content using simple NLP
        if content:
            # Common tech/news keywords
            tech_keywords = [
                'artificial intelligence', 'ai', 'machine learning', 'blockchain',
                'cryptocurrency', 'cybersecurity', 'data privacy', 'cloud computing',
                'software', 'hardware', 'startup', 'innovation', 'digital transformation'
            ]
            
            content_lower = content.lower()
            for keyword in tech_keywords:
                if keyword in content_lower:
                    tags.add(keyword.title())
        
        return list(tags)[:10]  # Limit to 10 tags
    
    @staticmethod
    def analyze_sentiment(content: str) -> float:
        """Simple sentiment analysis using keyword matching"""
        if not content:
            return 0.0
        
        positive_words = [
            'success', 'growth', 'innovation', 'breakthrough', 'advance', 'improve',
            'excellent', 'outstanding', 'remarkable', 'positive', 'benefit', 'gain'
        ]
        
        negative_words = [
            'failure', 'decline', 'crisis', 'problem', 'issue', 'concern',
            'worry', 'threat', 'risk', 'danger', 'loss', 'decrease'
        ]
        
        content_lower = content.lower()
        positive_score = sum(1 for word in positive_words if word in content_lower)
        negative_score = sum(1 for word in negative_words if word in content_lower)
        
        total_words = len(content.split())
        if total_words == 0:
            return 0.0
        
        # Normalize to -1 to 1 scale
        sentiment = (positive_score - negative_score) / max(total_words / 100, 1)
        return max(-1.0, min(1.0, sentiment))