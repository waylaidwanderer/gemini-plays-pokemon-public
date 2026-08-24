import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting for battle menu to load...")
    time.sleep(2.0) # Wait 2 seconds for battle intro to finish
    # Dismiss any text
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    print("Sending escape inputs...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    # Clear "Got away safely!"
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    print("Escape sequence complete.")

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 200"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 100
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
            
        if x < target_x:
            direction = "Right"
        elif x > target_x:
            direction = "Left"
        elif y < target_y:
            direction = "Down"
        elif y > target_y:
            direction = "Up"
            
        pos_before, pos_after = walk_step(direction)
        
        if pos_before == pos_after:
            time.sleep(0.1)
            pos_now = get_pos()
            if pos_now == pos_before:
                # We are definitely blocked/in battle!
                run_from_battle()
        else:
            print(f"Stepped {direction} to {pos_after}")
            
        steps += 1
    print("Failed to reach target.")
    return False

# Starting inside 3F West at (1, 10) in State B
print("Starting get_secret_key_resume.py from inside Mansion 3F West at (1, 10)...")
print("Initial Position:", get_pos())

# Phase 1: Walk to Column 6 Row 10, then walk UP Column 6 to Row 6
print("PHASE 1: Walking to Column 6 and going Up to Row 6...")
if not walk_to(6, 10): sys.exit(1)
if not walk_to(6, 6): sys.exit(1)

# Phase 2: Walk to 3F East pitfall at (26, 6)
print("PHASE 2: Walking to pitfall at (26, 6)...")
if not walk_to(26, 6): sys.exit(1)
print("Dropped through pitfall! Waiting 2.0 seconds...")
time.sleep(2.0)
print("Position after drop (should be 1F East inside fenced room around 25, 6):", get_pos())

# Walk to B1F stairs on 1F East via Row 3 and warp DOWN
print("PHASE 3: Walking to B1F stairs...")
if not walk_to(26, 3): sys.exit(1)
if not walk_to(21, 3): sys.exit(1)
if not walk_to(21, 2): sys.exit(1)
if not walk_to(22, 2): sys.exit(1)
print("Stepping UP to warp DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 1200"])
print("Position on B1F East:", get_pos())

# Walk along B1F to Secret Key room at (1, 5) bypassing the Row 5 Column 17/18 wall
print("PHASE 4: Crossing B1F Row 6/5 to Secret Key...")
if not walk_to(18, 6): sys.exit(1)
if not walk_to(10, 6): sys.exit(1)
if not walk_to(10, 5): sys.exit(1)
if not walk_to(1, 5): sys.exit(1)

# Retrieve Secret Key at (1, 4)
print("PHASE 5: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 800"]) # Obtained dialogue
mgba.press_buttons(["A", "sleep 800"]) # Clear dialogue
mgba.press_buttons(["B", "sleep 400"]) # Safeguard close
print("Secret Key retrieved! Current position:", get_pos())

# DIG out back to Cinnabar Island
print("PHASE 6: Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 400"])
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"]) # Select POKéMON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 180"])
mgba.press_buttons(["A", "sleep 600"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1500"]) # Select DIG
time.sleep(3.0)

print("SUCCESS! Final position Cinnabar Island:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
