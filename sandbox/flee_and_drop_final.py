import mgba
import sys
import os
import time

def get_pos():
    return mgba.get_coordinates()

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to_clean(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 40
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
        if x < target_x: direction = "Right"
        elif x > target_x: direction = "Left"
        elif y < target_y: direction = "Down"
        elif y > target_y: direction = "Up"
        pos_before, pos_after = walk_step(direction)
        if pos_before == pos_after:
            # Try a second time (handles turning in place)
            pos_before, pos_after = walk_step(direction)
            if pos_before == pos_after:
                print(f"BLOCKED at {pos_before} when trying to go {direction}!")
                return False
        steps += 1
    return False

# 1. Clean up obsolete files
obsolete_files = [
    "toggle_3f_switch_true.py",
    "toggle_3f_left.py",
    "test_switch_dialogue.py",
    "flee_and_drop_true.py",
    "flee_and_drop_final.py",
    "test_right_a.py",
    "test_warp.py"
]
print("Cleaning up obsolete files...")
for f_name in obsolete_files:
    if os.path.exists(f_name):
        try:
            os.remove(f_name)
            print(f"Deleted {f_name}")
        except Exception as e:
            print(f"Error deleting {f_name}: {e}")

# 2. Update Switch_Matrix notepad
notepad_path = "notepads/Scratchpad/Switch_Matrix"
if os.path.exists(notepad_path):
    print("Updating Switch_Matrix notepad...")
    with open(notepad_path, "r") as f:
        content = f.read()
    
    old_text = "   - On 3F West: walk to `(4, 11)` -> `(4, 13)` -> `(1, 13)` -> `(2, 13)` -> `(2, 12)`.\n   - Stand at `(2, 12)` facing UP towards the Mewtwo statue switch at `(2, 11)` and toggle it to State B! (Select YES)."
    new_text = "   - On 3F West: walk to `(1, 11)` via the Row 13 detour.\n   - Walk RIGHT to `(2, 11)` facing RIGHT towards the switch at `(3, 11)` (visually pink/white floor, but has the trigger) and toggle it to State B by pressing A, A, A, B."
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(notepad_path, "w") as f:
            f.write(content)
        print("Notepad updated successfully!")
    else:
        # Fallback split lines replacement
        lines = content.splitlines()
        replaced = False
        for idx, line in enumerate(lines):
            if "Stand at `(2, 12)` facing UP towards" in line:
                lines[idx] = "   - Stand at `(1, 11)` facing RIGHT towards the switch at `(2, 11)` and toggle it to State B by pressing A, A, A, B."
                replaced = True
        if replaced:
            with open(notepad_path, "w") as f:
                f.write("\n".join(lines))
            print("Notepad partially updated!")

# 3. Flee from wild Ponyta (cursor is at FIGHT)
print("Fleeing from wild Ponyta...")
mgba.press_buttons(["A", "sleep 2500"]) # Advance text box
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 3000"]) # Flee
mgba.press_buttons(["B", "sleep 600"]) # Dismiss "Got away safely!" text
print("Overworld position after fleeing:", get_pos())

# 4. Walk UP Column 6 to (6, 6)
if not walk_to_clean(6, 6): sys.exit(1)

# 5. Walk RIGHT along Row 6 to (26, 6)
if not walk_to_clean(26, 6): sys.exit(1)

# 6. Step RIGHT to drop
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East inside fenced room):", get_pos())
mgba.take_screenshot()
