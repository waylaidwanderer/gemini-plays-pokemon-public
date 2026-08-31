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
    # Currently at (22, 16) on 1F East inside the fenced room.
    # We want to systematically walk to:
    # 1. (27, 11)
    # 2. (28, 11)
    # 3. (27, 9)
    # 4. (27, 8)
    
    # Path to (27, 11):
    # From (22, 16) -> (22, 14) -> (25, 14) -> (25, 12) -> (27, 12) -> (27, 11)
    path_to_27_11 = [
        (22, 15), (22, 14),
        (23, 14), (24, 14), (25, 14),
        (25, 13), (25, 12),
        (26, 12), (27, 12),
        (27, 11)
    ]
    
    # Path to (27, 8):
    # From (27, 12) (or nearby) -> (25, 12) -> (25, 7) -> (27, 7) -> (27, 8) -> (27, 9)
    path_to_27_8 = [
        (26, 12), (25, 12),
        (25, 11), (25, 10), (25, 9), (25, 8), (25, 7),
        (26, 7), (27, 7),
        (27, 8),
        (27, 9)
    ]
    
    print("Initial position:", mgba.get_coordinates())
    
    # Execute Path to 27, 11
    for target in path_to_27_11:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
            return
            
    # Execute Path to 27, 8
    for target in path_to_27_8:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
            return
            
    print("Search finished. Current position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
