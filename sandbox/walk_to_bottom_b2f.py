import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

# We are at (25, 13) on B2F
pos = mgba.get_coordinates()
print("Starting from:", pos)

if pos['x'] == 25 and pos['y'] == 13:
    # Walk Down to Row 15
    print("Walking Down to Row 15...")
    pos = move(["Down"])
    pos = move(["Down"])
    
    # Walk Left to Column 19
    print("Walking Left to Column 19...")
    for _ in range(6):
        pos = move(["Left"])
        
    # Walk Up to Row 11
    print("Walking Up to Row 11...")
    pos = move(["Up"])
    pos = move(["Up"])
    
    # Step Left onto (17, 11) LEFT spinner -> slides to (2, 9)
    print("Stepping onto (17, 11) LEFT spinner...")
    pos = move(["Left"])
    pos = move(["Left"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide 1:", pos)
    
    # Walk to (3, 11)
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    
    # Step Right onto (4, 11) RIGHT spinner -> slides to (8, 11)
    print("Stepping onto (4, 11) RIGHT spinner...")
    pos = move(["Right"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide 2:", pos)
    
    # Walk to (10, 14)
    pos = move(["Right"])
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    pos = move(["Down"])
    
    # Step Right onto (11, 14) DOWN spinner -> slides to (15, 18)
    print("Stepping onto (11, 14) DOWN spinner...")
    pos = move(["Right"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide 3:", pos)
    
    # Walk to (14, 18)
    pos = move(["Left"])
    
    # Step Left onto (13, 18) LEFT spinner -> slides to (11, 20) stopper
    print("Stepping onto (13, 18) LEFT spinner...")
    pos = move(["Left"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after slide 4:", pos)
    
    # Let's explore walking Right along Row 20 to see if we can reach Column 24!
    print("Exploring Row 20 walkability...")
    for i in range(15):
        old_pos = pos
        pos = move(["Right"])
        if pos == old_pos:
            print(f"Blocked going Right at: {pos}")
            break
            
    # Let's see if we can walk Down to Row 21 or 22 from where we got blocked
    print("Exploring Downward walkability from block...")
    pos = move(["Down"])
    if pos['y'] > 20:
        # If we could walk Down, let's try walking Right from here!
        for i in range(15):
            old_pos = pos
            pos = move(["Right"])
            if pos == old_pos:
                print(f"Blocked going Right on lower row at: {pos}")
                break

mgba.take_screenshot()
