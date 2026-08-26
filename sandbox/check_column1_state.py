import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

p = check_pos()

if p == {"x": 2, "y": 10}:
    # Walk Left to (1, 10)
    print("Walking Left to (1, 10)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 1, "y": 10}:
        # Try walking UP to (1, 9) and (1, 8)
        print("At (1, 10). Trying to walk UP to (1, 9)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        p = check_pos()
        
        if p == {"x": 1, "y": 9}:
            print("At (1, 9). Trying UP to (1, 8)...")
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            p = check_pos()
            if p == {"x": 1, "y": 8}:
                print("SUCCESS! Column 1 Row 9 is OPEN! We are in State B!")
            else:
                print("BLOCKED at (1, 9) trying to go to (1, 8)")
        else:
            print("BLOCKED at (1, 10) trying to go to (1, 9). We are in State A!")
else:
    print("Not starting at (2, 10)")
