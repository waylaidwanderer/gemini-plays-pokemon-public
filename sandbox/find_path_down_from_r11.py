import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step(direction):
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == cx and new_pos['y'] == cy:
        # We didn't move!
        # Check if in battle or just blocked
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            return False, (cx, cy)
        return True, (after['x'], after['y'])
    return True, (new_pos['x'], new_pos['y'])

# Start at (25, 11)
print("Systematically probing Left on Row 11 for DOWN path...")
while True:
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    print(f"At ({cx}, {cy}). Probing DOWN...")
    
    # Try DOWN
    success_d, pos_d = step("Down")
    if success_d:
        print(f"SUCCESS! Found DOWN path at Column {cx}! Reached: {pos_d}")
        break
    else:
        print(f"Column {cx} DOWN is blocked.")
        
    # Try LEFT
    success_l, pos_l = step("Left")
    if not success_l:
        print("Blocked Left! No more columns to test on Row 11.")
        break

print("Probing complete.")
mgba.take_screenshot()
