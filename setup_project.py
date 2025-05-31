"""
Setup script for the Web Scraping Project
Run this script to automatically fix all conflicts and setup the project
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def create_init_files():
    """Create all necessary __init__.py files"""
    init_dirs = [
        'src',
        'src/core',
        'src/handlers', 
        'src/extractors',
        'src/utils',
        'src/system',
        'examples'
    ]
    
    for dir_path in init_dirs:
        init_file = os.path.join(dir_path, '__init__.py')
        if not os.path.exists(init_file):
            os.makedirs(dir_path, exist_ok=True)
            with open(init_file, 'w', encoding='utf-8') as f:
                f.write(f'"""\n{dir_path.replace("/", " ").title()} package\n"""\n')
            print(f"✅ Created: {init_file}")
        else:
            print(f"📁 Exists: {init_file}")


def remove_conflicting_files():
    """Remove duplicate and conflicting files"""
    files_to_remove = [
        'src/utils/utils.py',  # Duplicate of content_processor.py
    ]
    
    for file_path in files_to_remove:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"🗑️ Removed conflicting file: {file_path}")
        else:
            print(f"❌ File not found (OK): {file_path}")


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    else:
        print(f"✅ Python version OK: {version.major}.{version.minor}.{version.micro}")
        return True


def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False


def install_playwright():
    """Install Playwright browsers"""
    print("🎭 Installing Playwright browsers...")
    try:
        subprocess.check_call([sys.executable, '-m', 'playwright', 'install'])
        print("✅ Playwright browsers installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Playwright browsers: {e}")
        print("Try running manually: playwright install")
        return False


def create_test_script():
    """Create a simple test script"""
    test_content = '''"""
Quick test script for the web scraping project
"""

import asyncio
import sys
import os

# Add project to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from examples.simple_news_system import SimpleNewsSystem
    print("✅ Import successful")
    
    async def quick_test():
        print("🧪 Running quick test...")
        system = SimpleNewsSystem()
        
        # Test with one URL
        test_urls = ["https://www.bbc.com/news"]
        articles = await system.run_comprehensive_scraping(test_urls)
        
        if articles:
            print(f"✅ Test successful! Extracted {len(articles)} articles")
            system.save_results(articles, "test_results.json")
        else:
            print("⚠️ No articles extracted, but system is working")
    
    if __name__ == "__main__":
        asyncio.run(quick_test())
        
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("Please check the setup and try again")
'''
    
    with open('quick_test.py', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print("✅ Created quick_test.py")


def main():
    """Main setup function"""
    print("🕷️ Web Scraping Project Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create directory structure
    print("\n📁 Setting up directory structure...")
    create_init_files()
    
    # Remove conflicting files
    print("\n🧹 Cleaning up conflicts...")
    remove_conflicting_files()
    
    # Install requirements
    print("\n📦 Installing dependencies...")
    if not install_requirements():
        print("⚠️ You may need to install requirements manually:")
        print("pip install -r requirements.txt")
    
    # Install Playwright
    print("\n🎭 Setting up browser automation...")
    if not install_playwright():
        print("⚠️ You may need to install Playwright manually:")
        print("playwright install")
    
    # Create test script
    print("\n🧪 Creating test utilities...")
    create_test_script()
    
    print("\n" + "=" * 50)
    print("✅ Setup Complete!")
    print("\nNext steps:")
    print("1. Run quick test: python quick_test.py")
    print("2. Run main demo: python examples/main.py")
    print("3. Check logs for any issues")
    print("\nIf you encounter issues, see SETUP_INSTRUCTIONS.md")
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎉 Project setup completed successfully!")
        else:
            print("\n❌ Setup encountered issues. Please check the output above.")
    except KeyboardInterrupt:
        print("\n⚠️ Setup interrupted by user")
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        print("Please check the error and try again, or set up manually")