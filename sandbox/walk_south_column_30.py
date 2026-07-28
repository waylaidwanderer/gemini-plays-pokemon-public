import mgba
import time

def main():
    print("Walking south along column 30...")
    # Starting at (30, 7) on 1F
    # Target: row 35 (28 steps Down)
    
    for i in range(28):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Down", "sleep 320"])
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: Before={pos_before}, After={pos_after}")
        
        screenshot = mgba.take_screenshot()
        print(f"Saved screenshot: {screenshot}")
        
if __name__ == "__main__":
    main()
