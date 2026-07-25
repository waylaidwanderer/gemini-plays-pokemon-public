import mgba
import time

def main():
    print("Walking to B2F (21, 17) vertical chamber ladder...")
    # Currently at (15, 27) on B2F
    
    # Step 1: Walk Up 5 steps to (15, 22)
    print("Walking Up...")
    for i in range(5):
        mgba.press_buttons(["Up", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Up Step {i+1}: Coordinates={pos}")
        
    # Step 2: Walk Right 6 steps to (21, 22)
    print("Walking Right...")
    for i in range(6):
        mgba.press_buttons(["Right", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Right Step {i+1}: Coordinates={pos}")
        
    # Step 3: Walk Up 5 steps to (21, 17)
    print("Walking Up to ladder...")
    for i in range(5):
        mgba.press_buttons(["Up", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Up to Ladder Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
