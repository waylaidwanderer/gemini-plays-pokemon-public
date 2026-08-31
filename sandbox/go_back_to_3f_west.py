import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Press B to dismiss any initial text/menus
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    
    # Select RUN
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Dismiss "Got away safely!"
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Flee complete.")

def get_dir(curr, target):
    if target[0] > curr['x']: return "Right"
    if target[0] < curr['x']: return "Left"
    if target[1] > curr['y']: return "Down"
    if target[1] < curr['y']: return "Up"
    return None

def walk_to_target(target):
    while True:
        pos = mgba.get_coordinates()
        if pos['x'] == target[0] and pos['y'] == target[1]:
            print(f"Reached target {target}")
            break
            
        direction = get_dir(pos, target)
        if not direction:
            break
            
        print(f"Current: ({pos['x']}, {pos['y']}) | Moving {direction} to target {target}")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We didn't move. Could be battle.
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.3)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.3)

def main():
    print("Starting go_back_to_3f_west.py from (25, 14)...")
    
    # Test path: (25, 14) -> (25, 16) -> (21, 16) -> (12, 16) -> (12, 11) -> (3, 11)
    path = [
        # Down to Row 16
        (25, 15), (25, 16),
        # Left along Row 16 to Column 21
        (24, 16), (23, 16), (22, 16), (21, 16),
        # Continue Left to Column 12
        (20, 16), (19, 16), (18, 16), (17, 16), (16, 16), (15, 16), (14, 16), (13, 16), (12, 16),
        # Up Column 12 to Row 11
        (12, 15), (12, 14), (12, 13), (12, 12), (12, 11),
        # Left along Row 11 to Column 3
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    pos = mgba.get_coordinates()
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Walking path from index {start_idx} (target: {path[start_idx]})")
    for idx in range(start_idx, len(path)):
        walk_to_target(path[idx])
        
    print("Finished go_back_to_3f_west. Current position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
