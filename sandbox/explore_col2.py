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

# Step 1: Walk to (4, 11)
print("Walking DOWN to (4, 11)...")
mgba.press_buttons(["Down"])
time.sleep(0.55)
p = check_pos()

if p == {"x": 4, "y": 11}:
    # Walk Left along Row 11
    print("Walking Left along Row 11...")
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 3, "y": 11}:
        mgba.press_buttons(["Left"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 2, "y": 11}:
        print("Reached (2, 11)!")
        # Let's check adjacent tiles for a statue!
        # Usually we stand at (2, 12) or (2, 13) and face UP, or similar?
        # Let's try walking Left to (1, 11)
        mgba.press_buttons(["Left"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 1, "y": 11}:
        print("Reached (1, 11)!")
        
else:
    print("Failed to reach (4, 11)")
