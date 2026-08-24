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

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 30
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
        steps += 1
    return False

# Starting from current position (2, 12) on 3F West
print("Walking to (1, 11)...")
if not walk_to(1, 12): sys.exit(1)
if not walk_to(1, 11): sys.exit(1)

# Face RIGHT
print("Facing RIGHT...")
mgba.press_buttons(["Right", "sleep 500"])

# Trigger dialogue
print("Triggering dialogue from the LEFT facing RIGHT...")
mgba.press_buttons(["A", "sleep 1500"])
sc1 = mgba.take_screenshot()
print("Dialogue opened. Screenshot 1 saved:", sc1)

# Try pressing A to advance
print("Pressing A to advance...")
mgba.press_buttons(["A", "sleep 1500"])
sc2 = mgba.take_screenshot()
print("After A to advance. Screenshot 2 saved:", sc2)

# Try pressing A to select YES
print("Pressing A to select YES...")
mgba.press_buttons(["A", "sleep 1500"])
sc3 = mgba.take_screenshot()
print("After A to select YES. Screenshot 3 saved:", sc3)

# Close textbox with B
mgba.press_buttons(["B", "sleep 500"])
sc4 = mgba.take_screenshot()
print("After close B. Screenshot 4 saved:", sc4)
