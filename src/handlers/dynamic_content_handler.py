"""
JavaScript and dynamic content processing handler
"""

from typing import Dict, List
from urllib.parse import urlparse


class DynamicContentHandler:
    """
    JavaScript handling and dynamic content processing
    """
    
    @staticmethod
    def detect_spa_framework(html_content: str) -> Dict[str, bool]:
        """Detect if the page uses SPA frameworks"""
        frameworks = {
            'react': any(pattern in html_content.lower() for pattern in [
                'react', '_react', 'reactdom', 'jsx'
            ]),
            'vue': any(pattern in html_content.lower() for pattern in [
                'vue.js', 'vuejs', 'vue-', '__vue__'
            ]),
            'angular': any(pattern in html_content.lower() for pattern in [
                'angular', 'ng-', 'angularjs'
            ]),
            'nextjs': 'next.js' in html_content.lower() or '__next' in html_content.lower(),
            'nuxt': 'nuxt' in html_content.lower(),
            'svelte': 'svelte' in html_content.lower()
        }
        
        return frameworks
    
    @staticmethod
    def generate_smart_js_code(url: str, framework_info: Dict[str, bool]) -> List[str]:
        """Generate intelligent JavaScript based on detected frameworks"""
        js_code = []
        
        # Universal scroll behavior for lazy loading
        js_code.append("""
        // Intelligent scrolling for lazy-loaded content
        (async () => {
            const initialHeight = document.body.scrollHeight;
            let scrollAttempts = 0;
            const maxScrolls = 5;
            
            while (scrollAttempts < maxScrolls) {
                window.scrollTo(0, document.body.scrollHeight);
                await new Promise(resolve => setTimeout(resolve, 1000));
                
                const newHeight = document.body.scrollHeight;
                if (newHeight === initialHeight) {
                    break;
                }
                scrollAttempts++;
            }
            
            // Scroll back to top
            window.scrollTo(0, 0);
        })();
        """)
        
        # Framework-specific handling
        if framework_info.get('react') or framework_info.get('nextjs'):
            js_code.append("""
            // Wait for React components to fully render
            (async () => {
                let attempts = 0;
                while (attempts < 10) {
                    if (document.querySelector('[data-reactroot], #__next, #root')) {
                        const reactComponents = document.querySelectorAll('[data-react-class], [class*="react"]');
                        if (reactComponents.length > 0) break;
                    }
                    await new Promise(resolve => setTimeout(resolve, 500));
                    attempts++;
                }
            })();
            """)
        
        if framework_info.get('vue') or framework_info.get('nuxt'):
            js_code.append("""
            // Wait for Vue.js hydration
            (async () => {
                let attempts = 0;
                while (attempts < 10) {
                    if (window.Vue || document.querySelector('[data-server-rendered="true"]')) {
                        break;
                    }
                    await new Promise(resolve => setTimeout(resolve, 500));
                    attempts++;
                }
            })();
            """)
        
        # Handle infinite scroll and "Load More" buttons
        if 'news' in url or 'blog' in url:
            js_code.append("""
            // Handle "Load More" buttons and infinite scroll
            (async () => {
                const loadMoreSelectors = [
                    'button[class*="load"], button[class*="more"]',
                    'a[class*="load"], a[class*="more"]',
                    '[data-testid*="load"], [data-testid*="more"]',
                    '.load-more, .show-more, .read-more'
                ];
                
                for (const selector of loadMoreSelectors) {
                    const buttons = document.querySelectorAll(selector);
                    for (const button of buttons) {
                        if (button.offsetParent !== null) { // Check if visible
                            button.click();
                            await new Promise(resolve => setTimeout(resolve, 2000));
                            break;
                        }
                    }
                }
            })();
            """)
        
        return js_code
    
    @staticmethod
    def create_wait_conditions(url: str) -> str:
        """Create intelligent wait conditions based on URL patterns"""
        domain = urlparse(url).netloc
        
        if 'bbc' in domain:
            return "() => document.querySelector('[data-testid=\"headline\"]') !== null"
        elif 'cnn' in domain:
            return "() => document.querySelector('.headline__text') !== null"
        elif 'reuters' in domain:
            return "() => document.querySelector('[data-testid=\"Heading\"]') !== null"
        else:
            # Generic condition for article pages
            return """() => {
                const title = document.querySelector('h1');
                const content = document.querySelectorAll('p');
                return title && content.length > 3;
            }"""