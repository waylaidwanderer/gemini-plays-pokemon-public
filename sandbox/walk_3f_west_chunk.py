import mgba
import time
import os
import shutil

# 1. Dismiss the "Got away safely!" screen
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for fade back to overworld

# 2. Update PokemonMansionB1F.md on disk with correct switch details
b1f_path = "notepads/Locations/PokemonMansionB1F.md"
if os.path.exists(b1f_path):
    try:
        with open(b1f_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        old_text = "However, we do not need to toggle any switch on B1F to retrieve the Secret Key! The entire mansion is solved by toggling the Mewtwo statue switch at (2, 11) on 3F West, dropping down the 3F East pitfall at (26, 6) to 1F East (25, 6), warping down to B1F East (22, 3), and walking straight across Row 5 through the open Column 9 gate directly to the Secret Key room on B1F West."
        new_text = "The Mewtwo statue switch at (8, 10) on B1F West is functional and can be used to toggle the mansion layout (e.g. to State B). Toggling this B1F West switch is extremely useful if the player enters B1F East in State A and needs to open the Row 5 Column 9 shutter gate to reach B1F West North and the Secret Key room."
        content = content.replace(old_text, new_text)
        
        with open(b1f_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated PokemonMansionB1F.md with verified B1F switch logic.")
    except Exception as e:
        print(f"Error updating B1F notepad: {e}")

# 3. Clean up obsolete files from sandbox/
obsolete_files = [
    "enter_actual_mansion.py",
    "probe_1f_west.py",
    "probe_1f_west_left.py",
    "probe_1f_west_middle.py",
    "warp_to_2f_west.py",
    "warp_to_3f_west.py"
]
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

# Clean up any residual __pycache__ directories
pycache_dir = "__pycache__"
if os.path.exists(pycache_dir):
    try:
        shutil.rmtree(pycache_dir)
        print("Cleaned up __pycache__ directory.")
    except Exception as e:
        print(f"Error cleaning __pycache__: {e}")

# 4. Walk from (7, 11) on 3F West to (11, 6) on 3F West (Row 6 crossing to 3F East)
steps = [
    ("Left", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
    ("Left", {"x": 4, "y": 11}),
    ("Left", {"x": 3, "y": 11}),
    ("Left", {"x": 2, "y": 11}),
    ("Left", {"x": 1, "y": 11}),
    ("Up", {"x": 1, "y": 10}),
    ("Up", {"x": 1, "y": 9}),   # Open gate in State B!
    ("Up", {"x": 1, "y": 8}),
    ("Up", {"x": 1, "y": 7}),
    ("Up", {"x": 1, "y": 6}),
    ("Right", {"x": 2, "y": 6}),
    ("Right", {"x": 3, "y": 6}),
    ("Right", {"x": 4, "y": 6}),
    ("Right", {"x": 5, "y": 6}),
    ("Right", {"x": 6, "y": 6}),
    ("Right", {"x": 7, "y": 6}),
    ("Right", {"x": 8, "y": 6}),
    ("Right", {"x": 9, "y": 6}),
    ("Right", {"x": 10, "y": 6}),
    ("Right", {"x": 11, "y": 6}),
]

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (11, 6) on 3F West successfully!")
else:
    print("Failed to reach (11, 6).")
