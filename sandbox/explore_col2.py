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

if p == {"x": 7, "y": 10}:
    # Let's try walking Left to (6, 10) and (5, 10)
    print("Walking Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.55)
    p = check_pos()
    
    if p == {"x": 6, "y": 10}:
        mgba.press_buttons(["Left"])
        time.sleep(0.55)
        p = check_pos()
        
    if p == {"x": 5, "y": 10}:
        print("Reached (5, 10)!")
        # Let's walk UP Column 5 and see where we get blocked!
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        p = check_pos()
        
        if p == {"x": 5, "y": 9}:
            print("At (5, 9). Trying UP to (5, 8)...")
            mgba.press_buttons(["Up"])
            time.sleep(0.55)
            p = check_pos()
            
            if p == {"x": 5, "y": 8}:
                print("SUCCESS! Column 5 Row 9 is OPEN in State A!")
                # Let's see how far up we can go
                mgba.press_buttons(["Up"])
                time.sleep(0.55)
                p = check_pos()
                
                if p == {"x": 5, "y": 7}:
                    print("At (5, 7)!")
            else:
                print("BLOCKED at (5, 9) trying to go UP to (5, 8) in State A!")
        else:
            print("BLOCKED at (5, 10) trying to go UP to (5, 9)!")
            
else:
    print("Not starting at (7, 10)")
