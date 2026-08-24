import mgba
import sys
import time

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting 4.5 seconds for intro...")
    time.sleep(4.5)
    # Dismiss "Wild XXX appeared!" text
    print("Dismissing text...")
    mgba.press_buttons(["B", "sleep 350", "B", "sleep 350", "B", "sleep 350"])
    time.sleep(0.5)
    # Now we are definitely at the battle menu. Send RUN selection.
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "sleep 350", "Right", "sleep 350", "A", "sleep 1800"])
    # Clear "Got away safely!"
    print("Clearing escape text...")
    mgba.press_buttons(["B", "sleep 350", "B", "sleep 350", "B", "sleep 350"])
    time.sleep(1.0)
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
            time.sleep(0.3)
            pos_now = get_pos()
            if pos_now == pos_before:
                # We are definitely blocked/in battle!
                run_from_battle()
        else:
            print(f"Stepped {direction} to {pos_after}")
            
        steps += 1
    print("Failed to reach target.")
    return False

# Starting at current position on 3F West
print("Starting cross_and_drop_fast.py...")
print("Initial Position:", get_pos())

# Step 1: Walk to (1, 9)
if not walk_to(1, 9): sys.exit(1)

# Step 2: Walk to (12, 9)
if not walk_to(12, 9): sys.exit(1)

# Step 3: Walk to (12, 6)
if not walk_to(12, 6): sys.exit(1)

# Step 4: Walk to pitfall at (26, 6)
if not walk_to(26, 6): sys.exit(1)

print("Dropped through pitfall! Waiting 2.0 seconds...")
time.sleep(2.0)
print("Final Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
