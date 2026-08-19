import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (10, 26).
# Let's walk UP column 10, and at each step, test if we can walk RIGHT to column 12.
# We will do this up to row 14.

button_count = 0

for y in range(25, 13, -1):
    # Walk to (10, y)
    pos = mgba.get_coordinates()
    print(f"Targeting (10, {y}) from {pos}...")
    while pos['y'] > y:
        mgba.press_buttons(["Up"])
        button_count += 1
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            run_from_battle()
            pos = mgba.get_coordinates()
        else:
            pos = new_pos
            
    while pos['y'] < y:
        mgba.press_buttons(["Down"])
        button_count += 1
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            run_from_battle()
            pos = mgba.get_coordinates()
        else:
            pos = new_pos

    # Now we are at (10, y). Test walking Right twice to reach column 12 (or just once to column 11)
    print(f"At {pos}, testing walking RIGHT...")
    mgba.press_buttons(["Right"])
    button_count += 1
    time.sleep(0.3)
    pos_after_right = mgba.get_coordinates()
    
    if pos_after_right['x'] > 10:
        print(f"SUCCEEDED! Walked Right to {pos_after_right} on row {y}!")
        break
    else:
        print(f"Failed to walk Right on row {y}. Coordinates remained: {pos_after_right}")
        # In case we entered a battle during the Right test
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == pos_after_right:
            # Check if battle screen is open, if so run away
            pass # the loop will handle it or we will see in output

print("Final position:", mgba.get_coordinates())
