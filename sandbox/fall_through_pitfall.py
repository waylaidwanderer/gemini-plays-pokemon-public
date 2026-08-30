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
    # Currently at (17, 6) on 2F East
    path = [
        # 1. UP Column 17 to Row 3
        (17, 5),
        (17, 4),
        (17, 3),
        # 2. Left along Row 3 to Column 12
        (16, 3),
        (15, 3),
        (14, 3),
        (13, 3),
        (12, 3),
        # 3. DOWN Column 12 to Row 14
        (12, 4),
        (12, 5),
        (12, 6),
        (12, 7),
        (12, 8),
        (12, 9),
        (12, 10),
        (12, 11),
        (12, 12),
        (12, 13),
        (12, 14),
        # 4. Right along Row 14 to Column 16 (the pitfall!)
        (13, 14),
        (14, 14),
        (15, 14),
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
