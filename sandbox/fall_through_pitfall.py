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

def walk_to_2f_pitfall():
    # Currently at (24, 11) on 2F East
    path = [
        # 1. Right to Column 26
        (25, 11),
        (26, 11),
        # 2. UP Column 26 to Row 6
        (26, 10),
        (26, 9),
        (26, 8),
        (26, 7),
        (26, 6),
        # 3. Left along Row 6 to Column 16
        (25, 6),
        (24, 6),
        (23, 6),
        (22, 6),
        (21, 6),
        (20, 6),
        (19, 6),
        (18, 6),
        (17, 6),
        (16, 6),
        # 4. DOWN Column 16 to Row 14 (Expected 2F East pitfall!)
        (16, 7),
        (16, 8),
        (16, 9),
        (16, 10),
        (16, 11),
        (16, 12),
        (16, 13),
        (16, 14)
    ]
    
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
                print("Coordinates did not change. Checking for battle/barrier...")
                flee_battle()
                chk_pos = mgba.get_coordinates()
                if chk_pos['x'] != pos['x'] or chk_pos['y'] != pos['y']:
                    print(f"Warp detected after flee: {chk_pos}")
                    return True
            else:
                attempts = 0
                # If we warp/fall, the coordinates will change and not match the target
                if new_pos['x'] != tx or new_pos['y'] != ty:
                    print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                    mgba.take_screenshot()
                    return True
                
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break

    # If we reached (16, 14) but didn't fall, try stepping Down to (16, 15)
    pos = mgba.get_coordinates()
    if pos['x'] == 16 and pos['y'] == 14:
        print("At (16, 14). Trying to step Down to (16, 15) to trigger pitfall...")
        mgba.press_buttons(["Down"])
        time.sleep(0.6)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] != 16 or new_pos['y'] != 15:
            print(f"WARP/FALL DETECTED after stepping Down! Landed at: {new_pos}")
            mgba.take_screenshot()
            return True

    mgba.take_screenshot()
    print(f"Final Position: {mgba.get_coordinates()}")
    return False

walk_to_2f_pitfall()
