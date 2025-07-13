import os
from datetime import datetime
import json

directories = ["frontend", "backend1", "backend2", "db"]

# Create or update README.md in each directory
def update_readme(directory):
    readme_path = os.path.join(directory, "README.md")
    print(f"Processing directory: {directory}")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_line = f"\n<!-- Updated on {timestamp} -->\n"

    if os.path.isdir(directory):
        print(f"Directory {directory} found.")
    else:
        print(f"Skipping {directory}: directory not found.")

    count_file = "count.json"
    if os.path.exists(count_file):
        try:
            with open(count_file, "r") as f:
                count_data = f.read()
            
            # read the value of count
            data = json.loads(count_data) or {} # convert empty string to empty dict
            count = data.get("count", 0)
            count += 1

            with open(count_file, "w") as f:
                json.dump({"count": count}, f)

        except Exception as e:
            print(f"Error reading {count_file}: {e}")
            count = 0
    else:
        print(f"Count file {count_file} not found, initializing count to 0.")
        count = 0

    
    # Append or create the README.md
    try:
        with open(readme_path, "a") as f:
            f.write(update_line)
        print(f"Updated {readme_path}")
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")

    # now git add all the files from current directory
    try:
        os.system(f"git add .")
        print(f"Added all files...")
    except Exception as e:
        print(f"Error adding files to git: {e}")

    try:
        os.system(f"git commit -m 'fix: fixing github ci/cd issues'")
    except Exception as e:
        print(f"Error committing changes due to {e}")

    try:
        os.system(f"git push")
    except Exception as e:
        print(f"Error pushing changes to remote repository: {e}")

if __name__ == "__main__":
    for dir_name in directories:
        update_readme(dir_name)
