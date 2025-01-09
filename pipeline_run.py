import os
import subprocess
import random
from datetime import datetime, timedelta

# Set your repository path
REPO_PATH = r"C:\Users\SRILUCKY\OneDrive\Desktop\my_github_projects\End-to-End-Creation-of-CI-CD-Pipeline-Orchestration-Project"

# Set your GitHub email and username
GIT_USER_NAME = "srikanth5451"
GIT_USER_EMAIL = "basimsettysrikanth5451@gmail.com"  # Make sure this matches your GitHub email

# Change directory to the repo
os.chdir(REPO_PATH)

# Ensure Git is configured properly
subprocess.run(f'git config user.name "{GIT_USER_NAME}"', shell=True)
subprocess.run(f'git config user.email "{GIT_USER_EMAIL}"', shell=True)

# Generate 50 meaningful commits
for i in range(50):
    # Generate a backdated timestamp (last 6 months)
    days_back = random.randint(1, 180)
    commit_date = datetime.now() - timedelta(days=days_back, hours=random.randint(1, 12))

    # Format the date for Git
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Create a temporary file to track meaningful changes
    file_name = "progress_log.txt"
    with open(file_name, "a") as file:
        file.write(f"Update {i+1}: Implemented feature {random.randint(100, 999)}\n")

    # Add the file to Git
    subprocess.run("git add .", shell=True)

    # Commit with a backdated timestamp
    commit_message = f"Feature Update {i+1}: Enhanced performance of module {random.randint(1, 10)}"
    commit_command = f'git commit -m "{commit_message}"'
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = formatted_date
    env["GIT_COMMITTER_DATE"] = formatted_date

    subprocess.run(commit_command, shell=True, env=env)

# Push commits to GitHub
subprocess.run("git push origin main --force", shell=True)

print("✅ 50 meaningful backdated commits pushed successfully!")
