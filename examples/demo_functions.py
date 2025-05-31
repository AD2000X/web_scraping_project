"""
Advanced demonstration functions for web scraping capabilities
"""

from src.handlers.http_handler import SmartHTTPHandler
from src.handlers.dynamic_content_handler import DynamicContentHandler
from src.handlers.anti_scraping_handler import AntiScrapingHandler

async def demonstrate_http_mastery():
    """Demonstrate HTTP protocol mastery"""
    print("\n🌐 HTTP Protocol Mastery Demonstration")
    print("="*60)
    
    handler = SmartHTTPHandler()
    
    test_urls = [
        "https://www.bbc.com/news",
        "https://edition.cnn.com/",
        "https://www.reuters.com/"
    ]
    
    for url in test_urls:
        print(f"\n🔍 Analyzing: {url}")
        
        # Generate smart headers
        headers = handler.get_smart_headers(url)
        print(f"   📡 User-Agent: {headers['User-Agent'][:50]}...")
        print(f"   🔗 Referer: {headers.get('Referer', 'None')}")
        
        # Check URL health
        health = await handler.check_url_health(url)
        print(f"   ✅ Accessible: {health.get('accessible', False)}")
        print(f"   ⚡ Latency: {health.get('latency', 0):.2f}s")
        print(f"   🖥️  Server: {health.get('server', 'Unknown')}")


async def demonstrate_dynamic_content_handling():
    """Demonstrate JavaScript and dynamic content expertise"""
    print("\n⚡ Dynamic Content Handling Demonstration")
    print("="*60)
    
    handler = DynamicContentHandler()
    
    # Sample HTML content with different frameworks
    test_scenarios = [
        ("React App", '<div id="root" data-reactroot=""></div><script src="/static/js/react.js"></script>'),
        ("Vue App", '<div id="app"></div><script>window.Vue = {}</script>'),
        ("Regular Site", '<html><body><h1>Traditional Website</h1></body></html>')
    ]
    
    for scenario_name, html_content in test_scenarios:
        print(f"\n🧪 Testing: {scenario_name}")
        
        frameworks = handler.detect_spa_framework(html_content)
        print(f"   📦 Detected frameworks: {[k for k, v in frameworks.items() if v]}")
        
        if any(frameworks.values()):
            js_code = handler.generate_smart_js_code("https://example.com", frameworks)
            print(f"   🔧 Generated {len(js_code)} JS handling scripts")
        else:
            print("   📄 Traditional static content detected")


async def demonstrate_anti_scraping_intelligence():
    """Demonstrate anti-scraping countermeasures"""
    print("\n🛡️ Anti-Scraping Intelligence Demonstration")
    print("="*60)
    
    handler = AntiScrapingHandler()
    
    # Simulate different scenarios
    scenarios = [
        ("cloudflare", "Checking your browser before accessing..."),
        ("captcha", "Please complete the CAPTCHA to continue"),
        ("rate_limit", "Too many requests from your IP"),
        ("clean", "Welcome to our news website")
    ]
    
    for scenario_name, sample_content in scenarios:
        print(f"\n🧪 Testing: {scenario_name}")
        
        measures = handler.detect_anti_scraping_measures(sample_content, {})
        detected = [k for k, v in measures.items() if v]
        
        if detected:
            print(f"   🚨 Detected measures: {', '.join(detected)}")
            delay = handler.calculate_smart_delay("example.com")
            print(f"   ⏳ Recommended delay: {delay:.1f}s")
        else:
            print("   ✅ No anti-scraping measures detected")