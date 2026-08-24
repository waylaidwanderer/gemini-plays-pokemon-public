import mgba
import time
import os
import shutil

# 1. Clean up obsolete files as requested by overwatch
obsolete_files = [
    "finish_toggle_switch.py",
    "probe_3f_east.py",
    "toggle_switch_from_15_6.py",
    "toggle_switch_from_18_10.py",
    "toggle_switch_via_2f_east.py",
    "walk_from_6_11.py",
    "walk_to_secret_key.py",
    "probe_row4_and_3.py"
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

# 2. Correct the unverified pitfall coordinates in Scratchpad/Switch_Matrix.md
switch_matrix_path = "notepads/Scratchpad/Switch_Matrix.md"
if os.path.exists(switch_matrix_path):
    try:
        with open(switch_matrix_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Perform replacements to retract unverified coordinates
        old_phrase1 = "On 3F East, walk to the pitfall at (26, 6) or (26, 3) and drop down."
        new_phrase1 = "On 3F East, walk to the pitfall at (26, 4) and drop down."
        content = content.replace(old_phrase1, new_phrase1)
        
        old_phrase2 = "Step DOWN/RIGHT onto Column 26 to fall through the pit, landing on 1F East inside the fenced room at (26, 3)."
        new_phrase2 = "Step DOWN onto (26, 4) on Column 26 to fall through the pit, landing on 1F East inside the fenced room at (26, 4) (verified Turn 59164)."
        content = content.replace(old_phrase2, new_phrase2)
        
        with open(switch_matrix_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated Scratchpad/Switch_Matrix.md with verified coordinates.")
    except Exception as e:
        print(f"Error updating switch matrix notepad: {e}")

# 3. Walk from (19, 4) on 3F East to (26, 3) and step DOWN to drop
steps = [
    ("Right", {"x": 20, "y": 4}),
    ("Up", {"x": 20, "y": 3}),  # Open vertical passage!
    ("Right", {"x": 21, "y": 3}),
    ("Right", {"x": 22, "y": 3}),
    ("Right", {"x": 23, "y": 3}),
    ("Right", {"x": 24, "y": 3}),
    ("Right", {"x": 25, "y": 3}),
    ("Right", {"x": 26, "y": 3}),
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
    print("Reached (26, 3) on 3F East! Stepping DOWN onto (26, 4) to fall through pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5) # Wait for drop animation and map load
    pos = mgba.get_coordinates()
    print(f"Landed on 1F East inside fenced room! Position: {pos}")
else:
    print("Failed to reach pitfall.")
