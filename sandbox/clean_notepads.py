import os

def clean_pokemon_mansion_1f():
    path = "notepads/Locations/PokemonMansion1F.md"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean incorrect landing line
    old_line = "- **Southern Area Access:** Taking the stairs down from 2F West at (7, 10) lands the player at (7, 11) on 1F West (in the southern half of 1F West)."
    # Check if this line is in content
    if old_line in content:
        print("Found incorrect line in 1F West layout. Keeping the correct one.")
    else:
        print("Incorrect line not found or already clean.")

    # Let's write the verified (22, 7) stairs on 1F East
    addition = """
## B1F East Stairs (Verified Turn 69328)
- **Location:** (22, 7) on 1F East is the active staircase leading DOWN to B1F East (landing at 22, 7 on B1F East).
- **Proof:** Standing at (22, 7) on 1F East and stepping ONTO it warps the player to B1F East on Turn 69328.
"""
    if "## B1F East Stairs (Verified Turn 69328)" not in content:
        content += addition
        print("Added B1F East Stairs verified coordinates to 1F East.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def clean_pokemon_mansion_2f():
    path = "notepads/Locations/PokemonMansion2F.md"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove the contradictory speculative line:
    # "- **Row 11 Open Gates:** Shutter gates on Row 11 are open in State A, allowing horizontal connection between 2F East and 2F West."
    content = content.replace("- **Row 11 Open Gates:** Shutter gates on Row 11 are open in State A, allowing horizontal connection between 2F East and 2F West.", "")
    
    # Correct Row 11 information
    content = content.replace("allowing horizontal connection between 2F East and 2F West.", "")

    # Document the Southwest staircase warp landing
    warp_info = """
## Southwest Staircase Warp Connections
- **Staircase (5, 10) on 3F West:** Warps DOWN to 2F West, landing at (5, 11) on 2F West.
- **Staircase on 2F West:** The staircase at (5, 10) on 2F West leads DOWN to 1F West, landing at (5, 11) on 1F West.
"""
    if "## Southwest Staircase Warp Connections" not in content:
        content += warp_info
        print("Added Southwest Staircase Warp Connections to 2F.")

    # Document Row 2 walkability boundaries
    row2_info = """
## Row 2 Walkability Boundaries
- **State B Corridor:** Row 2 on 2F is completely open and passable horizontally (Columns 5-12). However, on 2F East, a solid obstruction blocks horizontal travel past Column 14.
"""
    if "## Row 2 Walkability Boundaries" not in content:
        content += row2_info
        print("Added Row 2 Walkability Boundaries to 2F.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def clean_pokemon_mansion_3f():
    path = "notepads/Locations/PokemonMansion3F.md"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    warp_info = """
## Southwest Staircase Warp Connections
- **Staircase (5, 10) on 3F West:** Warps DOWN to 2F West, landing at (5, 11) on 2F West.
"""
    if "## Southwest Staircase Warp Connections" not in content:
        content += warp_info
        print("Added Southwest Staircase Warp Connections to 3F.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def clean_b1f_connection():
    path = "notepads/Scratchpad/B1F_Connection.md"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove '## Southeast Fenced Room B1F Stairs (Active Hypothesis)' and the text after it
    idx = content.find("## Southeast Fenced Room B1F Stairs (Active Hypothesis)")
    if idx != -1:
        content = content[:idx]
        print("Removed outdated 'Southeast Fenced Room B1F Stairs (Active Hypothesis)' section.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    clean_pokemon_mansion_1f()
    clean_pokemon_mansion_2f()
    clean_pokemon_mansion_3f()
    clean_b1f_connection()
    print("Notepad cleanup completed successfully.")
