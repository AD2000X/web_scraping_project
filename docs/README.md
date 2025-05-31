# Comprehensive Web Scraping Project

A production-ready web scraping system that demonstrates mastery of all web scraping fundamentals including HTTP protocol handling, dynamic content processing, anti-scraping countermeasures, and advanced data extraction strategies.

## 🚀 Features

- **Advanced HTTP Protocol Handling**: Smart header generation, user-agent rotation, and response analysis
- **Dynamic Content Processing**: JavaScript framework detection (React, Vue, Angular) and intelligent handling
- **Anti-Scraping Countermeasures**: Detection and handling of Cloudflare, CAPTCHAs, rate limiting, and bot detection
- **Multi-Strategy Data Extraction**: CSS selectors, semantic analysis, and LLM-based extraction
- **Robust Error Handling**: Exponential backoff, retry mechanisms, and graceful degradation
- **Intelligent Content Processing**: Noise removal, sentiment analysis, and tag extraction
- **Comprehensive Monitoring**: Real-time statistics, performance metrics, and detailed reporting

## 📁 Project Structure

```
web_scraping_project/
├── src/                           
├── examples/
│   ├── main.py
│   ├── simple_news_system.py
│   └── demo_functions.py
├── docs/
├── requirements.txt
├── LICENSE
├── .gitignore
├── unicode_fix_config.py
└── README.md           
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/web-scraping-project.git
   cd web-scraping-project
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers** (required for Crawl4AI):
   ```bash
   playwright install
   ```

## 📋 Requirements

- Python 3.8+
- Crawl4AI >= 0.2.0
- aiohttp >= 3.8.0
- Additional dependencies listed in `requirements.txt`

## 🚀 Quick Start

### Basic Usage

```bash
python main.py
```

### Custom URL Scraping

```python
from news_intelligence_system import NewsIntelligenceSystem

async def custom_scraping():
    system = NewsIntelligenceSystem()
    
    # Define your target URLs
    urls = [
        "https://example-news-site.com/technology",
        "https://another-site.com/articles"
    ]
    
    # Run scraping
    articles = await system.run_comprehensive_scraping(urls)
    
    # Save results
    system.save_results(articles, "custom_results.json")

# Run the custom scraping
import asyncio
asyncio.run(custom_scraping())
```

## 🔧 Configuration

Modify `config.py` to customize:

- **Target URLs**: Add or modify news sources
- **Delays and Timeouts**: Adjust scraping speed and reliability
- **User Agents**: Customize browser identification
- **Domain-Specific Settings**: Configure per-domain behavior
- **Content Filtering**: Adjust content quality thresholds

## 📊 Key Components

### 1. HTTP Handler (`http_handler.py`)
- Smart header generation with domain-specific customization
- User-agent rotation to avoid detection
- URL health checking and response analysis
- Latency monitoring and server identification

### 2. Selector Intelligence (`selector_intelligence.py`)
- Domain-specific CSS selector generation
- Fallback selector chains for robustness
- Support for major news sites (BBC, CNN, Reuters, etc.)
- Generic selectors for unknown sites

### 3. Dynamic Content Handler (`dynamic_content_handler.py`)
- SPA framework detection (React, Vue, Angular, Next.js)
- Intelligent JavaScript code generation
- Wait condition creation for dynamic loading
- Lazy loading and infinite scroll handling

### 4. Anti-Scraping Handler (`anti_scraping_handler.py`)
- Cloudflare and bot detection recognition
- CAPTCHA and rate limiting identification
- Intelligent delay calculation with jitter
- Domain-specific failure tracking

### 5. Intelligent Extractor (`intelligent_extractor.py`)
- Multi-strategy extraction (CSS, LLM, Semantic)
- Adaptive schema generation based on URL analysis
- Content validation and enhancement
- Metadata extraction from various sources

### 6. Content Processing (`utils.py`)
- Advanced text cleaning and noise removal
- Sentiment analysis using keyword matching
- Tag extraction from content and metadata
- Content quality assessment

## 📈 Output and Results

The system generates:

1. **JSON Results File**: Structured data with articles and metadata
2. **Log File**: Detailed execution logs and error tracking
3. **Console Output**: Real-time progress and statistics
4. **Performance Metrics**: Success rates, timing, and error analysis

### Sample Output Structure

```json
{
  "metadata": {
    "scraping_timestamp": "2024-01-15T10:30:00",
    "total_articles": 15,
    "scraping_stats": {...},
    "extraction_methods": [...]
  },
  "articles": [
    {
      "url": "https://example.com/article",
      "title": "Article Title",
      "content": "Article content...",
      "author": "Author Name",
      "publish_date": "2024-01-15",
      "category": "Technology",
      "tags": ["AI", "Machine Learning"],
      "source_domain": "example.com",
      "sentiment_score": 0.3,
      "content_length": 1250
    }
  ]
}
```

## 🎯 Learning Objectives Demonstrated

### ✅ HTTP Protocol Mastery
- Request/response cycle understanding
- Header manipulation and customization
- Status code handling and interpretation
- Connection management and optimization

### ✅ HTML Structure Analysis
- CSS selector expertise and optimization
- DOM traversal and element identification
- Metadata extraction and processing
- Content structure recognition

### ✅ JavaScript & Dynamic Content
- SPA framework detection and handling
- Asynchronous content loading management
- Wait conditions and timing optimization
- Client-side rendering challenges

### ✅ Anti-Scraping Countermeasures
- Detection mechanism recognition
- Evasion strategy implementation
- Rate limiting and delay management
- Browser fingerprinting avoidance

### ✅ Advanced Data Extraction
- Multi-strategy extraction implementation
- Content validation and quality assessment
- Structured data generation
- Error handling and recovery

### ✅ Performance & Monitoring
- Real-time statistics tracking
- Resource usage optimization
- Comprehensive error analysis
- Scalability considerations

## 🛡️ Ethical Considerations

This project is designed for educational and legitimate research purposes. Always ensure:

- Respect for `robots.txt` files
- Adherence to website terms of service
- Reasonable request rates to avoid server overload
- Proper attribution when using scraped content
- Compliance with applicable laws and regulations

## 🔍 Troubleshooting

### Common Issues

1. **Playwright Installation**: Ensure browsers are installed with `playwright install`
2. **Rate Limiting**: Increase delays in `config.py` if encountering 429 errors
3. **JavaScript Timeout**: Adjust `WAIT_TIMEOUT` for slow-loading sites
4. **Memory Usage**: Monitor memory consumption for large-scale scraping

### Debug Mode

Enable verbose logging by modifying the logging level in `main.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

For questions, issues, or suggestions:

1. Check the [Issues](https://github.com/yourusername/web-scraping-project/issues) page
2. Create a new issue with detailed description
3. Include relevant logs and error messages

## 🎓 Educational Value

This project represents production-ready web scraping knowledge that goes beyond basic tutorials. It demonstrates:

- **Professional-grade architecture** with proper separation of concerns
- **Real-world problem solving** for common scraping challenges
- **Best practices** for maintainable and scalable code
- **Comprehensive error handling** for robust operations
- **Performance optimization** for efficient resource usage

Perfect for developers looking to master web scraping or build production scraping systems.
