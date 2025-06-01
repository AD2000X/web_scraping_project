# Web Scraping Project with Crawl4AI

A production-ready web scraping system that demonstrates mastery of all web scraping fundamentals including HTTP protocol handling, dynamic content processing, anti-scraping countermeasures, and advanced data extraction strategies.

## 🚀 Deployment

### Quick Deployment to GitHub

**Windows:**
```cmd
scripts/deploy_to_github.bat
```

**Linux/macOS:**
```bash
chmod +x scripts/deploy_to_github.sh
./scripts/deploy_to_github.sh
```

### Manual Deployment
See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) for manual steps.

### Alternative: One-line Deployment
```bash
# For experienced users - deploy current local files to develop branch
git checkout develop && git add -A && git commit -m "Update: Deploy latest changes" && git push origin develop
```

## 📋 Deployment Options

| Method | Best For | Time Required |
|--------|----------|---------------|
| **Automated Scripts** | First-time users, team collaboration | 2-3 minutes |
| **Manual Commands** | Experienced Git users | 5-10 minutes |
| **One-line** | Quick updates | 30 seconds |

## 🔧 Prerequisites for Deployment

- Git configured with GitHub credentials
- Repository access (push permissions)
- All modified files saved locally
- Python environment properly set up

## ✨ Features

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
├── src/                           # Core source code
│   ├── __init__.py               # Package initialization
│   ├── core/                     # Core components
│   │   ├── __init__.py
│   │   ├── config.py            # Configuration settings
│   │   └── models.py            # Data models
│   ├── handlers/                 # Request handling
│   │   ├── __init__.py
│   │   ├── http_handler.py      # HTTP protocol handling
│   │   ├── dynamic_content_handler.py  # JavaScript handling
│   │   ├── anti_scraping_handler.py    # Anti-scraping measures
│   │   └── error_handler.py     # Error handling and retries
│   ├── extractors/               # Data extraction
│   │   ├── __init__.py
│   │   ├── intelligent_extractor.py    # Multi-strategy extraction
│   │   └── selector_intelligence.py    # CSS selector intelligence
│   ├── utils/                    # Utility functions
│   │   ├── __init__.py
│   │   └── content_processor.py # Content processing
│   └── system/                   # Main system
│       ├── __init__.py
│       └── news_intelligence_system.py # Complete system
├── examples/                     # Example implementations
│   ├── __init__.py
│   ├── main.py                  # Main demonstration script
│   ├── simple_news_system.py   # Simplified version
│   └── demo_functions.py       # Individual demos
├── scripts/                     # Deployment scripts
│   ├── deploy_to_github.bat    # Windows deployment
│   └── deploy_to_github.sh     # Linux/macOS deployment
├── docs/                        # Documentation
│   └── README.md               # This file
├── data/                        # Output data (generated)
│   ├── logs/                   # Log files
│   └── outputs/                # Scraping results
├── requirements.txt             # Python dependencies
├── setup_project.py            # Automated setup script
├── unicode_fix_config.py       # Unicode handling utilities
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
└── README.md                   # Main documentation
```

## 🛠️ Installation

### Option 1: Automated Setup (Recommended)
```bash
# Clone the repository
git clone https://github.com/AD2000X/web-scraping-project.git
cd web-scraping-project

# Run automated setup
python setup_project.py

# Test installation
python examples/main.py
```

### Option 2: Manual Installation
```bash
# 1. Clone the repository
git clone https://github.com/AD2000X/web-scraping-project.git
cd web-scraping-project

# 2. Create virtual environment
python -m venv web_scraping_env
# Windows:
web_scraping_env\Scripts\activate
# macOS/Linux:
source web_scraping_env/bin/activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers (required for Crawl4AI)
playwright install

# 5. Test installation
python examples/simple_news_system.py
```

## 📋 System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 2GB free space for dependencies and data
- **Network**: Internet connection for scraping and installing dependencies

### Core Dependencies
- `crawl4ai>=0.6.3` - Advanced web scraping framework
- `aiohttp>=3.8.0` - Asynchronous HTTP client
- `playwright>=1.40.0` - Browser automation
- `beautifulsoup4>=4.12.0` - HTML parsing
- Additional dependencies listed in `requirements.txt`

## 🚀 Quick Start

### Basic Usage - Run Examples
```bash
# Run the main demonstration
python examples/main.py

# Run simplified system
python examples/simple_news_system.py

