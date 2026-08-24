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

# Starting at (2, 11)
print("Starting at:", get_pos())

# 1. Test if we can walk up to (2, 10) -> (6, 10) -> (6, 6) directly (State B bypass)
print("Attempting to traverse State B bypass to Row 6...")
b_bypass_success = False

if walk_to_clean(2, 10):
    if walk_to_clean(6, 10):
        if walk_to_clean(6, 6):
            b_bypass_success = True

if not b_bypass_success:
    print("Mansion is currently in State A! Walking to (1, 11) to toggle switch...")
    # Walk to (1, 11) via Row 13 detour from our current position
    # (Since we got blocked, we could be at (6, 10) or elsewhere. We walk to (6, 13) first)
    pos = get_pos()
    if pos['y'] < 13:
        if not walk_to_clean(pos['x'], 13): sys.exit(1)
    if not walk_to_clean(1, 13): sys.exit(1)
    if not walk_to_clean(1, 11): sys.exit(1)
    
    # Toggle switch to State B
    print("Toggling switch from (1, 11) facing RIGHT...")
    mgba.press_buttons(["Right", "sleep 250", "A", "sleep 800", "A", "sleep 800", "A", "sleep 500", "B", "sleep 300"])
    print("State B activated! Walking State B bypass route...")
    
    # State B is now active! Walk to (1, 13) -> (2, 13) -> (2, 10) -> (6, 10) -> (6, 6)
    if not walk_to_clean(1, 13): sys.exit(1)
    if not walk_to_clean(2, 13): sys.exit(1)
    if not walk_to_clean(2, 10): sys.exit(1)
    if not walk_to_clean(6, 10): sys.exit(1)
    if not walk_to_clean(6, 6): sys.exit(1)

# Now we are definitely at (6, 6) in State B!
# Walk RIGHT along Row 6 to (26, 6)
if not walk_to_clean(26, 6): sys.exit(1)

# Step onto pitfall
print("Stepping onto pitfall...")
mgba.press_buttons(["Right", "sleep 2500"])
print("SUCCESS! Position after drop:", get_pos())
mgba.take_screenshot()
