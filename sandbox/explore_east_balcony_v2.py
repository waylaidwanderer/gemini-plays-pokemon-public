import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 10:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

def walk_to_local(tx, ty):
    pos = mgba.get_coordinates()
    attempts = 0
    while (pos['x'] != tx or pos['y'] != ty) and attempts < 40:
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx < 0: d = "Left"
        elif dx > 0: d = "Right"
        elif dy < 0: d = "Up"
        else: d = "Down"
        
        pos_before = pos
        mgba.press_buttons([d])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        if pos == pos_before:
            handle_battle()
            pos = mgba.get_coordinates()
        attempts += 1
    return pos['x'] == tx and pos['y'] == ty

# Start at (26, 5) on 2F East (State B)
pos = mgba.get_coordinates()
print("Starting exploration of 2F East from:", pos)

# We want to see how far Left we can walk along different rows!
# Let's test Row 3, Row 5, Row 6, Row 7, Row 11, Row 14, Row 15, Row 16.

for test_row in [3, 5, 6, 7, 11, 14, 15, 16]:
    # Reset to (26, 5)
    print(f"\n--- Testing Row {test_row} ---")
    if not walk_to_local(26, 5):
        print("Failed to reset to (26, 5)")
        break
        
    # Walk to Column 26 on the target row
    if not walk_to_local(26, test_row):
        print(f"Failed to reach column 26 on Row {test_row}")
        continue
        
    # Try to walk LEFT as far as possible
    col = 26
    while col > 1:
        next_col = col - 1
        if walk_step(next_col, test_row, 'Left'):
            col = next_col
        else:
            print(f"Blocked on Row {test_row} at Column {col} going LEFT to {next_col}")
            break
    print(f"Row {test_row} reached Column {col}")
    if col <= 15:
        print(f"SUCCESS! Row {test_row} crossed the barrier to Column {col}!")
        # Let's see if we can reach (15, 11) from here!
        if walk_to_local(15, 11):
            print("Successfully walked to stairs at (15, 11)!")
            mgba.press_buttons(["Up"])
            time.sleep(2.0)
            print("Warped! Final position:", mgba.get_coordinates())
            mgba.take_screenshot()
            exit()

print("\nFinished testing all rows.")
mgba.take_screenshot()
