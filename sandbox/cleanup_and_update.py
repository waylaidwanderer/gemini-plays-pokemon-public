import shutil
import os

# 1. Delete redundant nested directory
nested_dir = "notepads/notepads"
if os.path.exists(nested_dir):
    shutil.rmtree(nested_dir)
    print(f"Successfully deleted {nested_dir}")
else:
    print(f"{nested_dir} does not exist.")

# 2. Update Locations/FuchsiaCity.md on disk
fuchsia_md_path = "notepads/Locations/FuchsiaCity.md"
if os.path.exists(fuchsia_md_path):
    with open(fuchsia_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove/modify the incorrect ledge statement
    old_phrase = "blocked at Row 25 by a south-facing one-way ledge (you can jump DOWN over Row 25 Column 24, but cannot walk back UP)"
    new_phrase = "completely open and walkable vertically without any ledge or obstacle (verified on Turn 41246)"
    
    if old_phrase in content:
        content = content.replace(old_phrase, new_phrase)
        with open(fuchsia_md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated Locations/FuchsiaCity.md")
    else:
        print("Incorrect ledge statement not found in Locations/FuchsiaCity.md")
else:
    print(f"{fuchsia_md_path} does not exist.")
