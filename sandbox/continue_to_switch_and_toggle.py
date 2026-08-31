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
    # We are starting at (26, 3) on 3F East.
    # Path to (3, 5) on 3F West:
    path = [
        # Left along Row 3 to Column 10
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
        # Down Column 10 to Row 6
        (10, 4), (10, 5), (10, 6),
        # Left along Row 6 to Column 3
        (9, 6), (8, 6), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6),
        # Up Column 3 to Row 5 (standing next to switch at (2, 5))
        (3, 5)
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
        walk_to_target(target)
        
    print("Reached switch area at (3, 5). Turning LEFT...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    print("Pressing A to interact with Mewtwo statue switch at (2, 5) to set to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Clear residual text / menu
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    print("Toggled switch. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
