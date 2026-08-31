import mgba
import time

def flee_battle_fully():
    print("Fleeing battle...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B"])
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
        mgba.press_buttons([direction])
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
    
    # Path from (21, 13) to (22, 1) using Column 17 detour
    path = [
        # Up to Row 12
        (21, 12),
        # Left on Row 12 to Column 19
        (20, 12), (19, 12),
        # Up Column 19 to Row 5
        (19, 11), (19, 10), (19, 9), (19, 8), (19, 7), (19, 6), (19, 5),
        # Left on Row 5 to Column 17
        (18, 5), (17, 5),
        # Up Column 17 to Row 1
        (17, 4), (17, 3), (17, 2), (17, 1),
        # Right on Row 1 to Column 22
        (18, 1), (19, 1), (20, 1), (21, 1), (22, 1)
    ]
    
    # Trim path
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
    active_path = path[start_idx:]
    
    print("Executing walk to 3F East stairs via Column 17 detour...")
    for target in active_path:
        res = walk_to_target(target[0], target[1])
        if res == "FALLEN":
            print("Warped/Fell successfully! Landed at:", mgba.get_coordinates())
            break
        elif res == "DISPLACED":
            print("Displaced.")
            break
        elif res == "FAILED":
            print(f"Failed to reach {target}")
            break

    print("Ended at:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
