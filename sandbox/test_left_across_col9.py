import mgba
import time

# We are at (16, 9). Let's walk and test the tiles to find the warp.
# Let's test Column 15 and Column 14.

test_path = ["Left", "Down", "Down", "Left", "Down"]

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
        # Check coordinates again
        pos_now = mgba.get_coordinates()
        print(f"Coordinates now: {pos_now}")
        if pos_now != pos_before:
            print("Warped or moved!")
            break
    else:
        # Check if map transitioned
        # If we warped, our coordinates might change drastically or we might be on a different floor.
        print(f"Moved to {pos_after}")
