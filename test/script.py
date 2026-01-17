from pathlib import Path # Path module for filesystem paths

current_dir = Path.cwd()   # Get the current working directory == Path("/workspaces/data-engineering-zoomcamp2026/test")
current_file = Path(__file__).name

print(f"Files in {current_dir}:") # Print the current directory path

for filepath in current_dir.iterdir(): # Iterate over each item in the current directory
    if filepath.name == current_file: # Skip if the item is the current script file
        continue

    print(f"  - {filepath.name}") # Print the name of the item

    if filepath.is_file(): # Check if the item is a file, because directories don't have content to read
        content = filepath.read_text(encoding='utf-8') # Read the file content with UTF-8 encoding
        print(f"    Content: {content}")