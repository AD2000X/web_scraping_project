"""
Advanced data extraction engine
"""

import json
from typing import Dict, Any
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig
from crawl4ai.extraction_strategy import (
    JsonCssExtractionStrategy, 
    CosineStrategy
)
from src.extractors.selector_intelligence import SelectorIntelligence


class IntelligentExtractor:
    """
    Advanced data extraction strategies
    """
    
    def __init__(self):
        self.selector_intelligence = SelectorIntelligence()
    
    def create_adaptive_schema(self, url: str) -> Dict[str, Any]:
        """Create adaptive extraction schema based on URL analysis"""
        domain = urlparse(url).netloc
        selectors = self.selector_intelligence.get_selectors_for_domain(domain)
        
        schema = {
            "name": f"News Article Extraction - {domain}",
            "baseSelector": "html",
            "fields": []
        }
        
        # Add fields with fallback selectors
        for field_name, field_selectors in selectors.items():
            schema["fields"].append({
                "name": field_name,
                "selector": ", ".join(field_selectors),  # CSS fallback chain
                "type": "text",
                "multiple": field_name == "content",  # Content can have multiple paragraphs
                "transform": "strip"
            })
        
        # Add metadata fields
        schema["fields"].extend([
            {
                "name": "meta_description",
                "selector": "meta[name='description']",
                "type": "attribute",
                "attribute": "content"
            },
            {
                "name": "meta_keywords",
                "selector": "meta[name='keywords']",
                "type": "attribute", 
                "attribute": "content"
            },
            {
                "name": "og_title",
                "selector": "meta[property='og:title']",
                "type": "attribute",
                "attribute": "content"
            },
            {
                "name": "canonical_url",
                "selector": "link[rel='canonical']",
                "type": "attribute",
                "attribute": "href"
            }
        ])
        
        return schema
    
    def create_llm_extraction_prompt(self, url: str) -> str:
        """Create intelligent LLM extraction prompt"""
        domain = urlparse(url).netloc
        
        if 'bbc' in domain:
            focus = "BBC-style journalism with focus on balanced reporting"
        elif 'cnn' in domain:
            focus = "CNN-style breaking news with emphasis on timeliness"
        elif 'reuters' in domain:
            focus = "Reuters-style factual reporting with international perspective"
        else:
            focus = "general news article structure"
        
        return f"""
        Extract comprehensive information from this {focus} article:
        
        1. **Title**: The main headline of the article
        2. **Author**: Writer(s) or journalist(s) who wrote the article
        3. **Publication Date**: When the article was published
        4. **Category/Section**: News category (Politics, Business, Tech, etc.)
        5. **Content Summary**: A concise 2-3 sentence summary of the main points
        6. **Key Facts**: 3-5 most important factual points from the article
        7. **Quotes**: Any direct quotes from sources or officials
        8. **Location**: Geographic focus of the news (if applicable)
        9. **Tags**: Relevant keywords or topics covered
        10. **Sentiment**: Overall tone (Neutral, Positive, Negative, Mixed)
        
        Focus on accuracy and completeness. If any information is not available, mark it as "Not Available".
        """
    
    async def extract_with_multiple_strategies(self, url: str, crawler: AsyncWebCrawler) -> Dict[str, Any]:
        """Use multiple extraction strategies and combine results"""
        results = {}
        
        # Strategy 1: CSS-based extraction
        try:
            schema = self.create_adaptive_schema(url)
            css_strategy = JsonCssExtractionStrategy(schema, verbose=False)
            
            css_config = CrawlerRunConfig(
                extraction_strategy=css_strategy,
                cache_mode=CacheMode.ENABLED
            )
            
            css_result = await crawler.arun(url, config=css_config)
            if css_result.extracted_content:
                results['css_extraction'] = json.loads(css_result.extracted_content)
        except Exception as e:
            results['css_extraction'] = {'error': str(e)}
        
        # Strategy 2: LLM-based extraction (if API key available)
        try:
            llm_prompt = self.create_llm_extraction_prompt(url)
            # Note: This would require an LLM API key
            # llm_strategy = LLMExtractionStrategy(
            #     provider="openai/gpt-4",
            #     api_token="your_api_key",
            #     instruction=llm_prompt
            # )
            # llm_result = await crawler.arun(url, extraction_strategy=llm_strategy)
            # results['llm_extraction'] = json.loads(llm_result.extracted_content)
            results['llm_extraction'] = {'status': 'LLM API key required'}
        except Exception as e:
            results['llm_extraction'] = {'error': str(e)}
        
        # Strategy 3: Semantic clustering for content analysis
        try:
            semantic_strategy = CosineStrategy(
                semantic_filter="news article content, journalism, current events",
                sim_threshold=0.3,
                max_dist=0.2,
                top_k=5
            )
            
            semantic_config = CrawlerRunConfig(
                extraction_strategy=semantic_strategy,
                cache_mode=CacheMode.ENABLED
            )
            
            semantic_result = await crawler.arun(url, config=semantic_config)
            if semantic_result.extracted_content:
                results['semantic_extraction'] = json.loads(semantic_result.extracted_content)
        except Exception as e:
            results['semantic_extraction'] = {'error': str(e)}
        
        return results