import mgba
import time

def escape_battle():
    print("Attempting to escape battle...")
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

def try_step(direction, expected_coords):
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    mgba.press_buttons([direction])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

# Starting from (10, 5)
print("Starting systematic Row search on Column 9...")

# We will test Rows 3, 4, 5, 6, 7
for row in [3, 4, 5, 6, 7]:
    # 1. Move to (10, row)
    print(f"Moving to (10, {row})...")
    current_pos = mgba.get_coordinates()
    
    # Walk vertically to the target row
    while current_pos["y"] != row:
        if current_pos["y"] < row:
            mgba.press_buttons(["Down"])
        else:
            mgba.press_buttons(["Up"])
        time.sleep(0.5)
        current_pos = mgba.get_coordinates()
        
    print(f"At (10, {row}). Testing walk LEFT to (9, {row})...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    new_pos = mgba.get_coordinates()
    if new_pos["x"] == 9:
        print(f"SUCCESS! Walked LEFT on Row {row} to {new_pos}!")
        break
    else:
        print(f"Row {row} is BLOCKED.")
        # Ensure we face LEFT for next attempts or are back at column 10
        if new_pos["x"] != 10:
            mgba.press_buttons(["Right"])
            time.sleep(0.5)

pos = mgba.get_coordinates()
print("Search finished. Current position:", pos)