# Run individual demonstrations
python examples/demo_functions.py
```

### Custom URL Scraping
```python
import asyncio
from src.system.news_intelligence_system import NewsIntelligenceSystem

async def custom_scraping():
    system = NewsIntelligenceSystem()
    
    # Define your target URLs
    urls = [
        "https://www.bbc.com/news/technology",
        "https://techcrunch.com/",
        "https://www.reuters.com/technology/"
    ]
    
    # Run scraping
    articles = await system.run_comprehensive_scraping(urls)
    
    # Save results
    filename = system.save_results(articles, "custom_results.json")
    print(f"Results saved to: {filename}")

# Run the custom scraping
if __name__ == "__main__":
    asyncio.run(custom_scraping())
```

### Using the Simplified System
```python
import asyncio
from examples.simple_news_system import SimpleNewsSystem

async def simple_scraping():
    system = SimpleNewsSystem()
    
    # Use default URLs or specify custom ones
    articles = await system.run_comprehensive_scraping([
        "https://www.bbc.com/news"
    ])
    
    # Save and display results
    if articles:
        filename = system.save_results(articles)
        print(f"Extracted {len(articles)} articles")
        print(f"Results saved to: {filename}")

asyncio.run(simple_scraping())
```

## 🔧 Configuration

The system can be customized by modifying `src/core/config.py`:

### Target URLs
```python
DEFAULT_NEWS_SOURCES = [
    "https://www.bbc.com/news/technology",
    "https://edition.cnn.com/business",
    "https://www.reuters.com/technology/",
    "https://techcrunch.com/",
    "https://www.theguardian.com/technology"
]
```

### Scraping Behavior
```python
# HTTP settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
BASE_DELAY = 1.0

# Domain-specific delays (seconds)
DOMAIN_DELAYS = {
    'bbc.com': 2.0,
    'cnn.com': 1.5,
    'reuters.com': 2.0,
    'techcrunch.com': 2.5
}

# Content filtering
MIN_CONTENT_LENGTH = 50
MIN_WORD_THRESHOLD = 20
```

### User Agents
The system automatically rotates through multiple user agents to avoid detection.

## 📊 Key Components

### 1. HTTP Handler (`src/handlers/http_handler.py`)
- Smart header generation with domain-specific customization
- User-agent rotation to avoid detection
- URL health checking and response analysis
- Latency monitoring and server identification

### 2. Selector Intelligence (`src/extractors/selector_intelligence.py`)
- Domain-specific CSS selector generation
- Fallback selector chains for robustness
- Support for major news sites (BBC, CNN, Reuters, TechCrunch)
- Generic selectors for unknown sites

### 3. Dynamic Content Handler (`src/handlers/dynamic_content_handler.py`)
- SPA framework detection (React, Vue, Angular, Next.js)
- Intelligent JavaScript code generation
- Wait condition creation for dynamic loading
- Lazy loading and infinite scroll handling

### 4. Anti-Scraping Handler (`src/handlers/anti_scraping_handler.py`)
- Cloudflare and bot detection recognition
- CAPTCHA and rate limiting identification
- Intelligent delay calculation with jitter
- Domain-specific failure tracking

### 5. Intelligent Extractor (`src/extractors/intelligent_extractor.py`)
- Multi-strategy extraction (CSS, LLM, Semantic)
- Adaptive schema generation based on URL analysis
- Content validation and enhancement
- Metadata extraction from various sources

### 6. Content Processing (`src/utils/content_processor.py`)
- Advanced text cleaning and noise removal
- Sentiment analysis using keyword matching
- Tag extraction from content and metadata
- Content quality assessment

## 📈 Output and Results

The system generates comprehensive results in multiple formats:

### 1. JSON Results File
Structured data with articles and metadata:
```json
{
  "metadata": {
    "scraping_timestamp": "2024-12-20T10:30:00",
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
      "publish_date": "2024-12-20",
      "category": "Technology",
      "tags": ["AI", "Machine Learning"],
      "source_domain": "example.com",
      "sentiment_score": 0.3,
      "content_length": 1250
    }
  ]
}
```

### 2. Log Files
- **Console Output**: Real-time progress and statistics
- **Log Files**: Detailed execution logs and error tracking
- **Performance Metrics**: Success rates, timing, and error analysis

### 3. Statistical Reports
- Success/failure rates by domain
- Average content length and sentiment scores
- Most common tags and categories
- Error analysis and troubleshooting information

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

This project is designed for **educational and legitimate research purposes**. Always ensure:

- **Respect robots.txt**: Check and follow website robots.txt files
- **Terms of Service**: Adhere to website terms of service and usage policies
- **Reasonable Rates**: Use appropriate request rates to avoid server overload
- **Content Attribution**: Provide proper attribution when using scraped content
- **Legal Compliance**: Comply with applicable laws and regulations in your jurisdiction
- **Data Privacy**: Handle scraped data responsibly and respect privacy rights

## 🔍 Troubleshooting

### Common Issues

#### 1. Installation Problems
```bash
# Playwright browsers not installed
playwright install

