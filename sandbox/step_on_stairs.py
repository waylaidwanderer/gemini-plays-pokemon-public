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

def walk_to_stairs():
    # Currently at (28, 16)
    path = [
        # 1. Left to Column 26
        (27, 16),
        (26, 16),
        # 2. UP Column 26 to Row 1
        (26, 15),
        (26, 14),
        (26, 13), # Wait, (26, 13) is a solid partition wall!
    ]
    
    # Wait, (26, 13) is blocked, so we must use Column 25 (where (25, 13) gate is open in State A!)
    path = [
        # 1. Left to Column 25
        (27, 16),
        (26, 16),
        (25, 16),
        # 2. UP Column 25 past Row 13 to Row 12
        (25, 15),
        (25, 14),
        (25, 13), # Open gate in State A!
        (25, 12),
        # 3. Right to Column 26
        (26, 12),
        # 4. UP Column 26 to Row 1
        (26, 11),
        (26, 10),
        (26, 9),
        (26, 8),
        (26, 7),
        (26, 6),
        (26, 5),
        (26, 4),
        (26, 3),
        (26, 2),
        (26, 1),
        # 5. Left to Column 22 on Row 1 (the stairs!)
        (25, 1),
        (24, 1),
        (23, 1),
        (22, 1)
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
                if tx == 22 and ty == 1:
                    # Expected stair warp
                    if new_pos['x'] != tx or new_pos['y'] != ty:
                        print(f"WARP DETECTED! Landed at: {new_pos}")
                        mgba.take_screenshot()
                        return True
                
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break

    mgba.take_screenshot()
    print(f"Final Position: {mgba.get_coordinates()}")
    return False

walk_to_stairs()
