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
    
    # Path from (21, 15) on 1F East to (7, 11) on 1F West
    path = [
        # Up Column 21 to Row 6
        (21, 14), (21, 13), (21, 12), (21, 11), (21, 10), (21, 9), (21, 8), (21, 7), (21, 6),
        # Left along Row 6 to Column 7
        (20, 6), (19, 6), (18, 6), (17, 6), (16, 6), (15, 6), (14, 6), (13, 6), (12, 6), (11, 6), (10, 6), (9, 6), (8, 6), (7, 6),
        # Down Column 7 to (7, 11)
        (7, 7), (7, 8), (7, 9), (7, 10), (7, 11)
    ]
    
    # Trim path
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
    active_path = path[start_idx:]
    
    print("Walking to 1F West stairs...")
    for target in active_path:
        res = walk_to_target(target[0], target[1])
        if res == "FALLEN":
            print("Warped/Fell successfully! Landed at:", mgba.get_coordinates())
            mgba.take_screenshot()
            return
        elif res == "DISPLACED":
            print("Displaced.")
            continue
        elif res == "FAILED":
            print(f"Failed to reach {target}")
            break
            
    # Try stepping Up onto (7, 10) to warp to 2F West
    print("Stepping Up onto stairs at (7, 10)...")
    walk_to_target(7, 10)
    
    final_pos = mgba.get_coordinates()
    print("Final position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
