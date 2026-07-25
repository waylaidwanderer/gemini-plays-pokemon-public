import mgba
import time

def main():
    print("Walking to the 1F (25, 15) ladder...")
    # Currently at (30, 33)
    
    # Step 1: Walk Up 18 steps to (30, 15)
    print("Walking Up...")
    for i in range(18):
        mgba.press_buttons(["Up", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Up Step {i+1}: Coordinates={pos}")
        
    # Step 2: Walk Left 5 steps to (25, 15)
    print("Walking Left...")
    for i in range(5):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
