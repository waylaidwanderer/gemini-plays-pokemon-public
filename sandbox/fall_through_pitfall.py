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

def walk_to_pitfall_2f():
    # Currently at (22, 2) on 2F East
    path = [
        # 1. Right to Column 26
        (23, 2),
        (24, 2),
        (25, 2),
        (26, 2),
        # 2. DOWN Column 26 to Row 15
        (26, 3),
        (26, 4),
        (26, 5),
        (26, 6),
        (26, 7),
        (26, 8),
        (26, 9),
        (26, 10),
        (26, 11),
        (26, 12),
        (26, 13),
        (26, 14),
        (26, 15) # Expected 2F East pitfall!
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

    # If we reached (26, 15) but didn't fall, let's try stepping Right to (27, 15)
    pos = mgba.get_coordinates()
    if pos['x'] == 26 and pos['y'] == 15:
        print("At (26, 15). Trying to step Right to (27, 15) to trigger pitfall...")
        mgba.press_buttons(["Right"])
        time.sleep(0.6)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] != 27 or new_pos['y'] != 15:
            print(f"WARP/FALL DETECTED after stepping Right! Landed at: {new_pos}")
            mgba.take_screenshot()
            return True

    mgba.take_screenshot()
    print(f"Final Position: {mgba.get_coordinates()}")
    return False

walk_to_pitfall_2f()
