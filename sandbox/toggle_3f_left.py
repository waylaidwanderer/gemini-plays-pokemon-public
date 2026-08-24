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

print("Starting at overworld position:", get_pos())

# 1. Walk from (6, 10) to (1, 11) via Row 13 detour
if not walk_to_clean(6, 13): sys.exit(1)
if not walk_to_clean(1, 13): sys.exit(1)
if not walk_to_clean(1, 11): sys.exit(1)

# 2. Stand at (1, 11) facing UP. Turn RIGHT towards the solid statue at (2, 11)
print("Turning RIGHT towards switch...")
mgba.press_buttons(["Right", "sleep 300"])
print("Position after turning (should be 1, 11):", get_pos())

# 3. Toggle switch
print("Toggling Mewtwo switch...")
mgba.press_buttons(["A", "sleep 1200"]) # Dialogue: "A secret switch!"
mgba.press_buttons(["A", "sleep 1200"]) # Dialogue: "Press it?" -> Select YES
mgba.press_buttons(["A", "sleep 1200"]) # Dialogue: "Who wouldn't?" -> Close
mgba.press_buttons(["B", "sleep 500"])  # Close dialogue
print("State B toggled!")

# 4. Walk UP Column 1 to Row 6 (since State B is active, Row 9 gate is open!)
if not walk_to_clean(1, 6): sys.exit(1)

# 5. Walk RIGHT along Row 6 to Column 26
if not walk_to_clean(26, 6): sys.exit(1)

# 6. Step onto pitfall
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("SUCCESS! Landing position:", get_pos())
mgba.take_screenshot()
