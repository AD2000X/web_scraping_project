"""
Unicode Fix Configuration and Environment Setup
"""

import os
import sys
import locale


def setup_unicode_environment():
    """Setup proper Unicode environment for Windows and other systems"""

    # Set environment variables for UTF-8
    os.environ['PYTHONIOENCODING'] = 'utf-8'

    # For Windows specifically
    if sys.platform.startswith('win'):
        try:
            # Try to set console code page to UTF-8
            os.system('chcp 65001')
        except:
            pass

        # Set locale to support UTF-8
        try:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        except:
            try:
                locale.setlocale(locale.LC_ALL, 'C.UTF-8')
            except:
                pass

    # Ensure stdout/stderr use UTF-8 encoding
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')


def safe_log_message(message: str) -> str:
    """Convert potentially problematic Unicode characters to safe alternatives"""
    emoji_replacements = {
        '🚀': '[ROCKET]',
        '📰': '[NEWS]',
        '🔍': '[SEARCH]',
        '✅': '[SUCCESS]',
        '❌': '[ERROR]',
        '⏳': '[WAITING]',
        '🚫': '[BLOCKED]',
        '🔧': '[MAINTENANCE]',
        '📊': '[REPORT]',
        '⏱️': '[TIMER]',
        '📡': '[SIGNAL]',
        '📈': '[TRENDING]',
        '💾': '[SAVE]',
        '🏷️': '[TAG]',
        '😊': '[POSITIVE]',
        '🌐': '[GLOBAL]',
        '🎉': '[CELEBRATION]',
        '📝': '[DOCUMENT]'
    }

    safe_message = message
    for emoji, replacement in emoji_replacements.items():
        safe_message = safe_message.replace(emoji, replacement)

    return safe_message


class SafeLogger:
    """Logger wrapper that handles Unicode issues gracefully"""

    def __init__(self, logger):
        self.logger = logger

    def info(self, message):
        try:
            self.logger.info(message)
        except UnicodeEncodeError:
            safe_message = safe_log_message(str(message))
            self.logger.info(safe_message)

    def error(self, message):
        try:
            self.logger.error(message)
        except UnicodeEncodeError:
            safe_message = safe_log_message(str(message))
            self.logger.error(safe_message)

    def warning(self, message):
        try:
            self.logger.warning(message)
        except UnicodeEncodeError:
            safe_message = safe_log_message(str(message))
            self.logger.warning(safe_message)

    def debug(self, message):
        try:
            self.logger.debug(message)
        except UnicodeEncodeError:
            safe_message = safe_log_message(str(message))
            self.logger.debug(safe_message)


# Updated requirements.txt content
UPDATED_REQUIREMENTS = """
# Core scraping framework
crawl4ai>=0.3.0

# HTTP and async support
aiohttp>=3.8.0
asyncio
httpx>=0.24.0

# Async utilities
nest-asyncio>=1.5.0

# Data handling
pandas>=1.5.0
numpy>=1.21.0

# Web automation (for Crawl4AI)
playwright>=1.35.0

# Text processing
beautifulsoup4>=4.11.0
lxml>=4.9.0
html5lib>=1.1

# Utility libraries
python-dotenv>=1.0.0
pydantic>=2.0.0
click>=8.1.0

# Optional: For advanced text analysis
# textblob>=0.17.0
# nltk>=3.8.0

# Development tools
pytest>=7.0.0
black>=23.0.0
flake8>=6.0.0
"""

# Troubleshooting guide
TROUBLESHOOTING_GUIDE = """
# Troubleshooting Guide for Web Scraping Issues

## 1. Unicode/Encoding Issues (CP950 Codec Error)

### Problem:
- UnicodeEncodeError: 'cp950' codec can't encode character
- Logging fails with emoji characters

### Solutions:

#### For Windows Users:
1. Set environment variable before running:
   ```cmd
   set PYTHONIOENCODING=utf-8
   chcp 65001
   python your_script.py
   ```

2. Use the SafeLogger class from unicode_fix_config.py

3. Run Python with UTF-8 mode:
   ```cmd
   python -X utf8 your_script.py
   ```

#### For All Systems:
1. Import and call setup_unicode_environment() at the start of your script
2. Use the provided safe_log_message() function
3. Ensure all file operations specify encoding='utf-8'

## 2. Crawl4AI API Changes

### Problem:
- CrawlerRunConfig.__init__() got an unexpected keyword argument 'headers'

### Solution:
The Crawl4AI API has changed. Headers should now be passed to the AsyncWebCrawler constructor, not CrawlerRunConfig.

#### Old (Broken) Way:
```python
config = CrawlerRunConfig(headers=headers, ...)
async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url, config=config)
```

#### New (Fixed) Way:
```python
config = CrawlerRunConfig(...)  # No headers here
async with AsyncWebCrawler(headers=headers) as crawler:
    result = await crawler.arun(url, config=config)
```

## 3. Installation Issues

### Update Crawl4AI:
```bash
pip install --upgrade crawl4ai
playwright install
```

### Full Clean Installation:
```bash
pip uninstall crawl4ai
pip install crawl4ai>=0.3.0
playwright install
```

## 4. Running the Fixed Version

1. Save the provided fixed code as `fixed_news_system.py`
2. Run the setup function:
   ```python
   from unicode_fix_config import setup_unicode_environment
   setup_unicode_environment()
   ```
3. Use the FixedNewsIntelligenceSystem class instead of the original

## 5. Testing the Fix

Run this simple test to verify everything works:

```python
import asyncio
from unicode_fix_config import setup_unicode_environment
from fixed_news_system import fixed_main

# Setup environment
setup_unicode_environment()

# Run the fixed scraper
asyncio.run(fixed_main())
```
"""


if __name__ == "__main__":
    # Setup environment when run directly
    setup_unicode_environment()
    print("Unicode environment configured successfully!")

    # Save updated requirements
    with open('requirements_fixed.txt', 'w', encoding='utf-8') as f:
        f.write(UPDATED_REQUIREMENTS)

    # Save troubleshooting guide
    with open('TROUBLESHOOTING.md', 'w', encoding='utf-8') as f:
        f.write(TROUBLESHOOTING_GUIDE)

    print("Created:")
    print("- requirements_fixed.txt")
    print("- TROUBLESHOOTING.md")