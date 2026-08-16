import mgba
import time

def escape_battle():
    print("Encountered a battle! Escape sequence...")
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
        # Check if in battle or just bumped
        escape_battle()
        time.sleep(0.5)
        after = mgba.get_coordinates()
        if after['x'] == cx and after['y'] == cy:
            return False, (cx, cy)
        return True, (after['x'], after['y'])
    return True, (new_pos['x'], new_pos['y'])

print("--- PROBING COLUMN 29 ---")
# Start at current position (28, 11).
# We will walk UP along Column 28 to Row 0 (or as far as we can), trying to step RIGHT at each row.
# Then we will walk DOWN to Row 35, trying to step RIGHT at each row.

for direction in ["Up", "Down"]:
    print(f"Probing {direction} and Right...")
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        
        # Try stepping Right onto Column 29
        success, pos = step("Right")
        if success and pos[0] == 29:
            print(f"SUCCESS! Crossed Column 29 at Row {pos[1]}")
            # Step back Left to keep probing
            step("Left")
        
        # Now move UP or DOWN to the next row
        success_move, pos_move = step(direction)
        if not success_move:
            print(f"Blocked moving {direction} at Row {cy}")
            break
        
        # Boundary check to avoid endless loop
        if direction == "Up" and pos_move[1] <= 1:
            break
        if direction == "Down" and pos_move[1] >= 34:
            break
