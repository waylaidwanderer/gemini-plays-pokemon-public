import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting for battle menu to load...")
    time.sleep(2.0) # Wait 2 seconds for battle intro to finish
    # Dismiss any text with B
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    print("Sending escape inputs...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    # Clear "Got away safely!"
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    print("Escape sequence complete.")

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 60
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

# 1. Flee from current wild Ponyta battle
print("Fleeing from starting wild battle...")
run_from_battle()

# 2. Walk UP Column 1 to Row 6
print("Walking to (1, 6) on 3F West...")
if not walk_to(1, 6): sys.exit(1)

# 3. Walk RIGHT along Row 6 to Column 26 to drop!
print("Walking to (26, 6) to drop through the pitfall...")
if not walk_to(26, 6): sys.exit(1)

# Wait for drop transition
print("Dropped! Waiting 2.0 seconds...")
time.sleep(2.0)
print("Position after drop:", get_pos())

# 4. On 1F East inside fenced room, walk to stairs at (22, 2)
print("Navigating fenced 1F East room...")
if not walk_to(26, 3): sys.exit(1)
if not walk_to(21, 3): sys.exit(1)
if not walk_to(21, 2): sys.exit(1)
if not walk_to(22, 2): sys.exit(1)

# Warp DOWN to B1F East
print("Warping DOWN to B1F...")
mgba.press_buttons(["Up", "sleep 1200"])
print("Position on B1F East:", get_pos())

# 5. On B1F East, walk horizontally to B1F West to (1, 5)
print("Crossing B1F to (1, 5)...")
if not walk_to(18, 6): sys.exit(1)
if not walk_to(10, 6): sys.exit(1)
if not walk_to(10, 5): sys.exit(1)
if not walk_to(1, 5): sys.exit(1)

# 6. Stand at (1, 5) facing UP and retrieve Secret Key at (1, 4)
print("Facing UP to retrieve Secret Key...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 800"]) # Obtained dialogue
mgba.press_buttons(["A", "sleep 800"]) # Clear dialogue
mgba.press_buttons(["B", "sleep 400"]) # Safeguard close
print("Secret Key retrieved! Current position:", get_pos())

# 7. Escape via DIG
print("Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 400"])
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"]) # Select POKéMON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 180"])
mgba.press_buttons(["A", "sleep 600"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 1500"]) # Select DIG
time.sleep(3.0)

print("SUCCESS! ESCAPED TO:", get_pos())
mgba.take_screenshot()
