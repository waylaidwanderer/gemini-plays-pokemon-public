import os

def clean_and_update():
    print("Starting notepad cleanup and updates...")
    
    # 1. Delete duplicate extensionless files
    files_to_delete = [
        "notepads/Locations/CinnabarIsland",
        "notepads/Locations/FuchsiaGym",
        "notepads/Locations/SafariZone",
        "notepads/Scratchpad/SafariZone_Route"
    ]
    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"Deleted duplicate extensionless file: {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")
                
    # 2. Update notepads/Scratchpad/Switch_Matrix.md
    matrix_path = "notepads/Scratchpad/Switch_Matrix.md"
    if os.path.exists(matrix_path):
        with open(matrix_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # A. Delete the obsolete line
        old_obsolete = "- **Search for True 3F Switch:** Since the east-central statues are decorative, the actual 3F Mewtwo statue switch must be located elsewhere on 3F (likely in the central-western or northwestern rooms near the stairs/bookshelves)."
        if old_obsolete in content:
            content = content.replace(old_obsolete, "")
            print("Deleted obsolete search line from Switch_Matrix.md")
            
        # B. Add 3F switch location under ## Switch Locations
        old_switch_locations = """## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` / `(12, 11)` and `(2, 11)` (northwest diary room).
- **B1F:** Mewtwo statue switch located near the center-left."""
        
        new_switch_locations = """## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` / `(12, 11)` and `(2, 11)` (northwest diary room).
- **3F:** Mewtwo statue switch located at `(2, 11)`, accessed from `(2, 12)` facing Up or `(1, 11)` facing Right.
- **B1F:** Mewtwo statue switch located near the center-left."""
        
        if old_switch_locations in content:
            content = content.replace(old_switch_locations, new_switch_locations)
            print("Added 3F switch location to switch list.")
            
        # C. Add Column 9 wall constraint on 3F with Turn 49004 timestamp and empirical methodology
        rubble_constraint_section = """## Verified 3F Layout Constraints
- **Northeast Columns:** On 3F, columns 18 and 19 on row 8 are blocked by solid columns/machines (empirically verified on Turn 48596).
- **Row 7 Blocked on West:** On 3F, row 7 is physically blocked by rubble across columns 5-9 on the west side, but open across columns 10-14 on the east side.
- **Row 3 Column 18/19 Cabinets:** On 3F, columns 18 and 19 on row 3 are blocked by solid cabinets, separating the west/center from the east.
- **Column 15 Wall:** On 3F, column 15 is physically blocked by a solid brick wall across rows 1-4, preventing horizontal traversal past column 15 on those rows.
- **Row 6 Open Passage:** On 3F, row 6 is wide-open horizontally across columns 11-20, allowing horizontal crossing between the east and west wings.
- **3F Switch Location:** The true Mewtwo statue switch on 3F is located at `(2, 11)`, accessed from `(2, 12)` facing Up or `(1, 11)` facing Right."""

        new_rubble_constraint_section = rubble_constraint_section + "\n- **Column 9 Wall:** On 3F, column 9 is a solid vertical wall from row 0 to row 6. (Empirically verified on Turn 49004 by attempting to walk Left from (10, 3) to (9, 3) and being blocked by a solid wall boundary)."
        
        if rubble_constraint_section in content:
            content = content.replace(rubble_constraint_section, new_rubble_constraint_section)
            print("Logged Column 9 wall constraint on 3F.")
            
        with open(matrix_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # 3. Let's write the turn numbers to Cinnabar Island notepad as requested
    cinnabar_path = "notepads/Locations/CinnabarIsland.md"
    if os.path.exists(cinnabar_path):
        with open(cinnabar_path, "r", encoding="utf-8") as f:
            c_content = f.read()
            
        # Add Turn 49084 for Pokemon Center and Turn 49102/49106 for Loop Road
        old_cinnabar_list = """- **Pokémon Center:** Located at `(11, 11)` on the main island loop. Serves as a Fly waypoint.
- **Cinnabar Gym:** Located at `(18, 4)`. Currently LOCKED. Gym Leader: Blaine (Volcano Badge #6). Requires the Secret Key to open.
- **Pokémon Mansion:** Entrance located at the northwest corner of Cinnabar Island. Contains the Secret Key required to unlock the Gym.
- **Pokémon Lab:** Located on the western side of the island. 
  - Photo of Dr. Fuji at `(3, 2)`.
  - Email about legendary birds (Articuno, Zapdos, Moltres) at `(1, 4)`.
  - Diary about Eevee at `(0, 3)`.
  - Trade NPC inside.

## Island Layout & Traversal
- Main road is a loop that is open and passable across columns 15 and 19.
- Boundary borders and cliffs mapped to prevent soft-locks."""

        new_cinnabar_list = """- **Pokémon Center:** Located at `(11, 11)` on the main island loop. (Verified/visited on Turn 49084 - serves as a Fly and DIG waypoint).
- **Cinnabar Gym:** Located at `(18, 4)`. Currently LOCKED. Gym Leader: Blaine (Volcano Badge #6). Requires the Secret Key to open (verified/visited on Turn 49103).
- **Pokémon Mansion:** Entrance located at `(6, 3)` (with door at (6, 3) and entry from (6, 4) walking UP). (Verified/visited/entered on Turn 49109).
- **Pokémon Lab:** Located on the western side of the island. 
  - West entrance door is at `(3, 7)` / `(3, 8)` (verified on Turn 49088).
  - East entrance door is at `(15, 11)` / `(15, 12)` (verified on Turn 49101).
  - Photo of Dr. Fuji at `(3, 2)` inside Lab (Turn 47975).
  - Email about legendary birds (Articuno, Zapdos, Moltres) at `(1, 4)` (Turn 47975).
  - Diary about Eevee at `(0, 3)` (Turn 47975).
  - Trade NPC inside (Turn 47975).

## Island Layout & Traversal
- Main road is a loop that is open and passable across columns 15 and 19 (empirically mapped on Turn 49102 and Turn 49106).
- Row 12 serves as a horizontal overworld connection between the east side and west side (tested/verified on Turn 49098).
- Column 9 functions as a solid vertical wall boundary on the overworld between row 2 and row 10, separating the Lab yard from the eastern area (Turn 49107).
- Boundary borders and cliffs mapped to prevent soft-locks."""

        if old_cinnabar_list in c_content:
            c_content = c_content.replace(old_cinnabar_list, new_cinnabar_list)
            print("Logged Cinnabar Island turn numbers and spatial discoveries.")
            
        with open(cinnabar_path, "w", encoding="utf-8") as f:
            f.write(c_content)

if __name__ == "__main__":
    clean_and_update()
