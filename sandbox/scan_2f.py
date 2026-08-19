import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (7, 7) on 2F.
# Let's walk along row 7 from column 5 to column 12, and at each column, try to step Down to row 8.
print("Scanning row 7 on 2F for any Downward gap to row 8...")

button_count = 0

for x in range(5, 13):
    # Walk to (x, 7)
    pos = mgba.get_coordinates()
    print(f"Targeting ({x}, 7) from {pos}...")
    while pos['x'] > x:
        mgba.press_buttons(["Left"])
        button_count += 1
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            run_from_battle()
            pos = mgba.get_coordinates()
        else:
            pos = new_pos
            
    while pos['x'] < x:
        mgba.press_buttons(["Right"])
        button_count += 1
        time.sleep(0.3)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            run_from_battle()
            pos = mgba.get_coordinates()
        else:
            pos = new_pos

    # Now we are at (x, 7). Test walking Down
    print(f"At {pos}, testing walking DOWN...")
    mgba.press_buttons(["Down"])
    button_count += 1
    time.sleep(0.3)
    pos_after_down = mgba.get_coordinates()
    
    if pos_after_down['y'] > 7:
        print(f"SUCCEEDED! Found a gap Down to {pos_after_down} at column {x}!")
        # Walk back up to row 7 to continue scan or stop
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        break
    else:
        print(f"Column {x} is BLOCKED at row 8.")
        # Check battle
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == pos_after_down:
            pass

print("Final position:", mgba.get_coordinates())
