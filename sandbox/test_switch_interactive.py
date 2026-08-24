import mgba
import sys
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

# 1. Flee from wild Ponyta (cursor starts at FIGHT)
print("Fleeing from wild Ponyta...")
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 3000"])
# Dismiss "Got away safely!" text
mgba.press_buttons(["B", "sleep 600"])
print("Overworld position after fleeing:", get_pos())

# 2. Walk to (1, 11)
if not walk_to_clean(1, 11): sys.exit(1)

# 3. Turn RIGHT towards (2, 11) and try interacting
print("Turning RIGHT and interacting...")
mgba.press_buttons(["Right", "sleep 300"])
print("Position after turning:", get_pos())

print("Pressing A (1)...")
mgba.press_buttons(["A", "sleep 1200"])
mgba.take_screenshot()

print("Pressing A (2)...")
mgba.press_buttons(["A", "sleep 1200"])
mgba.take_screenshot()

print("Pressing A (3)...")
mgba.press_buttons(["A", "sleep 1200"])
mgba.take_screenshot()

print("Pressing B...")
mgba.press_buttons(["B", "sleep 600"])
mgba.take_screenshot()

print("Switch check complete!")
