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

def walk_route(path, detect_warp=False):
    button_count = 0
    for i, target in enumerate(path):
        tx, ty = target
        attempts = 0
        while attempts < 15:
            # Check button limit
            if button_count > 35:
                print(f"Approaching button limit ({button_count}). Pausing execution to let player run next turn.")
                return False
                
            pos = mgba.get_coordinates()
            if pos['x'] == tx and pos['y'] == ty:
                print(f"[{i}] Already at ({tx}, {ty})")
                break
            
            dx = tx - pos['x']
            dy = ty - pos['y']
            if dx > 0: direction = "Right"
            elif dx < 0: direction = "Left"
            elif dy > 0: direction = "Down"
            elif dy < 0: direction = "Up"
            else: break
            
            print(f"Moving {direction} from {pos} to ({tx}, {ty}). Attempt {attempts+1}")
            mgba.press_buttons([direction])
            button_count += 1
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                attempts += 1
                print("Coordinates did not change. Checking for battle...")
                flee_battle()
                button_count += 3
                chk_pos = mgba.get_coordinates()
                if detect_warp and (chk_pos['x'] != pos['x'] or chk_pos['y'] != pos['y']):
                    print(f"Warp detected after battle: {chk_pos}")
                    return True
            else:
                attempts = 0
                if detect_warp and (new_pos['x'] != tx or new_pos['y'] != ty):
                    print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                    mgba.take_screenshot()
                    return True
                
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break
    return True

def toggle_switch():
    print("Facing Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # 4 A-Press sequence with generous delays
    for step in range(1, 5):
        print(f"Pressing A ({step}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)

def main():
    pos = mgba.get_coordinates()
    print("Stateful Controller - Start Position:", pos)
    
    # Segment 1: 3F East Corridor to (19, 3)
    if pos['x'] >= 19 and pos['y'] > 3:
        print("--- Segment 1: Walking to (19, 3) ---")
        path = []
        # First walk Up Column 26 to Row 3
        if pos['x'] != 26 and pos['y'] > 3:
            path.append((26, pos['y']))
        for y in range(pos['y'] - 1, 2, -1):
            path.append((26, y))
        # Then walk Left along Row 3 to Column 19
        for x in range(25, 18, -1):
            path.append((x, 3))
            
        print("Path:", path)
        walk_route(path)
        
    # Segment 2: From (19, 3) to (4, 1)
    elif pos['y'] == 3 and pos['x'] >= 4:
        print("--- Segment 2: Walking to (4, 1) ---")
        path = [
            (19, 2), (19, 1)
        ]
        for x in range(18, 3, -1):
            path.append((x, 1))
        print("Path:", path)
        walk_route(path)
        
    # Segment 3: From (4, 1) or Row 1 to (3, 5)
    elif pos['y'] == 1 and pos['x'] == 4:
        print("--- Segment 3: Walking to (3, 5) ---")
        path = [
            (4, 2), (4, 3), (4, 4), (4, 5), (3, 5)
        ]
        print("Path:", path)
        walk_route(path)
        
    # Segment 4: At the switch (3, 5) - TOGGLE
    elif pos['x'] == 3 and pos['y'] == 5:
        print("--- Segment 4: Toggling switch ---")
        toggle_switch()
        mgba.take_screenshot()
        # Immediately take a step Right to (4, 5) to save state and prepare walk back
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
    # Segment 5: From (4, 5) or Row 5 back to (26, 3) (Mansion is in State B)
    elif pos['y'] == 5 and pos['x'] == 4:
        print("--- Segment 5: Walking to (26, 3) in State B ---")
        path = [
            (4, 4), (4, 3), (4, 2), (4, 1)
        ]
        for x in range(5, 27):
            path.append((x, 1))
        path.append((26, 2))
        path.append((26, 3)) # Pitfall!
        print("Path:", path)
        walk_route(path, detect_warp=True)
        
    else:
        print("Unrecognized position. Please align player manually or refine path.")
        
    mgba.take_screenshot()
    print("Stateful Controller - End Position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
