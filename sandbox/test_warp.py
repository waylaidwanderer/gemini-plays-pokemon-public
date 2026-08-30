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

def walk_down_col12():
    # Currently at (27, 15)
    path = [
        # 1. Walk Left to Column 25
        (26, 15),
        (25, 15),
        # 2. Walk UP Column 25 to Row 1
        (25, 14),
        (25, 13), # Open gate!
        (25, 12),
        (25, 11),
        (25, 10),
        (25, 9),
        (25, 8),
        (25, 7),
        (25, 6),
        (25, 5),
        (25, 4),
        (25, 3),
        (25, 2),
        (25, 1),
        # 3. Walk Left to Column 12
        (24, 1),
        (23, 1),
        (22, 1),
        (21, 1),
        (20, 1),
        (19, 1),
        (18, 1),
        (17, 1),
        (16, 1),
        (15, 1),
        (14, 1),
        (13, 1),
        (12, 1),
        # 4. Walk DOWN Column 12 as far as possible
        (12, 2),
        (12, 3),
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
        (12, 15),
        (12, 16),
        (12, 17),
        (12, 18),
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
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break
                else:
                    print(f"Displaced to {new_pos}. Retrying target ({tx}, {ty}).")
                    time.sleep(0.3)
                    
    mgba.take_screenshot()
    print(f"Final Position: {mgba.get_coordinates()}")
    return False

walk_down_col12()
