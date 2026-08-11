import bridge
import time

def test_dirs():
    pos = bridge.get_coordinates()
    print(f"Starting test at: {pos}")
    for direction in ["Up", "Down", "Left", "Right"]:
        print(f"Testing direction: {direction}")
        bridge.press_buttons([direction, "sleep 350"])
        new_pos = bridge.get_coordinates()
        print(f"Result: {new_pos}")
        if new_pos != pos:
            # Move back to start
            opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
            print(f"Moving back: {opp}")
            bridge.press_buttons([opp, "sleep 350"])
            pos = bridge.get_coordinates()
            print(f"Re-verified start: {pos}")

if __name__ == "__main__":
    test_dirs()
