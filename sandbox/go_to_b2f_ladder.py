import mgba
import time

def main():
    print("Walking to B1F (13, 27) ladder to warp to B2F...")
    # Currently at (25, 15) on B1F
    
    # Step 1: Walk Down 11 steps to (25, 26)
    print("Walking Down...")
    for i in range(11):
        mgba.press_buttons(["Down", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Down Step {i+1}: Coordinates={pos}")
        
    # Step 2: Walk Left 12 steps to (13, 26)
    print("Walking Left...")
    for i in range(12):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Left Step {i+1}: Coordinates={pos}")
        
    # Step 3: Walk Down 1 step to (13, 27)
    print("Warping Down...")
    mgba.press_buttons(["Down", "sleep 320"])
    pos = mgba.get_coordinates()
    screenshot = mgba.take_screenshot()
    print(f"Final Step: Coordinates={pos}, Screenshot={screenshot}")
    
if __name__ == "__main__":
    main()
