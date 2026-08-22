import mgba
import time
import os

# Clean up obsolete files
obsolete_files = ['cleanup.py', 'dig_out.py', 'get_key_victory_final.py', 'CinnabarIsland']
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Cleaned up obsolete file: {f}")
        except Exception as e:
            print(f"Error removing {f}: {e}")

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    # First mash B to clear any text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Flee sequence
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_to_local(tx, ty):
    pos = mgba.get_coordinates()
    print(f"Walking to ({tx}, {ty}) from {pos}...")
    attempts = 0
    while (pos['x'] != tx or pos['y'] != ty) and attempts < 40:
        dx = tx - pos['x']
        dy = ty - pos['y']
        
        # Prioritize horizontal or vertical based on larger distance
        if abs(dx) >= abs(dy) and dx != 0:
            d = "Left" if dx < 0 else "Right"
        else:
            d = "Up" if dy < 0 else "Down"
            
        pos_before = pos
        mgba.press_buttons([d])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        
        if pos == pos_before:
            print(f"Bumped at {pos} going {d} towards ({tx}, {ty})")
            time.sleep(0.3)
            pos = mgba.get_coordinates()
            if pos == pos_before:
                handle_battle()
                pos = mgba.get_coordinates()
        attempts += 1
    return pos['x'] == tx and pos['y'] == ty

# Starting at (10, 18) on 2F West (State A)
pos = mgba.get_coordinates()
print("Starting definitive Mansion Victory Part 2 from 2F West:", pos)

if pos['x'] == 10 and pos['y'] == 18:
    print("--- STEP 1: WALKING TO 2F EAST ALTERNATE STAIRS AT (19, 8) ---")
    path_to_stairs = [
        # Walk UP Column 10 to Row 10
        (10, 17), (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11), (10, 10),
        # Walk RIGHT along Row 10 to Column 12 on 2F East
        (11, 10), (12, 10),
        # Walk UP Column 12 to Row 6
        (12, 9), (12, 8), (12, 7), (12, 6),
        # Walk RIGHT along Row 6 to Column 19
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6),
        # Walk DOWN Column 19 to Row 8 (onto stairs)
        (19, 7), (19, 8),
    ]
    for target in path_to_stairs:
        tx, ty = target
        if not walk_to_local(tx, ty):
            print(f"Failed to reach stairs at ({tx}, {ty})")
            exit()
            
    print("Stepping DOWN to enter alternate stairs and go UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)

pos = mgba.get_coordinates()
print("Position on next floor after climbing stairs (expected on 3F East):", pos)
mgba.take_screenshot()
