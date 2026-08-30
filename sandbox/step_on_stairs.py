import mgba
import time

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)

def walk_to_target(tx, ty):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
        
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        else: break
        
        print(f"Walking {direction} to ({tx}, {ty}) from {pos}...")
        mgba.press_buttons([direction])
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            print("No movement. Fleeing battle...")
            flee_battle()
        else:
            attempts = 0
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
    return False

def main():
    print("--- Probing Pitfalls on Column 26 (State B) ---")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # 1. Walk Right to (26, 3)
    if not walk_to_target(26, 3):
        print("Failed to reach (26, 3)")
        return
        
    # 2. Walk Down Column 26 all the way to Row 12, checking coordinates at each step
    print("Walking Down Column 26...")
    for y in range(4, 13):
        print(f"Attempting to step DOWN to ({26}, {y})...")
        mgba.press_buttons(["Down"])
        time.sleep(0.8)
        
        new_pos = mgba.get_coordinates()
        print("Current position:", new_pos)
        
        # Check if we dropped to another floor (our Y would change or map transition)
        # 1F East landing is at (26, 4) or (25, 6)
        if new_pos['y'] != y and new_pos['x'] != 26:
            print("Warp/Fall detected! New position:", new_pos)
            mgba.take_screenshot()
            return
            
        if new_pos == pos:
            # We didn't move, check for battle
            print("No movement. Checking for battle...")
            flee_battle()
            new_pos = mgba.get_coordinates()
            if new_pos['x'] != 26:
                print("Displaced after battle! New position:", new_pos)
                mgba.take_screenshot()
                return
        pos = new_pos

    print("Finished probing Column 26. No pitfall triggered.")
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
