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

# 1. We are currently in battle on turn 58275! Flee!
print("Fleeing from wild Grimer...")
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 3000"])
mgba.press_buttons(["B", "sleep 600"])
print("Overworld position:", get_pos())

# 2. Walk to (1, 11) via (1, 13) and (2, 13)
# Currently we are at (2, 11) or (2, 10).
if not walk_to_clean(2, 13): sys.exit(1)
if not walk_to_clean(1, 13): sys.exit(1)
if not walk_to_clean(1, 11): sys.exit(1)

# Now we are standing at (1, 11) facing UP.
# 3. Face RIGHT and IMMEDIATELY press A to open dialogue before walking!
print("Tapping RIGHT and immediately pressing A...")
mgba.press_buttons(["Right", "sleep 30", "A", "sleep 1200"])

# Check if dialogue is open by verifying if we are still at (1, 11)
pos_after_toggle = get_pos()
print("Position after A press:", pos_after_toggle)

if pos_after_toggle == {'x': 1, 'y': 11}:
    print("SUCCESS! Standing at (1, 11) and dialogue opened! Toggling...")
    mgba.press_buttons(["A", "sleep 1200"]) # Dialogue: "Press it?" -> Select YES
    mgba.press_buttons(["A", "sleep 1200"]) # Dialogue: "Who wouldn't?" -> Close
    mgba.press_buttons(["B", "sleep 500"])  # Close dialogue
    print("State B toggled successfully!")
    
    # Walk UP Column 1 to Row 6 (since State B is now active, Row 9 gate is open!)
    if not walk_to_clean(1, 6): sys.exit(1)
    
    # Walk RIGHT along Row 6 to Column 26
    if not walk_to_clean(26, 6): sys.exit(1)
    
    # Step onto pitfall
    print("Stepping onto pitfall...")
    mgba.press_buttons(["Right", "sleep 2500"])
    print("SUCCESS! Landing position:", get_pos())
    mgba.take_screenshot()
else:
    print("FAILED! Player walked onto (2, 11) instead of turning in place!")
    sys.exit(1)
