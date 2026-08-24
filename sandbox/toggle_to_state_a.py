
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
    max_steps = 50
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
                # We are definitely blocked/in battle!
                run_from_battle()
        steps += 1
    return False

# Starting from current position (7, 11) on 2F West in State B
print("PHASE 1: Bypassing the Burglar to reach switch...")
if not walk_to(6, 11): sys.exit(1)
if not walk_to(6, 9): sys.exit(1)
if not walk_to(3, 9): sys.exit(1)
if not walk_to(3, 11): sys.exit(1)

# Toggle Mewtwo switch back to State A
print("PHASE 2: Toggling switch back to State A...")
mgba.press_buttons(["Left", "sleep 300"])
mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "B", "sleep 400"])

# Walk back to warp stairs at (7, 11)
print("PHASE 3: Walking to stairs (7, 11)...")
if not walk_to(3, 9): sys.exit(1)
if not walk_to(6, 9): sys.exit(1)
if not walk_to(6, 11): sys.exit(1)
if not walk_to(7, 11): sys.exit(1)

# Warp UP to 3F West
print("PHASE 4: Warping UP to 3F West...")
mgba.press_buttons(["Up", "sleep 2500"])
print("Position after warp (should be 3F West):", get_pos())
mgba.take_screenshot()
