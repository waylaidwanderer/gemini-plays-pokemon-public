import mgba
import time

def press_buttons_safe(buttons):
    mgba.press_buttons(buttons)
    return True

def flee_battle_fully():
    print("Fleeing battle...")
    for _ in range(5):
        press_buttons_safe(["B"])
        time.sleep(0.4)
    press_buttons_safe(["Down", "Right", "A"])
    time.sleep(2.0)
    for _ in range(3):
        press_buttons_safe(["B"])
        time.sleep(0.4)

def walk_to_target(tx, ty):
    attempts = 0
    while attempts < 15:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return "ARRIVED"
        
        dx = tx - pos['x']
        dy = ty - pos['y']
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        else: break
        
        print(f"Walking {direction} to ({tx}, {ty}) from {pos}...")
        press_buttons_safe([direction])
        time.sleep(0.6)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            attempts += 1
            print("No movement. Fleeing battle...")
            flee_battle_fully()
            chk_pos = mgba.get_coordinates()
            if chk_pos['x'] != pos['x'] or chk_pos['y'] != pos['y']:
                print(f"Displaced to {chk_pos}")
                return "DISPLACED"
        else:
            attempts = 0
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return "ARRIVED"
            # If coordinates changed but not to the target, we fell/warped!
            if abs(new_pos['x'] - pos['x']) > 1 or abs(new_pos['y'] - pos['y']) > 1:
                print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                return "FALLEN"
    return "FAILED"

def main():
    pos = mgba.get_coordinates()
    print("Starting from:", pos)
    
    # Path from (8, 1) to (19, 18) balcony drop
    path_to_balcony = [
        # Right along Row 1
        (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1),
        # Down Column 26
        (26, 2), (26, 3), (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12),
        # Left to Column 24
        (25, 12), (24, 12),
        # Down Column 24
        (24, 13), (24, 14), (24, 15), (24, 16),
        # Left along Row 16
        (23, 16), (22, 16), (21, 16),
        # Down Column 21 through open balcony gates
        (21, 17), (21, 18),
        # Left to drop at (19, 18)
        (20, 18), (19, 18)
    ]
    
    # Trim path if we are already along it
    start_idx = 0
    for idx, pt in enumerate(path_to_balcony):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
    active_path = path_to_balcony[start_idx:]
    
    print("Executing path to balcony...")
    for target in active_path:
        res = walk_to_target(target[0], target[1])
        if res == "FALLEN":
            print("Warped/Fell successfully! Landed at:", mgba.get_coordinates())
            mgba.take_screenshot()
            return
        elif res == "DISPLACED":
            print("Displaced on way to balcony.")
            continue
        elif res == "FAILED":
            print(f"Failed to reach {target}")
            break
            
    final_pos = mgba.get_coordinates()
    print("Final position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
