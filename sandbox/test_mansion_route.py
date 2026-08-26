import mgba
import time

def handle_any_menu_or_battle():
    time.sleep(0.1)
    mgba.press_buttons(["B"])
    time.sleep(0.3)

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        print(f"Moved {direction}, current position: {pos}")
        return True
    print(f"Failed to move {direction} to {expected_coords}, current: {pos}")
    return False

def main():
    pos = mgba.get_coordinates()
    print("Starting test_mansion_route from inside Cinnabar Lab:", pos)
    
    # --- STEP 1: Exit Cinnabar Lab ---
    # We are at (2, 3). Walk DOWN to (2, 7) and exit
    while pos["y"] < 7:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
    # Step Down to exit to overworld
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Exited Cinnabar Lab, current overworld position:", pos)
    
    # --- STEP 2: Walk RIGHT to Column 18 ---
    # From (6, 12) to (18, 12)
    while pos["x"] < 18:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Right:", pos)
        
    # --- STEP 3: Walk UP Column 18 to Row 5 ---
    while pos["y"] > 5:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Up:", pos)
        
    # --- STEP 4: Walk LEFT along Row 5 to Column 6 ---
    while pos["x"] > 6:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Left:", pos)
        
    # --- STEP 5: Walk UP Column 6 to Row 3 ---
    while pos["y"] > 3:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        print("After Up:", pos)
        
    # Step UP to enter Mansion
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Final position inside Mansion:", pos)

if __name__ == "__main__":
    main()