# Outdated dependencies
pip install --upgrade -r requirements.txt

# Python version compatibility
python --version  # Should be 3.8+
```

#### 2. Scraping Issues
```bash
# Rate limiting (429 errors)
# Increase delays in src/core/config.py

# JavaScript timeout
# Adjust WAIT_TIMEOUT for slow-loading sites

# Unicode errors
python unicode_fix_config.py
```

#### 3. Import Errors
```bash
# Missing __init__.py files
python setup_project.py

# Path issues
# Ensure you're running from the project root directory
```

### Debug Mode
Enable verbose logging by modifying the logging level:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help
1. Review log files in the `data/logs/` directory
2. Run the diagnostic script: `python setup_project.py`
3. Create a new issue with detailed description and relevant logs

## 🆘 Deployment Troubleshooting

### Common Deployment Issues:
- **Permission denied**: Run `git config --global user.name "Your Name"`
- **Branch conflicts**: Use `git push origin develop --force` to override
- **File encoding errors**: Ensure all files are saved in UTF-8 encoding
- **Network issues**: Check internet connection and GitHub status

### Quick Deployment Fixes:
```bash
# Reset if deployment gets stuck
git reset --hard HEAD
git clean -fd
git add -A
git commit -m "Force deployment"
git push origin develop --force
```

## 🎯 Post-Deployment Steps

1. **Verify on GitHub**: Check your repository's develop branch
2. **Create Pull Request**: Merge develop → main when ready
3. **Test Deployment**:
   ```bash
   git clone -b develop https://github.com/AD2000X/your-repo.git test-deploy
   cd test-deploy
   python setup_project.py
   python examples/main.py
   ```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow the existing code style and add tests
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to the branch**: `git push origin feature/amazing-feature`
6. **Open a Pull Request**: Provide a clear description of your changes

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions and classes
- Include unit tests for new features
- Update documentation as needed
- Test on multiple Python versions (3.8+)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

For questions, issues, or suggestions:

1. **Documentation**: Check this README and other docs in the `docs/` folder
2. **Issues**: Create a [GitHub Issue](https://github.com/AD2000X/web-scraping-project/issues)
3. **Discussions**: Use [GitHub Discussions](https://github.com/AD2000X/web-scraping-project/discussions) for general questions
4. **Email**: Contact the maintainers (include logs and error messages)

### When Reporting Issues
Please include:
- Python version and operating system
- Complete error messages and stack traces
- Steps to reproduce the issue
- Relevant log files from `data/logs/`
- Configuration settings (if modified)

## 🎓 Educational Value

This project represents **production-ready web scraping knowledge** that goes beyond basic tutorials. It demonstrates:

- **Professional Architecture**: Proper separation of concerns and modular design
- **Real-World Problem Solving**: Solutions for common scraping challenges
- **Best Practices**: Maintainable, scalable, and robust code
- **Comprehensive Error Handling**: Graceful failure recovery and retry mechanisms
- **Performance Optimization**: Efficient resource usage and monitoring
- **Industry Standards**: Following established patterns and conventions

Perfect for:
- **Students** learning web scraping fundamentals
- **Developers** building production scraping systems
- **Researchers** conducting data collection projects
- **Teams** needing reliable scraping infrastructure

## 🏆 Project Highlights

- **Multi-Strategy Extraction**: CSS selectors, semantic analysis, and LLM integration
- **Intelligent Framework Detection**: Automatic handling of React, Vue, Angular applications
- **Advanced Anti-Scraping**: Cloudflare, CAPTCHA, and rate limiting detection
- **Comprehensive Monitoring**: Real-time statistics and performance metrics
- **Production Ready**: Error handling, logging, and scalability considerations
- **Educational Focus**: Clear documentation and learning-oriented design

---

**Ready to start scraping?** Run `python setup_project.py` and then `python examples/main.py` to see the system in action!