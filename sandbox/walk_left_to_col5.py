import mgba
import time

def main():
    print("Walking left along row 33 from column 21...")
    # Currently at (21, 33)
    # Target: column 5 (16 steps Left)
    
    for i in range(16):
        mgba.press_buttons(["Left", "sleep 320"])
        pos = mgba.get_coordinates()
        screenshot = mgba.take_screenshot()
        print(f"Step {i+1}: Coordinates={pos}, Screenshot={screenshot}")
        
if __name__ == "__main__":
    main()
