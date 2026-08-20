import os
import shutil

def perform_cleanup():
    print("Performing workspace cleanup and logging...")
    
    # 1. Write the Cinnabar Island notepad
    cinnabar_content = """# Cinnabar Island - Spatial & Narrative Mapping

## Point of Interest Coordinates
- **Pokémon Center:** Located at `(11, 11)` on the main island loop. Serves as a Fly waypoint.
- **Cinnabar Gym:** Located at `(18, 4)`. Currently LOCKED. Gym Leader: Blaine (Volcano Badge #6). Requires the Secret Key to open.
- **Pokémon Mansion:** Entrance located at the northwest corner of Cinnabar Island. Contains the Secret Key required to unlock the Gym.
- **Pokémon Lab:** Located on the western side of the island. 
  - Photo of Dr. Fuji at `(3, 2)`.
  - Email about legendary birds (Articuno, Zapdos, Moltres) at `(1, 4)`.
  - Diary about Eevee at `(0, 3)`.
  - Trade NPC inside.

## Island Layout & Traversal
- Main road is a loop that is open and passable across columns 15 and 19.
- Boundary borders and cliffs mapped to prevent soft-locks.
"""
    
    # Write Cinnabar Island notepad
    cinnabar_path = "notepads/Locations/CinnabarIsland.md"
    os.makedirs(os.path.dirname(cinnabar_path), exist_ok=True)
    with open(cinnabar_path, "w") as f:
        with open(cinnabar_path.replace(".md", ""), "w") as f_ext:
            f.write(cinnabar_content)
            f_ext.write(cinnabar_content)
    print("Logged Cinnabar Island spatial data.")
    
    # 2. Deletions
    files_to_delete = [
        "notepads/Locations/FuchsiaGym",
        "notepads/Locations/SafariZone",
        "notepads/Scratchpad/SafariZone_Route",
        "notepads/Locations/Route16",
        "warp_to_2f.py",
        "step_up.py",
        "test_interact.py",
        "test_stairs_down.py",
        "go_down_stairs.py",
        "escape_and_warp.py"
    ]
    
    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"Deleted obsolete file: {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")
                
    # Also clean pycache files
    pycache = "__pycache__"
    if os.path.exists(pycache):
        try:
            shutil.rmtree(pycache)
            print("Cleaned __pycache__")
        except Exception as e:
            print(f"Error cleaning pycache: {e}")

if __name__ == "__main__":
    perform_cleanup()
