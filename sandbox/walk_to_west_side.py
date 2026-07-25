import mgba
import time

def main():
    print("Walking to the west side of Mt. Moon 1F...")
    # Currently at (31, 30)
    # Step 1: Walk Down 3 steps to (31, 33)
    for i in range(3):
        mgba.press_buttons(["Down", "sleep 320"])
        
    # Step 2: Walk Left 26 steps to (5, 33)
    for i in range(26):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
