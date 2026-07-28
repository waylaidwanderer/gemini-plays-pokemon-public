import mgba
import time

def main():
    print("Testing row 25 crossing via column 25...")
    # Currently at (20, 28)
    
    # Step 1: Walk Right 5 steps to (25, 28)
    for i in range(5):
        mgba.press_buttons(["Right", "sleep 320"])
        
    # Step 2: Walk Up 3 steps to (25, 25)
    for i in range(3):
        mgba.press_buttons(["Up", "sleep 320"])
        
    # Step 3: Walk Left 10 steps on row 25 to (15, 25)
    print("Walking Left on row 25...")
    for i in range(10):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Left Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
