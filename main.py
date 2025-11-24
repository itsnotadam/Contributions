import os
import random
import subprocess
from datetime import datetime, timedelta

def main():
    print("🎲 Random Commit Graph Generator")
    
    # Get basic user input
    num_commits = int(input("How many commits? (default: 200): ") or "200")
    filename = input("File to modify (default: data.txt): ") or "data.txt"
    
    # NEW: Date selection mode
    print("\n📅 Date Selection Mode:")
    print("1. Random dates in past year")
    print("2. Specific date range")
    print("3. Exact specific dates")
    
    date_mode = input("Choose mode (1-3, default: 1): ").strip() or "1"
    
    # Variables for different modes
    start_date = end_date = None
    specific_dates = []
    date_range_days = 0
    
    if date_mode == "2":
        # Mode 2: Date range
        print("\nEnter date range (YYYY-MM-DD format):")
        try:
            start_str = input("Start date: ").strip()
            end_str = input("End date: ").strip()
            
            start_date = datetime.strptime(start_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_str, "%Y-%m-%d")
            
            if start_date > end_date:
                print("❌ Error: Start date must be before end date!")
                return
                
            date_range_days = (end_date - start_date).days
            if date_range_days < 1:
                print("❌ Error: Date range too small!")
                return
                
            print(f"✓ Using range: {start_str} to {end_str}")
            
        except ValueError:
            print("❌ Error: Invalid date format! Use YYYY-MM-DD")
            return
    
    elif date_mode == "3":
        # Mode 3: Exact dates
        print("\nEnter exact dates (YYYY-MM-DD, comma-separated):")
        print("Example: 2024-01-15,2024-02-20,2024-03-10")
        
        try:
            dates_input = input("Dates: ").strip()
            if not dates_input:
                print("❌ Error: No dates provided!")
                return
                
            date_strings = [d.strip() for d in dates_input.split(",")]
            specific_dates = [datetime.strptime(d, "%Y-%m-%d") for d in date_strings]
            
            if len(specific_dates) == 0:
                print("❌ Error: No valid dates!")
                return
                
            if num_commits > len(specific_dates):
                print(f"⚠️  Warning: {num_commits} commits > {len(specific_dates)} dates. Dates will be reused.")
            
            print(f"✓ Using {len(specific_dates)} specific dates")
            
        except ValueError:
            print("❌ Error: Invalid date format! Use YYYY-MM-DD")
            return
    
    print(f"\n📌 Creating {num_commits} commits...")
    
    for i in range(num_commits):
        # Generate commit date based on mode
        if date_mode == "1":
            # Random date in past year
            days_ago = random.randint(1, 365)
            hours_ago = random.randint(0, 23)
            minutes_ago = random.randint(0, 59)
            commit_date = datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
        
        elif date_mode == "2":
            # Random date within specified range
            random_days = random.randint(0, date_range_days)
            random_seconds = random.randint(0, 86399)
            commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
        
        elif date_mode == "3":
            # Pick a specific date and add random time
            base_date = random.choice(specific_dates)
            commit_date = base_date.replace(
                hour=random.randint(0, 23),
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
        
        # Create commit
        with open(filename, "a") as f:
            f.write(f"Commit {i+1} at {commit_date}\n")
        
        subprocess.run(["git", "add", filename], capture_output=True)
        
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(["git", "commit", "-m", f"Commit #{i+1}"], env=env, capture_output=True)
        print(f"[{i+1}/{num_commits}] {commit_date.strftime('%Y-%m-%d %H:%M')}")
    
    # Push
    print("\n⬆️  Pushing to GitHub...")
    subprocess.run(["git", "push"], capture_output=True)
    print("✅ Done! Check your GitHub graph.")

if __name__ == "__main__":
    main()
