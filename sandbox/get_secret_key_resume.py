import mgba
import sys
import os

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    mgba.press_buttons(["sleep 2000"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
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
            mgba.press_buttons(["sleep 150"])
            pos_now = get_pos()
            if pos_now == pos_before:
                run_from_battle()
        steps += 1
    return False

# Currently at (6, 10) on 3F West in State A
print("PHASE 1: Walking to (1, 11) via Row 13 to avoid the statue...")
if not walk_to(6, 13): sys.exit(1)
if not walk_to(1, 13): sys.exit(1)
if not walk_to(1, 11): sys.exit(1)

# Face RIGHT
print("PHASE 2: Facing RIGHT towards switch...")
mgba.press_buttons(["Right", "sleep 500"])

# Toggle Mewtwo switch to State B (Exactly 3 A's and 1 B, 1500ms sleeps)
print("PHASE 3: Toggling the switch at (2, 11) facing Right...")
mgba.press_buttons(["A", "sleep 1500"]) # "A secret switch!"
mgba.press_buttons(["A", "sleep 1500"]) # "Press it?" (Yes/No appears)
mgba.press_buttons(["A", "sleep 1500"]) # Select YES -> "(click)"
mgba.press_buttons(["B", "sleep 500"])  # Close dialogue box

print("Mansion should be in State B. Walking to 3F East pitfall...")
if not walk_to(1, 13): sys.exit(1)
if not walk_to(6, 13): sys.exit(1)
if not walk_to(6, 8): sys.exit(1)
if not walk_to(5, 8): sys.exit(1)
if not walk_to(5, 6): sys.exit(1)
if not walk_to(26, 6): sys.exit(1)

# Drop through pitfall to 1F East inside fenced room
print("PHASE 4: Dropping through 3F pitfall to 1F East...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East fenced room):", get_pos())

# Navigate to B1F stairs
print("PHASE 5: Walking to B1F stairs...")
if not walk_to(26, 3): sys.exit(1)
if not walk_to(22, 3): sys.exit(1)
if not walk_to(22, 2): sys.exit(1)

print("Stepping UP to warp down to B1F East...")
mgba.press_buttons(["Up", "sleep 2500"])
print("Position on B1F East (should be around 22, 3):", get_pos())

# Cross horizontally to Secret Key on B1F West
print("PHASE 6: Walking to B1F West Secret Key room...")
if not walk_to(21, 3): sys.exit(1)
if not walk_to(21, 5): sys.exit(1)
if not walk_to(1, 5): sys.exit(1)

# Retrieve Secret Key at (1, 4)
print("PHASE 7: Retrieving the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"]) # Click item ball
mgba.press_buttons(["A", "sleep 1000"]) # Confirm "ACE found SECRET KEY!"
mgba.press_buttons(["A", "sleep 1000"]) # "ACE put the SECRET KEY in the KEY ITEMS pocket!"
mgba.press_buttons(["B", "sleep 400"])  # Close potential menu

print("Secret Key retrieved! Current position:", get_pos())

# DIG out back to Cinnabar Island
print("PHASE 8: Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 400"])
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"]) # Select POKEMON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 180"])
mgba.press_buttons(["A", "sleep 600"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 3000"]) # Select DIG
print("SUCCESS! Final position Cinnabar Island:", get_pos())
mgba.take_screenshot()
