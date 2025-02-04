import os
from datetime import datetime, timedelta
import subprocess

def fix_contributions(repo_path):
    os.chdir(repo_path)
    
    # 1. Ensure we're on default branch (usually main/master)
    default_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
    
    # 2. Create real commits with proper email/name
    for day in range(1, 51):
        commit_date = (datetime.now() - timedelta(days=50-day)).strftime('%Y-%m-%d 12:00:00')
        
        # Create meaningful content
        with open(f"contribution_{day}.txt", "w") as f:
            f.write(f"Commit #{day} for GitHub contributions\n")
            f.write(f"Date: {commit_date}\n")
        
        # Stage and commit with proper dates
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run([
            'git', '-c', 'user.name=YourName',
            '-c', 'user.email=your-verified-email@example.com',
            'commit', '--date', commit_date,
            '-m', f"feat: Add contribution #{day}"
        ], check=True)
    
    # 3. Push to default branch
    subprocess.run(['git', 'push', 'origin', default_branch], check=True)

if __name__ == "__main__":
    repo_path = input("Enter repository path: ").strip()
    if not os.path.exists(os.path.join(repo_path, ".git")):
        print("Error: Not a Git repository!")
        exit(1)
    
    fix_contributions(repo_path)
    print("Commits pushed. Wait ~24h for GitHub to update contributions graph.")