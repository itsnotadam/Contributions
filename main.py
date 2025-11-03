import os
import random
import subprocess
from datetime import datetime, timedelta

def main():
    print("🎲 Random Commit Graph Generator")
    
    # Get user input
    num_commits = int(input("How many random commits? (default: 200): ") or "200")
    filename = input("File to modify (default: data.txt): ") or "data.txt"
    
    print(f"\nCreating {num_commits} random commits...")
    
    for i in range(num_commits):
        # Random date in the past year
        days_ago = random.randint(1, 365)
        hours_ago = random.randint(0, 23)
        minutes_ago = random.randint(0, 59)
        
        commit_date = datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
        
        # Modify file
        with open(filename, "a") as f:
            f.write(f"Commit {i+1} at {commit_date}\n")
        
        # Add and commit with specific date
        subprocess.run(["git", "add", filename], capture_output=True)
        
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(["git", "commit", "-m", f"Commit #{i+1}"], env=env, capture_output=True)
        print(f"[{i+1}/{num_commits}] {commit_date.strftime('%Y-%m-%d')}")
    
    # Push
    print("\nPushing to GitHub...")
    subprocess.run(["git", "push"], capture_output=True)
    print("✅ Done! Check your GitHub graph.")

if __name__ == "__main__":
    main()