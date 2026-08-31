import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Fled battle safely.")

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
        time.sleep(0.5)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # Currently at (22, 16) in State A on 3F East
    pos = mgba.get_coordinates()
    print("Starting go_back_to_3f_west from position:", pos)
    
    path = [
        # Walk to Column 25 on Row 16
        (23, 16), (24, 16), (25, 16),
        # Walk UP Column 25 to Row 12, passing through open gate at (25, 13)
        (25, 15), (25, 14), (25, 13), (25, 12),
        # Walk LEFT along Row 12 to Column 21
        (24, 12), (23, 12), (22, 12), (21, 12),
        # Walk UP Column 21 to Row 2, passing through open gate at (21, 5)
        (21, 11), (21, 10), (21, 9), (21, 8), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (21, 2),
        # Walk LEFT along Row 2 to Column 10
        (20, 2), (19, 2), (18, 2), (17, 2), (16, 2), (15, 2), (14, 2), (13, 2), (12, 2), (11, 2), (10, 2),
        # Walk DOWN Column 10 to Row 11
        (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11),
        # Walk LEFT along Row 11 to Column 3 (near the switch)
        (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    # Find our current position in the path and resume
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Resuming path from index {start_idx} (target: {path[start_idx]})")
    for idx in range(start_idx, len(path)):
        walk_to_target(path[idx])
        
    print("Reached switch. Final position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
