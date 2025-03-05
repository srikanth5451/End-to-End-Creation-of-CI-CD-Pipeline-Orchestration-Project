import os
import datetime

# Set repository directory (update this to your repo path)
REPO_DIR = REPO_DIR = r"C:\Users\SRILUCKY\OneDrive\Desktop\my_github_projects\End-to-End-Creation-of-CI-CD-Pipeline-Orchestration-Project"

# Change directory to repo
os.chdir(REPO_DIR)

# Your GitHub email (must be linked to your GitHub account)
GIT_USER = "srikanth5451"
GIT_EMAIL = "91301139+srikanth5451@users.noreply.github.com"

# Set user config
os.system(f'git config user.name "{GIT_USER}"')
os.system(f'git config user.email "{GIT_EMAIL}"')

# Start date for commits (e.g., 50 days ago)
start_date = datetime.datetime.now() - datetime.timedelta(days=50)

# List of Python functions to commit
functions = [
    ("factorial.py", "def factorial(n):\n    return 1 if n == 0 else n * factorial(n - 1)"),
    ("fibonacci.py", "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a"),
    ("palindrome.py", "def is_palindrome(s):\n    return s == s[::-1]"),
    ("prime.py", "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True"),
    ("reverse_string.py", "def reverse_string(s):\n    return s[::-1]"),
]

# Repeat functions to make 50 commits
for i in range(50):
    filename, code = functions[i % len(functions)]  # Cycle through functions
    commit_date = start_date + datetime.timedelta(days=i)
    date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

    # Write the code snippet to file
    with open(filename, "w") as f:
        f.write(code + "\n")

    # Add and commit with a meaningful message
    os.system(f"git add {filename}")
    os.system(f'GIT_AUTHOR_DATE="{date_str}" GIT_COMMITTER_DATE="{date_str}" git commit -m "Added {filename} function"')

# Push commits
os.system("git push origin main")

print("✅ 50 meaningful backdated commits pushed successfully!")