import mgba
import time

def main():
    print("Testing row 25 crossing via column 24...")
    # Currently at (20, 28)
    
    # Step 1: Walk Right 4 steps to (24, 28)
    for i in range(4):
        mgba.press_buttons(["Right", "sleep 320"])
        
    # Step 2: Walk Up 3 steps to (24, 25)
    for i in range(3):
        mgba.press_buttons(["Up", "sleep 320"])
        
    # Step 3: Walk Left 9 steps to (15, 25)
    print("Walking Left on row 25...")
    for i in range(9):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
