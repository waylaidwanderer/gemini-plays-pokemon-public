
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

# Starting from current position (5, 27) inside 1F West
print("PHASE 2: Warp UP to 2F West...")
if not walk_to(5, 11): sys.exit(1)
if not walk_to(8, 11): sys.exit(1)
if not walk_to(8, 10): sys.exit(1)
if not walk_to(5, 10): sys.exit(1)
print("Stepping Left to warp to 2F West...")
mgba.press_buttons(["Left", "sleep 2500"])
print("Position on 2F West:", get_pos())

# Navigate 2F West to 3F West (State A)
print("PHASE 3: Warp UP to 3F West...")
if not walk_to(7, 11): sys.exit(1)
print("Stepping UP to warp to 3F West...")
mgba.press_buttons(["Up", "sleep 2500"])
print("Position on 3F West:", get_pos())

# Toggle Mewtwo Statue Switch at (2, 11) to State B
print("PHASE 4: Toggling switch to State B...")
if not walk_to(3, 11): sys.exit(1)
if not walk_to(3, 13): sys.exit(1)
if not walk_to(1, 13): sys.exit(1)
if not walk_to(1, 11): sys.exit(1)
print("Facing Right towards (2, 11) and interacting...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 800", "A", "sleep 800", "A", "sleep 500", "B", "sleep 300"])
print("State B activated! Current Position:", get_pos())
mgba.take_screenshot()
