import mgba
import time
import os

def press_walk(direction, count=1):
    for _ in range(count):
        mgba.press_buttons([direction, "sleep 350"])

def main():
    print("Navigating to B2F manually in script...")
    # Currently at B1F (25, 16)
    
    # Walk Down 10 steps to (25, 26)
    press_walk("Down", 10)
    
    # Walk Left 12 steps to (13, 26)
    press_walk("Left", 12)
    
    # Walk Down 1 step to (13, 27) (warping to B2F (15, 27))
    press_walk("Down", 1)
    time.sleep(1.0) # sleep 1 second for map transition
    
    print("Arrived on B2F. Walking to (15, 23)...")
    # From B2F (15, 27), walk Up 4 steps to (15, 23)
    press_walk("Up", 4)
    
    print("Testing if column 14 is open northwards...")
    # Walk Left 1 step to (14, 23)
    press_walk("Left", 1)
    
    # Try walking Up 6 steps (which would take us through row 22, 21, 20, 19, 18 if open!)
    for i in range(6):
        mgba.press_buttons(["Up", "sleep 350"])
        pos = mgba.get_coordinates()
        print(f"Col 14 Up Step {i+1}: {pos}")
        
    print("Testing if column 16 is open northwards...")
    # Walk back to column 15: Down 6 times (to be safe), then Right 2 times, then Up 6 times on column 16
    press_walk("Down", 6)
    press_walk("Right", 2) # now at (16, 23)
    
    # Try walking Up 6 steps on column 16
    for i in range(6):
        mgba.press_buttons(["Up", "sleep 350"])
        pos = mgba.get_coordinates()
        print(f"Col 16 Up Step {i+1}: {pos}")
        
    final_img = mgba.take_screenshot()
    print(f"Final Screenshot: {final_img}")

if __name__ == "__main__":
    main()
