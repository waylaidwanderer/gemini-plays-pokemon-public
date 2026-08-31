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
    
    # Path from (18, 10) to balcony drop at (19, 18)
    path = [
        (19, 10), (20, 10),
        (20, 11), (20, 12), (20, 13), (20, 14), (20, 15), (20, 16),
        (21, 16),
        (21, 17), (21, 18),
        (20, 18), (19, 18)
    ]
    
    # Trim path in case we are already on it
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
    active_path = path[start_idx:]
    
    print("Executing walk to balcony drop...")
    for target in active_path:
        res = walk_to_target(target[0], target[1])
        if res == "FALLEN":
            print("Warped/Fell successfully! Landed at:", mgba.get_coordinates())
            mgba.take_screenshot()
            return
        elif res == "DISPLACED":
            print("Displaced. Re-evaluating position...")
            # Restart pathing
            break
        elif res == "FAILED":
            print(f"Failed to reach {target}")
            break
            
    final_pos = mgba.get_coordinates()
    print("Final position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
