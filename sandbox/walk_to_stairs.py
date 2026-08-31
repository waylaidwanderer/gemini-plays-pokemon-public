import mgba
import time

def test_stairs():
    # Currently at (7, 10)
    print("Walking Left to (5, 10)...")
    for step in range(2):
        pos = mgba.get_coordinates()
        print(f"Current: {pos}")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        print(f"New position: {new_pos}")

    # Now we are at (5, 10). Let's see if we warp.
    # Try to press UP to go into the stairs
    print("Pressing UP at (5, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Position after pressing UP at (5, 10):", pos)

    # Try to press DOWN to see if we can walk back down
    print("Pressing DOWN...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Position after pressing DOWN:", pos)

if __name__ == "__main__":
    test_stairs()
