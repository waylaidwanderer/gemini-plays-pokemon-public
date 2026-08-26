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

# Step 1: Walk to (8, 10)
print("Walking to (8, 10)...")
mgba.press_buttons(["Up"]) # We are currently at (9, 11)
time.sleep(0.55)
p = check_pos()

if p == {"x": 9, "y": 10}:
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()

if p == {"x": 8, "y": 10}:
    print("Walking Left onto stairs at (7, 10)...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5) # Allow warp and pushback animation
    p = check_pos()

# We should be at (7, 11) now due to pushback
if p == {"x": 7, "y": 11}:
    print("Successfully reached (7, 11) via warp pushback!")
    # Now try walking Left to (6, 11) and (5, 11)
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 6, "y": 11}:
        mgba.press_buttons(["Left"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 5, "y": 11}:
        print("Successfully reached (5, 11)!")
        # Now walk UP Column 5
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        p = check_pos()
        
        if p == {"x": 5, "y": 10}:
            print("Walking UP to Row 9...")
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            p = check_pos()
            
            if p == {"x": 5, "y": 9}:
                print("At (5, 9). Trying to walk UP to (5, 8)...")
                mgba.press_buttons(["Up"])
                time.sleep(0.55)
                p = check_pos()
                if p == {"x": 5, "y": 8}:
                    print("SUCCESS! Column 5 Row 9 is OPEN in State A!")
                    # Walk back down
                    mgba.press_buttons(["Down"])
                    time.sleep(0.55)
                else:
                    print("BLOCKED! Column 5 Row 9 is CLOSED in State A!")
            else:
                print("Failed to reach (5, 9)")
        else:
            print("Failed to reach (5, 10)")
else:
    print("Warp pushback test failed or landed elsewhere:", p)

print("Exploration finished!")
