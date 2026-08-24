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

# Starting at (6, 10)
print("Initial Position:", get_pos())

# Walk to (1, 11) via Column 5 and Row 13
if walk_to(5, 10) and walk_to(5, 13) and walk_to(1, 13) and walk_to(1, 11):
    # Stand at (1, 11) facing Right
    print("Arrived at (1, 11)!")
    print("Facing Right...")
    mgba.press_buttons(["Right", "sleep 300"])

    print("Pressing A (1st time)...")
    mgba.press_buttons(["A", "sleep 800"])
    sc1 = mgba.take_screenshot()
    print("Screenshot after 1st A:", sc1)

    print("Pressing A (2nd time)...")
    mgba.press_buttons(["A", "sleep 800"])
    sc2 = mgba.take_screenshot()
    print("Screenshot after 2nd A:", sc2)

    print("Pressing A (3rd time)...")
    mgba.press_buttons(["A", "sleep 800"])
    sc3 = mgba.take_screenshot()
    print("Screenshot after 3rd A:", sc3)

    mgba.press_buttons(["B", "sleep 300"])
    print("Finished test_switch_interaction.py!")
else:
    print("Failed to reach (1, 11)")
