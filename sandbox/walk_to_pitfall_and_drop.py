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

def walk_route():
    # Currently at (26, 8)
    path = [
        # 1. Down Column 26 to Row 12
        (26, 9),
        (26, 10),
        (26, 11),
        (26, 12),
        # 2. Left to Column 25
        (25, 12),
        # 3. Down Column 25 through the open gate to Row 16
        (25, 13),
        (25, 14),
        (25, 15),
        (25, 16),
        # 4. Left along Row 16 to (18, 16) (the pitfall!)
        (24, 16),
        (23, 16),
        (22, 16),
        (21, 16),
        (20, 16),
        (19, 16),
        (18, 16)
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
                if tx == 18 and ty == 16:
                    # Expected pitfall warp
                    if new_pos['x'] != tx or new_pos['y'] != ty:
                        print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                        mgba.take_screenshot()
                        return True
                
                if new_pos['x'] == tx and new_pos['y'] == ty:
                    print(f"[{i}] Arrived at ({tx}, {ty})")
                    break

    mgba.take_screenshot()
    print(f"Final Position: {mgba.get_coordinates()}")
    return False

if __name__ == "__main__":
    walk_route()
