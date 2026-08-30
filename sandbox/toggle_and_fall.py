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
    for i, target in enumerate(path):
        tx, ty = target
        attempts = 0
        while attempts < 15:
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
            time.sleep(0.6)
            
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                attempts += 1
                print("Coordinates did not change. Checking for battle...")
                flee_battle()
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
    path_to_switch = [
        # 1. Up Column 26 to Row 3
        (26, 14), (26, 13), (26, 12), (26, 11), (26, 10), (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3),
        # 2. Left along Row 3 to Column 19
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3),
        # 3. Up Column 19 to Row 1
        (19, 2), (19, 1),
        # 4. Left along Row 1 to Column 4
        (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        # 5. Down Column 4 to Row 5
        (4, 2), (4, 3), (4, 4), (4, 5),
        # 6. Left to (3, 5)
        (3, 5)
    ]

    path_to_pitfall = [
        # 1. Right to Column 4
        (4, 5),
        # 2. Up Column 4 to Row 1
        (4, 4), (4, 3), (4, 2), (4, 1),
        # 3. Right along Row 1 to Column 26
        (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1),
        # 4. Down Column 26 to (26, 3) (the pitfall!)
        (26, 2), (26, 3)
    ]

    print("Phase 1: Walking to the switch on 3F West...")
    if not walk_route(path_to_switch):
        print("Failed to reach the switch!")
        return

    print("Phase 2: Toggling switch to State B...")
    toggle_switch()
    mgba.take_screenshot()

    print("Phase 3: Walking back to 3F East to drop through pitfall...")
    walk_route(path_to_pitfall, detect_warp=True)
    
    print("Execution complete. Current position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
