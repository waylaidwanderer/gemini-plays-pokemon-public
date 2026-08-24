import mgba
import sys

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

print("Starting at:", get_pos())

# 1. Walk down to (2, 13)
if not walk_to_clean(2, 13): sys.exit(1)

# 2. Walk up to (2, 12) (ensures we are facing UP)
if not walk_to_clean(2, 12): sys.exit(1)

# 3. Toggle Mewtwo switch using the exact working sequence from mansion_phase3.py
print("Toggling 3F West switch at (2, 11) to State B...")
mgba.press_buttons(["Up", "sleep 200"]) # Face Up
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "A secret switch!"
mgba.press_buttons(["A", "sleep 800"]) # Dialogue: "Press it?" -> Select YES
mgba.press_buttons(["A", "sleep 500"]) # Dialogue: "Who wouldn't?" -> Close
print("State B activated!")

# 4. Walk to (6, 13) via (2, 13)
if not walk_to_clean(2, 13): sys.exit(1)
if not walk_to_clean(6, 13): sys.exit(1)

# 5. Walk UP Column 6 to (6, 6)
if not walk_to_clean(6, 6): sys.exit(1)

# 6. Walk RIGHT along Row 6 to Column 26
if not walk_to_clean(26, 6): sys.exit(1)

# 7. Drop through pitfall
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East fenced room):", get_pos())
mgba.take_screenshot()
