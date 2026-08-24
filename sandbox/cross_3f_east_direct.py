
import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting for battle menu to load...")
    mgba.press_buttons(["sleep 2000"]) # Wait for battle transition to finish
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
            mgba.press_buttons(["sleep 150"])
            pos_now = get_pos()
            if pos_now == pos_before:
                # We are definitely blocked/in battle!
                run_from_battle()
        else:
            print(f"Stepped {direction} to {pos_after}")
            
        steps += 1
    print("Failed to reach target.")
    return False

# Starting from current position (7, 11) on 3F West
print("PHASE 1: Crossing 3F West to 3F East...")
if not walk_to(6, 11): sys.exit(1)
if not walk_to(6, 9): sys.exit(1)
if not walk_to(12, 9): sys.exit(1)
if not walk_to(12, 6): sys.exit(1)
if not walk_to(26, 6): sys.exit(1)

print("Stepping Right onto pitfall to drop...")
mgba.press_buttons(["Right", "sleep 2500"])
print("Position after drop (should be 1F East inside fenced room around 25, 6):", get_pos())

print("PHASE 2: Walking to B1F stairs...")
if not walk_to(26, 3): sys.exit(1)
if not walk_to(22, 3): sys.exit(1)
if not walk_to(22, 2): sys.exit(1)

print("Stepping UP to warp down to B1F East...")
mgba.press_buttons(["Up", "sleep 2500"])
print("Position on B1F East (should be around 22, 3):", get_pos())

# On B1F East, walk horizontally to B1F West Secret Key room
print("PHASE 3: Walking to B1F West Secret Key room...")
if not walk_to(21, 3): sys.exit(1)
if not walk_to(21, 5): sys.exit(1)
if not walk_to(1, 5): sys.exit(1)

# Retrieve Secret Key at (1, 4)
print("PHASE 4: Picking up the Secret Key at (1, 4)...")
mgba.press_buttons(["Up", "sleep 250"])
mgba.press_buttons(["A", "sleep 800"]) # Obtained dialogue
mgba.press_buttons(["A", "sleep 800"]) # Clear dialogue
mgba.press_buttons(["B", "sleep 400"]) # Safeguard close
print("Secret Key retrieved! Current position:", get_pos())

# DIG out back to Cinnabar Island
print("PHASE 5: Escaping via DIG...")
mgba.press_buttons(["Start", "sleep 400"])
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 600"]) # Select POK�MON
for _ in range(5): # 5 Down presses to select TRUFFLE (Slot 6)
    mgba.press_buttons(["Down", "sleep 180"])
mgba.press_buttons(["A", "sleep 600"]) # Select TRUFFLE
mgba.press_buttons(["A", "sleep 3000"]) # Select DIG
print("SUCCESS! Final position Cinnabar Island:", get_pos())
mgba.take_screenshot()
