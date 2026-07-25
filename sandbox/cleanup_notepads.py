import os

def cleanup_1f():
    path = "notepads/Locations/MtMoon_1F.md"
    if not os.path.exists(path):
        print(f"Path {path} does not exist!")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Remove the incorrect result line
    incorrect_line = "  - **Result:** Rows 30 to 35 are completely open and walkable across column 16, allowing direct horizontal crossing between the western cavern and the eastern cavern!"
    if incorrect_line in content:
        content = content.replace(incorrect_line + "\n", "")
        content = content.replace(incorrect_line, "")
        print("Removed incorrect Result line!")
    else:
        print("Incorrect Result line not found!")
        
    # Modify the Raised Platform line
    old_platform = "  - **Raised Platform (West Side):** Columns 12 and 13 on rows 20 to 28 form an elevated platform."
    new_platform = "  - **Raised Platform (West Side):** Columns 12 and 13 form a solid vertical barrier extending from row 3 down to at least row 28, blocking all horizontal transit on rows 5, 7, 12, 15, and 20-28."
    
    if old_platform in content:
        content = content.replace(old_platform, new_platform)
        print("Updated Raised Platform description!")
    else:
        print("Old Raised Platform line not found!")
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    cleanup_1f()
