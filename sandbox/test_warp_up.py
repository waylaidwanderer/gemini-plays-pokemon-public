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

if p == {"x": 5, "y": 11}:
    print("Walking to (7, 11)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 6, "y": 11}:
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 7, "y": 11}:
        print("At (7, 11). Stepping UP onto stairs at (7, 10)...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # Allow warp animation
        p = check_pos()
        print("Position after warp attempt:", p)
else:
    print("Not starting at (5, 11)")
