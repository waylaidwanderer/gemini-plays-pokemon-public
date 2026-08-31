import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Clear battle text
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Move cursor to RUN (Down then Right)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!"
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
            # We didn't move. Let's check for battle or block.
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still no movement, try to flee
                flee_battle_safe()
                time.sleep(0.5)

def main():
    # Currently at (10, 18) on 3F West in State B
    # Perfect State B path to the balcony drop
    path = [
        # Up Column 10 to Row 6
        (10, 17), (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11), (10, 10), (10, 9), (10, 8), (10, 7), (10, 6),
        # Right along Row 6 to Column 19
        (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6),
        # Down Column 19 to Row 12 (through open gate at 19, 8 in State B)
        (19, 7), (19, 8), (19, 9), (19, 10), (19, 11), (19, 12),
        # Right to Column 21 Row 12
        (20, 12), (21, 12),
        # Down Column 21 to Row 18 (through open gate at 21, 17 in State B)
        (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18),
        # Left along Row 18 to Column 19 (balcony drop!)
        (20, 18), (19, 18),
        # Down on (19, 18) to trigger the fall
        (19, 19)
    ]
    
    print("Starting ultimate State B balcony drop solution from (10, 18)...")
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Robust warp check: did our position change by more than 5 tiles in a single step?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. We fell through! Success!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
