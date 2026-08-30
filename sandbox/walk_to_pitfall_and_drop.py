import mgba
import time

def main():
    print("Walking Right to Column 26 on Row 3...")
    for i in range(7):
        pos = mgba.get_coordinates()
        print(f"Current Position: {pos}")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print(f"Current Position at (26, 3)? : {pos}")
    
    # Take a screenshot before dropping
    mgba.take_screenshot()
    
    print("Walking Down onto the pitfall at (26, 4)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    
    pos_after = mgba.get_coordinates()
    print(f"Position after dropping: {pos_after}")
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
