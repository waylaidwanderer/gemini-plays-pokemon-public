import bridge
import time

def test_bypass():
    pos = bridge.get_coordinates()
    print(f"Starting at: {pos}")
    # Let's try Up, then Left, Left, Left, Left, then Down to get to (10, 24)
    # The target sequence is: Up (14, 23), Left (13, 23), Left (12, 23), Left (11, 23), Left (10, 23), Down (10, 24)
    steps = ["Up", "Left", "Left", "Left", "Left", "Down"]
    for i, step in enumerate(steps):
        bridge.press_buttons([step, "sleep 350"])
        new_pos = bridge.get_coordinates()
        print(f"Step {i+1} ({step}): {new_pos}")
        if new_pos is None:
            print("Encountered battle or lost coordinates. Aborting.")
            return

if __name__ == "__main__":
    test_bypass()
