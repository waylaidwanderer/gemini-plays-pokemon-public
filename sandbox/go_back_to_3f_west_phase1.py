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
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # Phase 1: Walk from (21, 16) to (25, 2)
    path = [
        # Right to Column 25
        (22, 16), (23, 16), (24, 16), (25, 16),
        # Up Column 25 to Row 2 (passing through open gate at 25, 13)
        (25, 15), (25, 14), (25, 13), (25, 12), (25, 11), (25, 10), (25, 9), (25, 8), (25, 7), (25, 6), (25, 5), (25, 4), (25, 3), (25, 2)
    ]
    
    print("Starting Phase 1: Walk to (25, 2)...")
    for target in path:
        walk_to_target(target)
        
    print("Phase 1 complete! Current coordinates:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
