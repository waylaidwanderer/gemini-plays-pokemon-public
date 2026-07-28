import mgba
import time

def main():
    print("Walking to 1F (25, 15) ladder via column 31 bypass...")
    # Currently at (30, 28)
    
    # Step 1: Walk Right 1 step to (31, 28)
    mgba.press_buttons(["Right", "sleep 320"])
    
    # Step 2: Walk Up 13 steps to (31, 15)
    print("Walking Up...")
    for i in range(13):
        mgba.press_buttons(["Up", "sleep 320"])
        pos = mgba.get_coordinates()
        print(f"Up Step {i+1}: Coordinates={pos}")
        
    # Step 3: Walk Left 6 steps to (25, 15)
    print("Walking Left...")
    for i in range(6):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
