import mgba
import time

def main():
    print("Testing row 25 crossing via column 23...")
    # Currently at (24, 28)
    
    # Step 1: Walk Left 1 step to (23, 28)
    mgba.press_buttons(["Left", "sleep 320"])
    
    # Step 2: Walk Up 3 steps to (23, 25)
    print("Walking Up...")
    for i in range(3):
        mgba.press_buttons(["Up", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Up Step {i+1}: Coordinates={pos}")
        
    # Step 3: Walk Left 8 steps to (15, 25)
    print("Walking Left on row 25...")
    for i in range(8):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
