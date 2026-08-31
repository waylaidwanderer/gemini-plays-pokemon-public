import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    time.sleep(1.0)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Pressing Down and Right to select RUN...")
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
            # Check if in battle or blocked
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still no movement, try to flee
                flee_battle_safe()
                new_pos = mgba.get_coordinates()
                if new_pos == pos:
                    print("Stuck or unable to move. Exiting.")
                    break

def main():
    # We start at (3, 11) in State B
    # Walk: Down to (3, 12), then Right along Row 12
    path = [
        (3, 12),
        (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12),
        (11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12),
        (18, 12), (19, 12), (20, 12), (21, 12), (22, 12), (23, 12), (24, 12), (25, 12)
    ]
    
    print("Testing Row 12 horizontal walkability...")
    for target in path:
        pos = mgba.get_coordinates()
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 2:
            print(f"BUMPED or BLOCKED at {pos}. Expected target was {target}.")
            break
        walk_to_target(target)
        
    print("Test finished. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
