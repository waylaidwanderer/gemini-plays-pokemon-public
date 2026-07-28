import mgba
import time

def main():
    print("Walking to column 30, row 33 on Mt. Moon 1F...")
    # Currently at (24, 25)
    
    # Step 1: Walk Right 1 step to (25, 25)
    mgba.press_buttons(["Right", "sleep 320"])
    
    # Step 2: Walk Down 8 steps to (25, 33)
    print("Walking Down...")
    for i in range(8):
        mgba.press_buttons(["Down", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Down Step {i+1}: Coordinates={pos}")
        
    # Step 3: Walk Right 5 steps to (30, 33)
    print("Walking Right...")
    for i in range(5):
        mgba.press_buttons(["Right", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Right Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
