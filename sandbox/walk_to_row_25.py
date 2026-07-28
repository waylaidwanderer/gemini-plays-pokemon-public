import mgba
import time

def main():
    print("Testing row 25 crossing on Mt. Moon 1F...")
    # Currently at (20, 33)
    # Step 1: Walk Up 8 steps to (20, 25)
    for i in range(8):
        mgba.press_buttons(["Up", "sleep 320"])
        
    # Step 2: Walk Left 5 steps to (15, 25)
    for i in range(5):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
