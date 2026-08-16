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
        # Blocked or battle
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            return False, (cx, cy)
            
        return True, (after['x'], after['y'])
    else:
        return True, (new_pos['x'], new_pos['y'])

print("Probing Left along Row 5 and checking for DOWN paths...")
# We are at (9, 5).
while True:
    curr = mgba.get_coordinates()
    cx, cy = curr['x'], curr['y']
    print(f"At ({cx}, {cy}). Probing DOWN...")
    
    # Try walking DOWN
    success_down, pos_down = step("Down")
    if success_down:
        print(f"Found DOWN path at Column {cx}! Reached {pos_down}")
        # Walk back UP to keep probing
        step("Up")
    else:
        print(f"Column {cx} Row {cy+1} is BLOCKED.")
        
    # Try walking LEFT
    success_left, pos_left = step("Left")
    if not success_left:
        print("Blocked Left! No more probing possible.")
        break
    
    # If we walked LEFT, continue loop

print("Probing complete.")
mgba.take_screenshot()
