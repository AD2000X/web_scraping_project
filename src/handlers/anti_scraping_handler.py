"""
Anti-scraping detection and countermeasures
"""

import asyncio
import random
from typing import Dict


class AntiScrapingHandler:
    """
    Understanding and handling of anti-scraping mechanisms
    """
    
    def __init__(self):
        self.request_delays = {}
        self.failure_counts = {}
        self.last_request_times = {}
    
    def calculate_smart_delay(self, domain: str) -> float:
        """Calculate intelligent delay based on domain and previous failures"""
        base_delay = 1.0
        
        # Domain-specific base delays
        domain_delays = {
            'bbc.com': 2.0,
            'cnn.com': 1.5,
            'reuters.com': 2.0,
            'nytimes.com': 3.0,
            'wsj.com': 4.0
        }
        
        base_delay = domain_delays.get(domain, base_delay)
        
        # Increase delay based on previous failures
        failure_count = self.failure_counts.get(domain, 0)
        if failure_count > 0:
            base_delay *= (1.5 ** failure_count)
        
        # Add random jitter to avoid detection
        jitter = random.uniform(0.5, 1.5)
        
        return min(base_delay * jitter, 30.0)  # Cap at 30 seconds
    
    async def handle_rate_limiting(self, domain: str, status_code: int):
        """Handle rate limiting responses intelligently"""
        if status_code == 429:  # Too Many Requests
            self.failure_counts[domain] = self.failure_counts.get(domain, 0) + 1
            delay = self.calculate_smart_delay(domain)
            
            print(f"⏳ Rate limited on {domain}. Waiting {delay:.1f} seconds...")
            await asyncio.sleep(delay)
            
        elif status_code == 403:  # Forbidden
            self.failure_counts[domain] = self.failure_counts.get(domain, 0) + 1
            print(f"🚫 Access forbidden on {domain}. Increasing delay...")
            
        elif status_code == 503:  # Service Unavailable
            delay = random.uniform(30, 60)
            print(f"🔧 Service unavailable on {domain}. Waiting {delay:.1f} seconds...")
            await asyncio.sleep(delay)
    
    def detect_anti_scraping_measures(self, html_content: str, headers: Dict) -> Dict[str, bool]:
        """Detect various anti-scraping measures"""
        measures = {
            'cloudflare': any(indicator in html_content.lower() for indicator in [
                'cloudflare', 'cf-ray', 'checking your browser'
            ]),
            'captcha': any(indicator in html_content.lower() for indicator in [
                'captcha', 'recaptcha', 'hcaptcha', 'prove you are human'
            ]),
            'javascript_challenge': any(indicator in html_content.lower() for indicator in [
                'please enable javascript', 'javascript is required', 'js-disabled'
            ]),
            'bot_detection': any(indicator in html_content.lower() for indicator in [
                'bot detected', 'automated traffic', 'suspicious activity'
            ]),
            'rate_limiting': 'retry-after' in headers or 'x-ratelimit' in str(headers).lower(),
            'geo_blocking': any(indicator in html_content.lower() for indicator in [
                'not available in your country', 'geo-restricted', 'location restricted'
            ])
        }
        
        return measures