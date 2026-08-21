import mgba
import time

# We are at (12, 10). Let's test Column 11 to Row 11 to bypass (12, 11) if it's a gate.

test_path = ["Left", "Down", "Right", "Right", "Right", "Right", "Up"]

for idx, direction in enumerate(test_path):
    pos_before = mgba.get_coordinates()
    print(f"Step {idx}: trying to move {direction} from {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print(f"Blocked at {pos_before} trying to move {direction}")
        # Try to see if battle occurred
        mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A", "sleep 1000", "B"])
        time.sleep(1.0)
        pos_now = mgba.get_coordinates()
        print(f"Coordinates now: {pos_now}")
        if pos_now != pos_before:
            print("Warped or moved!")
            break
    else:
        print(f"Moved to {pos_after}")
