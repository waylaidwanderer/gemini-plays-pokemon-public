import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting for battle menu to load...")
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    print("Sending escape inputs...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    print("Escape sequence complete.")

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    if pos_before == pos_after:
        print("Blocked/Battle! Attempting run from battle...")
        run_from_battle()
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
        if pos_before == pos_after:
            print(f"Failed step at {pos_before} going {direction}")
            return False
        steps += 1
    return False

print("--- B1F SECRET KEY RETRIEVAL ---")
print("Starting from:", get_pos())

# Dismiss any active text box first (like "Got away safely!")
mgba.press_buttons(["B", "sleep 500"])

# Phase 3: Walk to B1F West Secret Key room bypassing Row 5 Column 20-21 barrier
print("Walking to B1F West Secret Key room...")
if not walk_to(1, 7): sys.exit(1)
if not walk_to(1, 5): sys.exit(1)

print("Facing UP...")
mgba.press_buttons(["Up", "sleep 450"])
print("Retrieving Secret Key...")
mgba.press_buttons(["A", "sleep 1200"]) # Obtained dialogue
mgba.press_buttons(["A", "sleep 1200"]) # Clear dialogue
mgba.press_buttons(["B", "sleep 400"]) # Safeguard close
print("Secret Key retrieved successfully! Current position:", get_pos())

# Phase 4: Escape via DIG back to Cinnabar Island
print("Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 600"])
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 800"]) # POKéMON menu
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 600"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 2500"]) # Select DIG
print("Quest complete! Final position:", get_pos())
