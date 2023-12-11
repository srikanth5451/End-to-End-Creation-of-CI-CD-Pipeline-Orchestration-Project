# save as generate_commits.py
import os
import random
from datetime import datetime, timedelta
import subprocess

def create_commits(repo_path):
    os.chdir(repo_path)
    
    # Create realistic files
    files = [
        "src/main.py",
        "src/utils.py",
        "tests/test_core.py",
        "docs/ARCHITECTURE.md",
        ".github/workflows/ci.yml"
    ]
    
    # Create directories if they don't exist
    for f in files:
        os.makedirs(os.path.dirname(f), exist_ok=True)
    
    for i in range(1, 101):
        # Spread commits over 3 years
        commit_date = datetime.now() - timedelta(days=random.randint(1, 1095))
        date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        
        # Select a file to modify
        file_path = random.choice(files)
        
        # Generate realistic content based on file type
        if file_path.endswith('.py'):
            content = f'''# Commit {i} - {commit_date.strftime("%B %Y")}
            
def feature_{i}():
    """Auto-generated feature for commit {i}"""
    print("Implementing feature {i}")
    
    # {'Optimized' if i % 3 == 0 else 'Basic'} implementation
    return {i * random.randint(1, 100)}
'''
        elif file_path.endswith('.md'):
            content = f'''# Documentation Update (Commit {i})
            
**Date**: {commit_date.strftime("%Y-%m-%d")}
            
## Changes
- {'Added' if i % 2 == 0 else 'Updated'} section {i % 5}
- {'Fixed' if i % 4 == 0 else 'Improved'} documentation
'''
        elif file_path.endswith('.yml'):
            content = f'''# CI/CD Configuration
name: Workflow {i}
on: [push, pull_request]
            
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: python -m pytest tests/
'''
        
        # Write to file
        with open(file_path, 'w') as f:
            f.write(content)
        
        # Git operations
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run([
            'git', 
            '-c', 'user.name=Your Name',
            '-c', 'user.email=your@email.com',
            'commit', 
            '--date', date_str,
            '-m', f'{random.choice(["feat", "fix", "docs", "refactor"])}: Commit {i} - {commit_date.strftime("%Y-%m-%d")}'
        ], check=True)
        
        # Progress indicator
        if i % 100 == 0:
            print(f"Created {i} commits")
    
    print("Pushing to GitHub...")
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)

if __name__ == "__main__":
    repo_path = input("Enter full path to your Git repository: ").strip()
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print("Error: Not a Git repository!")
        exit(1)
    
    create_commits(repo_path)