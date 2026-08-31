import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Dismiss transition text
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Select RUN
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!"
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
    print("Fleeing current battle first...")
    flee_battle_safe()
    
    # Path from (26, 12) to balcony drop
    path = [
        # Left along Row 12 to Column 21
        (25, 12), (24, 12), (23, 12), (22, 12), (21, 12),
        # Down Column 21 to Row 18 (passing open gate at 21, 17)
        (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18),
        # Left along Row 18 to Column 19
        (20, 18), (19, 18),
        # Down from (19, 18) to drop
        (19, 19)
    ]
    
    print("Walking correct State B route to balcony...")
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. We fell through! Success!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
