import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
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
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.5)

def main():
    print("Dismissing 'Got away safely!' text...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Path to (10, 5) via Row 15:
    # 1. Walk to (25, 15)
    # 2. Walk Left to (10, 15)
    # 3. Walk Up to (10, 5)
    # 4. Walk Right to (21, 5)
    path = [
        # Walk to (25, 15)
        (24, 8), (25, 8), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12), (25, 12), (25, 13), (25, 14), (25, 15),
        # Walk Left along Row 15 to Column 10
        (24, 15), (23, 15), (22, 15), (21, 15), (20, 15), (19, 15), (18, 15), (17, 15), (16, 15), (15, 15), (14, 15), (13, 15), (12, 15), (11, 15), (10, 15),
        # Walk Up Column 10 to Row 5
        (10, 14), (10, 13), (10, 12), (10, 11), (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5),
        # Walk Right along Row 5 to Column 21
        (11, 5), (12, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (18, 5), (19, 5), (20, 5), (21, 5)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Starting path from index {start_idx} (target: {path[start_idx]})")
    for idx in range(start_idx, len(path)):
        target = path[idx]
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
