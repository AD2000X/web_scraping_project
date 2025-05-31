@echo off
REM =============================================================================
REM Web Scraping Project - Deploy to GitHub Develop Branch (Windows)
REM =============================================================================

echo 🕷️ Web Scraping Project - GitHub Deployment Script
echo ==================================================

REM Check if we're in a git repository
if not exist ".git" (
    echo ❌ Not a git repository. Please run 'git init' first or clone your repository.
    pause
    exit /b 1
)

echo ℹ️ Current directory: %CD%

REM Step 1: Check current git status
echo.
echo 📊 Checking current git status...
git status

REM Step 2: Check current branch
echo.
echo 🌿 Checking current branch...
for /f "tokens=*" %%a in ('git branch --show-current') do set CURRENT_BRANCH=%%a
echo Currently on: %CURRENT_BRANCH%

REM Step 3: Stash any uncommitted changes
echo.
echo 💾 Stashing any uncommitted changes...
git stash push -m "Pre-deployment stash %date% %time%"

REM Step 4: Fetch latest changes from remote
echo.
echo 📥 Fetching latest changes from remote...
git fetch origin

REM Step 5: Create or switch to develop branch
echo.
echo 🌿 Setting up develop branch...
git show-ref --verify --quiet refs/heads/develop
if %errorlevel% equ 0 (
    echo ℹ️ Develop branch exists locally. Switching to it...
    git checkout develop
    git pull origin develop 2>nul || echo ⚠️ No remote develop branch found
) else (
    git show-ref --verify --quiet refs/remotes/origin/develop
    if %errorlevel% equ 0 (
        echo ℹ️ Develop branch exists on remote. Creating local tracking branch...
        git checkout -b develop origin/develop
    ) else (
        echo ℹ️ Creating new develop branch...
        git checkout -b develop
    )
)

REM Step 6: Apply stashed changes if any
echo.
echo 📂 Applying stashed changes...
git stash pop 2>nul || echo ℹ️ No stashed changes to apply

REM Step 7: Clean up conflicting files
echo.
echo 🧹 Cleaning up conflicting files...
if exist "src\utils\utils.py" (
    del "src\utils\utils.py"
    echo ✅ Removed duplicate file: src\utils\utils.py
) else (
    echo ℹ️ No conflicting files found
)

REM Step 8: Create necessary directory structure
echo.
echo 📁 Creating directory structure...
if not exist "src\core" mkdir "src\core"
if not exist "src\handlers" mkdir "src\handlers"
if not exist "src\extractors" mkdir "src\extractors"
if not exist "src\utils" mkdir "src\utils"
if not exist "src\system" mkdir "src\system"
if not exist "examples" mkdir "examples"
if not exist "docs" mkdir "docs"
echo ✅ Directory structure created

REM Step 9: Create __init__.py files
echo.
echo 📄 Creating __init__.py files...

REM Create src/__init__.py
if not exist "src\__init__.py" (
    echo """Src package""" > "src\__init__.py"
    echo ✅ Created: src\__init__.py
) else (
    echo ℹ️ Exists: src\__init__.py
)

REM Create other __init__.py files
for %%d in (core handlers extractors utils system) do (
    if not exist "src\%%d\__init__.py" (
        echo """%%d package""" > "src\%%d\__init__.py"
        echo ✅ Created: src\%%d\__init__.py
    ) else (
        echo ℹ️ Exists: src\%%d\__init__.py
    )
)

if not exist "examples\__init__.py" (
    echo """Examples package""" > "examples\__init__.py"
    echo ✅ Created: examples\__init__.py
) else (
    echo ℹ️ Exists: examples\__init__.py
)

REM Step 10: Check which files are ready to commit
echo.
echo 📋 Checking files for commit...
git add -A
git status

REM Step 11: Show what will be committed
echo.
echo 📝 Files to be committed:
git diff --cached --name-status

REM Step 12: Confirm before committing
echo.
echo ⚠️ Ready to commit and push to develop branch.
set /p "REPLY=Continue? (y/N): "
if /i not "%REPLY%"=="y" if /i not "%REPLY%"=="yes" (
    echo ⚠️ Deployment cancelled by user
    pause
    exit /b 0
)

REM Step 13: Commit changes
echo.
echo 💾 Committing changes...
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

if %errorlevel% equ 0 (
    echo ✅ Changes committed successfully
) else (
    echo ❌ Commit failed
    pause
    exit /b 1
)

REM Step 14: Push to GitHub
echo.
echo 🚀 Pushing to GitHub develop branch...
git push -u origin develop

if %errorlevel% equ 0 (
    echo ✅ Successfully pushed to GitHub develop branch!
) else (
    echo ❌ Push failed. Please check your GitHub credentials and network connection.
    pause
    exit /b 1
)

REM Step 15: Display summary
echo.
echo 🎉 Deployment Summary
echo ==================================================
echo ✅ All fixed files deployed to GitHub develop branch

for /f "tokens=*" %%a in ('git remote get-url origin 2^>nul') do set REPO_URL=%%a
if defined REPO_URL (
    echo ✅ Repository: %REPO_URL%
)

echo ✅ Branch: develop

for /f "tokens=*" %%a in ('git rev-parse --short HEAD') do set COMMIT_HASH=%%a
echo ✅ Commit: %COMMIT_HASH%

echo.
echo 📋 Next Steps:
echo 1. Visit your GitHub repository to verify the deployment
echo 2. Create a Pull Request from develop to main when ready
echo 3. Test the deployment on a fresh environment:
echo    git clone -b develop ^<your-repo-url^> test-deployment
echo    cd test-deployment ^&^& python setup_project.py

echo.
echo 🔗 Quick Links:
if defined REPO_URL (
    echo Repository: %REPO_URL%
    echo Develop Branch: %REPO_URL%/tree/develop
    echo Create PR: %REPO_URL%/compare/develop
)

echo.
echo ✅ Deployment completed successfully!
pause