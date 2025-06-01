"""
Robust error handling and retry mechanisms
"""

import asyncio
import random
import aiohttp
import logging
from typing import Any, Callable


class ErrorHandler:
    """
    Comprehensive error handling and retry mechanisms
    """
    
    def __init__(self):
        self.max_retries = 3
        self.base_delay = 1.0
        self.max_delay = 60.0
        self.backoff_factor = 2.0
        self.logger = logging.getLogger(__name__)
    
    async def execute_with_retry(self, operation: Callable, *args, **kwargs) -> Any:
        """Execute operation with intelligent retry logic"""
        last_exception = None
        
        for attempt in range(self.max_retries + 1):
            try:
                return await operation(*args, **kwargs)
                
            except asyncio.TimeoutError as e:
                last_exception = e
                if attempt < self.max_retries:
                    delay = min(self.base_delay * (self.backoff_factor ** attempt), self.max_delay)
                    jitter = random.uniform(0.8, 1.2)
                    await asyncio.sleep(delay * jitter)
                    self.logger.warning(f"Timeout retry {attempt + 1}/{self.max_retries}")
                
            except aiohttp.ClientError as e:
                last_exception = e
                if "429" in str(e) or "503" in str(e):  # Rate limiting or service unavailable
                    if attempt < self.max_retries:
                        delay = min(30 * (attempt + 1), 120)  # Longer delays for server issues
                        await asyncio.sleep(delay)
                        self.logger.warning(f"Server error retry {attempt + 1}/{self.max_retries}")
                    else:
                        break
                else:
                    break  # Don't retry client errors
                
            except Exception as e:
                last_exception = e
                self.logger.error(f"Unexpected error: {e}")
                break  # Don't retry unexpected errors
        
        raise last_exception


# Create alias for backward compatibility
RobustErrorHandler = ErrorHandler