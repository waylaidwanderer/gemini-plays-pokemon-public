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
        
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            flee_battle()
        else:
            attempts = 0
    return mgba.get_coordinates() == {'x': tx, 'y': ty}

def main():
    print("Walking to (22, 3)...")
    if not walk_to_target(22, 3):
        print("Failed to reach (22, 3)")
        return
    
    print("Walking to (22, 2)...")
    if not walk_to_target(22, 2):
        print("Failed to reach (22, 2)")
        return
        
    print("Facing Left and trying to step onto (21, 2)...")
    pos = mgba.get_coordinates()
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == 21 and new_pos['y'] == 2:
        print("VERDICT: Mansion is in STATE A (Gate at (21, 2) is open!)")
        # Step back to (22, 2)
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    else:
        print("VERDICT: Mansion is in STATE B (Gate at (21, 2) is closed!)")
        
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
