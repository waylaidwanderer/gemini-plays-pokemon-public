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

# Let's walk to (5, 11)
if p == {"x": 2, "y": 11}:
    print("Walking to (5, 11)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 3, "y": 11}:
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 4, "y": 11}:
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 5, "y": 11}:
        print("At (5, 11). Checking if we can walk UP onto (5, 10) stairs...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5) # Allow warp animation if it triggers
        p = check_pos()
        
        # If we didn't warp, where are we?
        if p == {"x": 5, "y": 10}:
            print("Standing on stairs at (5, 10). Let's see if we can walk UP to (5, 9)...")
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            p = check_pos()
            
            if p == {"x": 5, "y": 9}:
                print("At (5, 9). Trying UP to (5, 8)...")
                mgba.press_buttons(["Up"])
                time.sleep(0.55)
                p = check_pos()
                if p == {"x": 5, "y": 8}:
                    print("SUCCESS! We are in State B and Column 5 Row 9 is open!")
                    # Walk back down
                    mgba.press_buttons(["Down"])
                    time.sleep(0.55)
                else:
                    print("BLOCKED at (5, 9) - still in State A!")
            else:
                print("Failed to walk UP past stairs, maybe warped?")
        else:
            print("Warped or blocked at stairs:", p)
else:
    print("Not starting at (2, 11)")
