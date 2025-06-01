#!/bin/bash

# =============================================================================
# Web Scraping Project - Deploy to GitHub Develop Branch
# =============================================================================

echo "🕷️ Web Scraping Project - GitHub Deployment Script"
echo "=================================================="

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️ $1${NC}"
}

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    print_error "Not a git repository. Please run 'git init' first or clone your repository."
    exit 1
fi

print_info "Current directory: $(pwd)"

# Step 1: Check current git status
echo -e "\n${BLUE}📊 Checking current git status...${NC}"
git status

# Step 2: Check current branch
echo -e "\n${BLUE}🌿 Current branch:${NC}"
CURRENT_BRANCH=$(git branch --show-current)
echo "Currently on: $CURRENT_BRANCH"

# Step 3: Stash any uncommitted changes
echo -e "\n${BLUE}💾 Stashing any uncommitted changes...${NC}"
git stash push -m "Pre-deployment stash $(date)"

# Step 4: Fetch latest changes from remote
echo -e "\n${BLUE}📥 Fetching latest changes from remote...${NC}"
git fetch origin

# Step 5: Create or switch to develop branch
echo -e "\n${BLUE}🌿 Setting up develop branch...${NC}"
if git show-ref --verify --quiet refs/heads/develop; then
    print_info "Develop branch exists locally. Switching to it..."
    git checkout develop
    git pull origin develop 2>/dev/null || print_warning "No remote develop branch found"
elif git show-ref --verify --quiet refs/remotes/origin/develop; then
    print_info "Develop branch exists on remote. Creating local tracking branch..."
    git checkout -b develop origin/develop
else
    print_info "Creating new develop branch..."
    git checkout -b develop
fi

# Step 6: Apply stashed changes if any
echo -e "\n${BLUE}📂 Applying stashed changes...${NC}"
git stash pop 2>/dev/null || print_info "No stashed changes to apply"

# Step 7: Clean up conflicting files
echo -e "\n${BLUE}🧹 Cleaning up conflicting files...${NC}"
if [ -f "src/utils/utils.py" ]; then
    rm -f src/utils/utils.py
    print_status "Removed duplicate file: src/utils/utils.py"
else
    print_info "No conflicting files found"
fi

# Step 8: Create necessary directory structure
echo -e "\n${BLUE}📁 Creating directory structure...${NC}"
mkdir -p src/{core,handlers,extractors,utils,system}
mkdir -p examples docs
print_status "Directory structure created"

# Step 9: Create __init__.py files
echo -e "\n${BLUE}📄 Creating __init__.py files...${NC}"
for dir in src src/core src/handlers src/extractors src/utils src/system examples; do
    if [ ! -f "$dir/__init__.py" ]; then
        cat > "$dir/__init__.py" << EOF
"""
$(echo $dir | sed 's/src\///g' | sed 's/\// /g' | sed 's/\b\w/\U&/g') package
"""
EOF
        print_status "Created: $dir/__init__.py"
    else
        print_info "Exists: $dir/__init__.py"
    fi
done

# Step 10: Check which files are ready to commit
echo -e "\n${BLUE}📋 Checking files for commit...${NC}"
git add -A
git status

# Step 11: Show what will be committed
echo -e "\n${BLUE}📝 Files to be committed:${NC}"
git diff --cached --name-status

# Step 12: Confirm before committing
echo -e "\n${YELLOW}⚠️ Ready to commit and push to develop branch.${NC}"
read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_warning "Deployment cancelled by user"
    exit 0
fi

# Step 13: Commit changes
echo -e "\n${BLUE}💾 Committing changes...${NC}"
git commit -m "Fix: Complete project refactor - resolve all code conflicts

Major improvements:
- Fix import path conflicts in news_intelligence_system.py
- Remove duplicate ContentProcessor class definitions
- Rename ScrapingConfig to Config for consistency
- Rename RobustErrorHandler to ErrorHandler
- Fix Crawl4AI API compatibility with latest version
- Add missing __init__.py files for proper package structure
- Remove circular imports in examples directory
- Replace emoji characters with safe text for Unicode compatibility
- Update requirements.txt with latest stable dependencies
- Add comprehensive setup automation and documentation

This version resolves all identified conflicts and provides a stable,
production-ready web scraping system with proper error handling,
modern async patterns, and comprehensive documentation.

Breaking Changes:
- Removed src/utils/utils.py (duplicate)
- Updated import paths to use consistent relative imports
- Modified configuration class names for clarity

Migration:
- Run setup_project.py for automatic environment setup
- Update any custom imports to use new class names
- Install updated requirements with: pip install -r requirements.txt

Tested on Python 3.8+ with crawl4ai>=0.6.3"

if [ $? -eq 0 ]; then
    print_status "Changes committed successfully"
else
    print_error "Commit failed"
    exit 1
fi

# Step 14: Push to GitHub
echo -e "\n${BLUE}🚀 Pushing to GitHub develop branch...${NC}"
git push -u origin develop

if [ $? -eq 0 ]; then
    print_status "Successfully pushed to GitHub develop branch!"
else
    print_error "Push failed. Please check your GitHub credentials and network connection."
    exit 1
fi

# Step 15: Display summary
echo -e "\n${GREEN}🎉 Deployment Summary${NC}"
echo "=================================================="
print_status "All fixed files deployed to GitHub develop branch"
print_status "Repository: $(git remote get-url origin 2>/dev/null || echo 'No remote URL found')"
print_status "Branch: develop"
print_status "Commit: $(git rev-parse --short HEAD)"

echo -e "\n${BLUE}📋 Next Steps:${NC}"
echo "1. Visit your GitHub repository to verify the deployment"
echo "2. Create a Pull Request from develop to main when ready"
echo "3. Test the deployment on a fresh environment:"
echo "   git clone -b develop <your-repo-url> test-deployment"
echo "   cd test-deployment && python setup_project.py"

echo -e "\n${BLUE}🔗 Quick Links:${NC}"
REPO_URL=$(git remote get-url origin 2>/dev/null | sed 's/\.git$//')
if [ ! -z "$REPO_URL" ]; then
    echo "Repository: $REPO_URL"
    echo "Develop Branch: $REPO_URL/tree/develop"
    echo "Create PR: $REPO_URL/compare/develop"
fi

echo -e "\n${GREEN}✅ Deployment completed successfully!${NC}"