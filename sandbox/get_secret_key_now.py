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
    max_steps = 40
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

print("Starting get_secret_key_now.py (State B start)...")
print("Initial Position:", get_pos())

# Step 1: Walk to (10, 5)
if not walk_to(10, 5):
    sys.exit(1)

# Step 2: Walk to (1, 5)
if not walk_to(1, 5):
    sys.exit(1)

# Step 3: Face Up to retrieve key
print("Arrived at (1, 5)! Facing UP to retrieve Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 200"])
mgba.press_buttons(["A", "sleep 800"])
screenshot_path = mgba.take_screenshot()
print("Took screenshot of key retrieval:", screenshot_path)

# Clear dialogue
mgba.press_buttons(["A", "sleep 800"])
mgba.press_buttons(["A", "sleep 800"])
mgba.press_buttons(["B", "sleep 500"])
print("Key retrieved. Current Position:", get_pos())

# Step 4: Escape via DIG
print("Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 300"])
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 600"]) # Select POKéMON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 500"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1000"]) # Select DIG
time.sleep(3.0)

print("Final position Cinnabar Island:", get_pos())
sc = mgba.take_screenshot()
print("Final Screenshot:", sc)
