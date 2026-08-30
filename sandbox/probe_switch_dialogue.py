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
            if abs(new_pos['x'] - pos['x']) > 1 or abs(new_pos['y'] - pos['y']) > 1:
                print(f"WARP/FALL DETECTED! Landed at: {new_pos}")
                return "FALLEN"
    return "FAILED"

def main():
    pos = mgba.get_coordinates()
    print("Starting from:", pos)
    
    # Path to the switch at (3, 5) from (22, 16)
    path = [
        # Walk to Column 25
        (23, 16), (24, 16), (25, 16),
        # Up Column 25
        (25, 15), (25, 14), (25, 13), (25, 12),
        # Right to Column 26
        (26, 12),
        # Up Column 26
        (26, 11), (26, 10), (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3),
        # Left along Row 3
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3),
        # Up to Row 1
        (19, 2), (19, 1),
        # Left to Column 4
        (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        # Down Column 4
        (4, 2), (4, 3), (4, 4), (4, 5),
        # Left to (3, 5)
        (3, 5)
    ]
    
    # Trim path
    start_idx = 0
    for idx, pt in enumerate(path):
        if pos['x'] == pt[0] and pos['y'] == pt[1]:
            start_idx = idx + 1
            break
    active_path = path[start_idx:]
    
    success = True
    for target in active_path:
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
        
    print("Facing Left...")
    mgba.press_buttons(["Left"])
    time.sleep(1.0)
    mgba.take_screenshot()
    
    for step in range(1, 6):
        print(f"Pressing A ({step}/5)...")
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        # Save screenshot for each step to see dialogue flow
        filename = mgba.take_screenshot()
        print(f"Screenshot saved to: {filename}")
        
    print("Probing complete.")

if __name__ == "__main__":
    main()
