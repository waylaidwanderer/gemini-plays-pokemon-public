import mgba
import time

def main():
    print("Exploring the east side of Mt. Moon 1F...")
    # Currently at (18, 7)
    # Walk Right 12 steps to (30, 7)
    
    for i in range(12):
        mgba.press_buttons(["Right", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
