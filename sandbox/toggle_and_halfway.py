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

def toggle_switch():
    print("Facing Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # 4 A-Press sequence with generous delays
    for step in range(1, 5):
        print(f"Pressing A ({step}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)

def main():
    pos = mgba.get_coordinates()
    print("Starting from:", pos)
    
    # Path to the switch at (3, 5)
    path_to_switch = [
        (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5)
    ]
    
    # Trim if needed
    start_idx = 0
    for idx, pt in enumerate(path_to_switch):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
    active_to_switch = path_to_switch[start_idx:]
    
    success = True
    for target in active_to_switch:
        res = walk_to_target(target[0], target[1])
        if res == "FALLEN":
            print("Fell through a pitfall!")
            return
        elif res == "DISPLACED":
            print("Displaced. Trying to continue...")
            continue
        elif res == "FAILED":
            print(f"Failed to reach {target}")
            success = False
            break
            
    if not success:
        return
        
    print("Toggling Mewtwo switch to State B...")
    toggle_switch()
    mgba.take_screenshot()
    
    print("Stepping Right to (4, 5)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    
    # Path halfway back to (15, 1)
    path_halfway = [
        (4, 4), (4, 3), (4, 2), (4, 1),
        (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1)
    ]
    
    print("Walking halfway back...")
    for target in path_halfway:
        res = walk_to_target(target[0], target[1])
        if res == "FALLEN":
            print("Fell successfully?")
            return
        elif res == "DISPLACED":
            print("Displaced.")
            continue
        elif res == "FAILED":
            print(f"Failed to reach {target}")
            break
            
    print("Reached halfway. Current position:", mgba.get_coordinates())
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
