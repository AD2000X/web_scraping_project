
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
