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
    path = [
        # Up to Row 6
        (21, 6),
        # Left to Column 10 Row 6
        (20, 6), (19, 6), (18, 6), (17, 6), (16, 6), (15, 6), (14, 6), (13, 6), (12, 6), (11, 6), (10, 6),
        # Down Column 10 to Row 11
        (10, 7), (10, 8), (10, 9), (10, 10), (10, 11),
        # Left along Row 11 to Column 3 Row 11
        (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    print("Starting walk_to_switch from current position...")
    for target in path:
        pos = mgba.get_coordinates()
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 5:
            print(f"Current pos {pos} is far from target {target}. Skipping.")
            continue
        walk_to_target(target)
        
    print("Walk finished. Final position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
