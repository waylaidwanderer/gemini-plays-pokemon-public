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
    # Currently at (11, 7) or nearby on 3F
    # Path to switch at (3, 5) via Column 12 and Row 11:
    path = [
        # Walk to Column 12 on Row 7
        (12, 7),
        # Down Column 12 to Row 11
        (12, 8), (12, 9), (12, 10), (12, 11),
        # Left along Row 11 to Column 3
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11),
        # Up Column 3 to Row 5 (standing next to switch at (2, 5))
        (3, 10), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5)
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
