import os
from datetime import datetime

# List of directories with README files
directories = ["frontend", "backend1", "backend2", "db"]

# Create or update README.md in each directory
def update_readme(directory):
    readme_path = os.path.join(directory, "README.md")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_line = f"\n<!-- Updated on {timestamp} -->\n"

    # Ensure directory exists
    if not os.path.isdir(directory):
        print(f"Skipping {directory}: directory not found.")
        return

    # Append or create the README.md
    try:
        with open(readme_path, "a") as f:
            f.write(update_line)
        print(f"Updated {readme_path}")
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")

if __name__ == "__main__":
    for dir_name in directories:
        update_readme(dir_name)
