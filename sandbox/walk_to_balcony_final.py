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
            # Check button limit to prevent crash
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
                    print(f"Warp/Fall detected after battle: {chk_pos}")
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

def main():
    pos = mgba.get_coordinates()
    print("State B Balcony Controller - Start Position:", pos)
    
    # Path from (19, 3) on 3F East to (19, 18) balcony drop in State B
    path = [
        # 1. Right along Row 3 to Column 26
        (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        # 2. Down Column 26 to Row 16 (since State B has open Row 13 on Column 26)
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16),
        # 3. Left along Row 16 to Column 21
        (25, 16), (24, 16), (23, 16), (22, 16), (21, 16),
        # 4. Down Column 21 through open balcony gates to Row 18
        (21, 17), (21, 18),
        # 5. Left along Row 18 to Column 19 (the drop!)
        (20, 18), (19, 18)
    ]
    
    # Strip any leading elements of the path if we are already partially along it
    # We find if our current pos is in the path
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
            
    active_path = path[start_idx:]
    print("Active Path:", active_path)
    
    walk_route(active_path, detect_warp=True)
    mgba.take_screenshot()
    print("State B Balcony Controller - End Position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
