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
    print("Starting flee_and_toggle.py...")
    # First, we are in battle right now, so flee!
    flee_battle_safe()
    
    # Path to (21, 2) on 3F East
    # From (23, 14) -> (25, 14) -> (25, 12) -> (21, 12) -> (21, 2)
    path = [
        (24, 14), (25, 14),
        (25, 13), (25, 12),
        (24, 12), (23, 12), (22, 12), (21, 12),
        (21, 11), (21, 10), (21, 9), (21, 8), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (21, 2)
    ]
    
    # Find our current position and resume walking
    pos = mgba.get_coordinates()
    # Check if we are still in battle or if we fled successfully
    print("Position after first flee:", pos)
    
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
        
    print("Reached (21, 2). Current position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
