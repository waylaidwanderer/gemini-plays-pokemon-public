import mgba
import time

def explore():
    print("Walking east to column 34...")
    # Currently at (30, 20).
    # Let's walk Right 4 times to (34, 20).
    for i in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.3)
    
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    print("Walking down column 34...")
    for i in range(15):
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        # If we transition to Route 5, the map will change.
        print(f"Position: {pos}")

explore()
