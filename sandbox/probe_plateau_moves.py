import bridge
import time

def test_moves():
    pos = bridge.get_coordinates()
    print("Starting position:", pos)
    
    for direction in ["Up", "Down", "Left", "Right"]:
        print(f"Testing move: {direction}")
        bridge.press_buttons([direction])
        time.sleep(0.3)
        new_pos = bridge.get_coordinates()
        print(f"Resulting position: {new_pos}")
        if new_pos != pos:
            # Move back
            opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
            bridge.press_buttons([opp])
            time.sleep(0.3)

if __name__ == "__main__":
    test_moves()
