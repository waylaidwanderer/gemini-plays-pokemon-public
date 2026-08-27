import mgba
import time
import os

# 1. Escape from battle
print("Dismissing 'Wild KOFFING appeared!' text...")
mgba.press_buttons(["B"])
time.sleep(1.2)

print("Selecting RUN...")
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
time.sleep(1.5)

print("Dismissing 'Got away safely!'...")
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Position after escaping battle:", pos)

# 2. Cleanup of notepads according to Overwatch instructions
switch_matrix_path = "notepads/Scratchpad/Switch_Matrix"
if os.path.exists(switch_matrix_path):
    with open(switch_matrix_path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
    
    # Let's filter out the incorrect / contradictory claims on lines 120-125
    # Let's see the lines first by printing them to understand what we're editing
    print("\n--- Editing Switch_Matrix ---")
    new_lines = []
    skip = False
    for i, line in enumerate(lines):
        # Remove Primary/Secondary Switch Statue lines around lines 120-125
        if "## Verified 3F West Switch Statue Coordinates (Updated Turn 61084)" in line or "Primary Switch Statue" in line or "Secondary Switch Statue" in line:
            print(f"Removing line {i+1}: {line.strip()}")
            continue
        if "Standing Position: Stand at `(1, 13)`" in line or "Collision Obstacle" in line or "Bypass Route" in line:
            print(f"Removing line {i+1}: {line.strip()}")
            continue
        # Remove outdated turn logs of failed switch attempts (lines 108-116 in original file)
        if "## Verified Parity Log (Turn-Stamped)" in line or "Turn 58747" in line:
            print(f"Removing line {i+1}: {line.strip()}")
            continue
        new_lines.append(line)
        
    with open(switch_matrix_path, "w", encoding="utf-8") as fh:
        fh.writelines(new_lines)
    print("Switch_Matrix updated!")

b1f_path = "notepads/Locations/PokemonMansionB1F"
if os.path.exists(b1f_path):
    with open(b1f_path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
    
    print("\n--- Editing PokemonMansionB1F ---")
    new_lines = []
    for i, line in enumerate(lines):
        # Remove the claim that B1F West SOUTH statues contain switches
        if "B1F East has Mewtwo statues" in line or "B1F West SOUTH" in line:
            # We replace or remove it
            print(f"Modifying line {i+1}: {line.strip()}")
            # We replace it with the verified info that B1F has NO switches
            line = "- **No Switches on B1F:** The Mewtwo statues on B1F are purely decorative and do not contain switches. Toggling must be done from 3F West.\n"
        new_lines.append(line)
        
    with open(b1f_path, "w", encoding="utf-8") as fh:
        fh.writelines(new_lines)
    print("PokemonMansionB1F updated!")

# 3. Clean up other obsolete files
print("\n--- Cleaning up obsolete files on disk ---")
obsolete_files = [
    'walk_to_2_11.py',
    'test_warp.py',
    'test_warp_state_b.py',
    'test_east.py',
    'test_right.py',
    'battle_and_cleanup.py',
    'battle_escape.py'
]
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")
            
    # Also clean pycache for these
    pycache_dir = "__pycache__"
    if os.path.exists(pycache_dir):
        base = os.path.splitext(f)[0]
        for pyc in os.listdir(pycache_dir):
            if pyc.startswith(base) and pyc.endswith(".pyc"):
                path = os.path.join(pycache_dir, pyc)
                try:
                    os.remove(path)
                    print(f"Deleted cached pyc: {path}")
                except Exception as e:
                    print(f"Error deleting {path}: {e}")
                    
print("Cleanup and battle escape complete!")
