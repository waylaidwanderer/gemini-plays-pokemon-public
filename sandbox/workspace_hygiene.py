import os

def update_safari_zone_md():
    path = "notepads/Locations/SafariZone.md"
    if not os.path.exists(path):
        print(f"Error: {path} does not exist.")
        return False
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if barriers are already documented
    if "Row 9 Tree Wall" in content:
        print("Barriers already documented in SafariZone.md.")
        return True
        
    # Let's append our newly verified physical boundaries to the Area 3 section
    search_str = "### 🔍 Verified Area 3 (West) Landmarks & Paths"
    new_barriers = """### 🔍 Verified Area 3 (West) Landmarks & Paths
- **Column 11 Tree Wall (Rows 1-7):** Solid vertical line of pine trees on Column 11, Rows 1-7, completely blocking horizontal ground-level passage in the north-middle.
- **Column 18 Vertical Barrier (Rows 20-23):** Solid tree/wall structure running vertically on Column 18 across Rows 20-23, blocking horizontal ground-level passage.
- **Row 9 Tree Wall (Columns 22-29):** Solid, continuous horizontal barrier of trees on Row 9, Columns 22-29, blocking all downward ground-level vertical passage on the east side of Area 3 (West).
- **Row 8 Column 12 Pond Shoreline Block:** The pond shoreline cliff corner blocks Row 8, Column 12, preventing downward ground-level vertical passage past Row 7 on Column 12.
- **Row 8 Column 21 Pond Shoreline Block:** The pond shoreline cliff corner blocks Row 8, Column 21, preventing downward ground-level vertical passage past Row 7 on Column 21."""

    if search_str in content:
        content = content.replace(search_str, new_barriers)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully updated Locations/SafariZone.md with new barriers.")
        return True
    else:
        print("Could not find search string in Locations/SafariZone.md.")
        return False

def update_progression_stats():
    path = "notepads/Progression_And_Party_Stats.md"
    if not os.path.exists(path):
        print(f"Error: {path} does not exist.")
        return False
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Let's replace the entire "Active Safari Zone Session" section programmatically
    # We find where it starts and overwrite to the end of the file
    marker = "## Active Safari Zone Session (Start Turn: 35311)"
    idx = content.find(marker)
    if idx == -1:
        print("Could not find Active Safari Zone Session marker in Progression_And_Party_Stats.")
        return False
        
    header_content = content[:idx]
    new_session_section = """## Active Safari Zone Session (Start Turn: 35311)
- **Start Turn:** 35311
- **Current Turn:** 35401
- **Steps Used:** 117
- **Steps Remaining:** 383
- **Current Location:** Safari Zone Area 3 (West) at (24, 8)
- **Session Goals:** Execute the sequential speedrun route to obtain the Gold Teeth and Surf.
- **Empirical Refutations:**
  - Bypassed the Central Plateau entirely. Verified Column 28 is 100% walkable and NOT blocked by trees on Turn 35165. This saved 22 steps.
  - Verified Column 27 Row 24 contains a solid signpost, which blocks direct horizontal crossing from (26, 24) on the ground.
  - Verified Column 23 on Row 24 can be traversed UP to Row 22/23 because there is no ledge line there.
  - Safely escaped battles using the refined sequential speedrun script.
  - Verified Column 11 has a solid Tree Wall on Rows 1-7 in Area 3 (West), blocking Row 1-7 horizontal crossing.
  - Verified Column 18 has a solid Vertical Barrier on Rows 20-23 in Area 3 (West).
  - Verified Column 21 at Row 8 has a pond shoreline block in Area 3 (West).
  - Verified Column 12 at Row 8 has a pond shoreline block in Area 3 (West).
  - Verified Row 9 has a solid Tree Wall on Columns 22-29 in Area 3 (West).
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(header_content + new_session_section)
    print("Successfully updated Progression_And_Party_Stats programmatically.")
    return True

def delete_redundant_files():
    files_to_delete = [
        "continue_safari_from_10_10.py",
        "continue_safari_from_21_7.py",
        "continue_safari_from_33_31.py"
    ]
    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"Deleted defunct script: {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")
        else:
            print(f"Defunct script {f} already cleaned up.")

def clean_scratchpad_route():
    path = "notepads/Scratchpad/SafariZone_Route.md"
    if not os.path.exists(path):
        return
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Remove unverified column 21 or 23 routing downwards
    old_str = "Walk Down Column 21 to (21, 18)"
    if old_str in content:
        content = content.replace(old_str, "Column 21 is blocked at Row 8 by the pond shore cliff, so we cannot walk DOWN Column 21 directly.")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Cleaned up unverified steps in Scratchpad/SafariZone_Route.md.")

if __name__ == "__main__":
    update_safari_zone_md()
    update_progression_stats()
    delete_redundant_files()
    clean_scratchpad_route()
