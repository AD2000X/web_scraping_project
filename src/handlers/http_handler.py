"""
Advanced HTTP protocol handling and management
"""

import aiohttp
import time
from typing import Dict, Any
from urllib.parse import urlparse


class SmartHTTPHandler:
    """
    Advanced HTTP protocol understanding and handling
    """
    
    def __init__(self):
        self.session = None
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]
        self.current_ua_index = 0
    
    def get_smart_headers(self, url: str, referer: str = None) -> Dict[str, str]:
        """Generate intelligent headers based on target URL"""
        domain = urlparse(url).netloc
        
        # Rotate User-Agent
        ua = self.user_agents[self.current_ua_index % len(self.user_agents)]
        self.current_ua_index += 1
        
        headers = {
            'User-Agent': ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        
        # Add appropriate referer
        if referer:
            headers['Referer'] = referer
        elif 'google' not in domain:
            headers['Referer'] = 'https://www.google.com/'
        
        # Domain-specific customizations
        if 'bbc' in domain:
            headers['Accept-Language'] = 'en-GB,en;q=0.9'
        elif 'cnn' in domain:
            headers['Accept-Language'] = 'en-US,en;q=0.9'
        
        return headers
    
    async def check_url_health(self, url: str) -> Dict[str, Any]:
        """Check URL accessibility and response characteristics"""
        try:
            async with aiohttp.ClientSession() as session:
                start_time = time.time()
                async with session.head(url, timeout=10) as response:
                    latency = time.time() - start_time
                    
                    return {
                        'accessible': True,
                        'status_code': response.status,
                        'latency': latency,
                        'server': response.headers.get('Server', 'Unknown'),
                        'content_type': response.headers.get('Content-Type', 'Unknown'),
                        'cache_control': response.headers.get('Cache-Control', 'None'),
                        'has_rate_limit': 'rate-limit' in str(response.headers).lower(),
                        'redirected': len(response.history) > 0
                    }
        except Exception as e:
            return {
                'accessible': False,
                'error': str(e),
                'error_type': type(e).__name__
            }