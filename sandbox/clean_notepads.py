import os

def clean_file(path, old_text, new_text):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_text in content:
            content = content.replace(old_text, new_text)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully cleaned: {path}")
        else:
            print(f"Old text not found in: {path}")
    else:
        print(f"Path does not exist: {path}")

# 1. Clean notepads/Scratchpad/SafariZone_Route.md
route_path = "notepads/Scratchpad/SafariZone_Route.md"
if os.path.exists(route_path):
    with open(route_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # We want to keep the header and clear the old step log.
    # Let's see what is inside the file.
    print(f"--- {route_path} current content ---")
    print("".join(lines[:15]))
    print("-------------------------------------")

# 2. Clean notepads/Locations/SafariZone.md
zone_path = "notepads/Locations/SafariZone.md"
if os.path.exists(zone_path):
    with open(zone_path, 'r', encoding='utf-8') as f:
        print(f"--- {zone_path} current content ---")
        print(f.read()[:500])
        print("-------------------------------------")
