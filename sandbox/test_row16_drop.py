import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def run_main():
    print("Dismissing status menus...")
    # Press B 3 times to get back to overworld
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print("Overworld position:", pos)
    mgba.take_screenshot()
    
    # We should be at (20, 16). Let's walk Left along Row 16
    print("Walking Left from current position to test drop...")
    # First Left press turns us Left
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position after turning Left:", mgba.get_coordinates())
    
    # Now step Left to (19, 16)
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    pos2 = mgba.get_coordinates()
    print("Position after step 1:", pos2)
    
    if pos2['x'] == 19 and pos2['y'] == 16:
        # Step Left to (18, 16)
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos3 = mgba.get_coordinates()
        print("Position after step 2:", pos3)
        
        if pos3['x'] == 18 and pos3['y'] == 16:
            # Step Left to drop off the edge!
            print("At the edge (18, 16). Stepping Left to DROP!")
            mgba.press_buttons(["Left"])
            time.sleep(3.0) # wait for drop
            
            final_pos = mgba.get_coordinates()
            print("Landing position after drop attempt:", final_pos)
            mgba.take_screenshot()
        else:
            print("Blocked at (19, 16)!")
            mgba.take_screenshot()
    else:
        print("Blocked at (20, 16)!")
        mgba.take_screenshot()

if __name__ == "__main__":
    run_main()
