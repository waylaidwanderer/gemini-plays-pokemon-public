import mgba
import time

def move_test(step):
    pos_before = mgba.get_coordinates()
    print(f"probe: Pressing '{step}' from {pos_before}...")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_before != pos_after:
        print(f"probe: MOVED to {pos_after}!")
        return pos_after
    else:
        print("probe: Did not move.")
        return None

def main():
    # 1. Dismiss "Got away safely!"
    print("probe: Dismissing text box...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"probe starting from: {pos}")
    
    # 2. Walk Left to (19, 7)
    while pos['x'] > 19:
        pos = move_test("Left")
        if not pos:
            # Maybe a turn-in-place occurred, retry once
            pos = move_test("Left")
            if not pos:
                print("probe: Blocked going Left.")
                return
                
    # 3. Walk Down Column 19 as far as possible!
    print("probe: Walking Down Column 19...")
    for y in range(8, 20):
        pos_after = move_test("Down")
        if not pos_after:
            # Retry once
            pos_after = move_test("Down")
            if not pos_after:
                print(f"probe: Stopped walking Down at {mgba.get_coordinates()}")
                break
        pos = pos_after
        # Check if we fell (if map changed or y is different)
        if pos['y'] > 18 or pos['y'] < 5: # wait, on B1F East y would be around 5-9 or 16
            print(f"probe: WE FELL! Current pos: {pos}")
            break

if __name__ == "__main__":
    main()
