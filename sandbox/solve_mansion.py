import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Clear "Wild GRIMER appeared!" text
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
    # If currently in battle, let's flee first
    print("Starting solve_mansion path from current battle at (27, 12)...")
    flee_battle_safe()
    
    # Corrected State A path to the balcony drop via Column 25
    path = [
        # Left to Column 25 Row 12
        (26, 12), (25, 12),
        # Down Column 25 to Row 16 (through the open shutter gate at 25, 13)
        (25, 13), (25, 14), (25, 15), (25, 16),
        # Left along Row 16 to Column 21
        (24, 16), (23, 16), (22, 16), (21, 16),
        # Down Column 21 to Row 18
        (21, 17), (21, 18),
        # Left along Row 18 to Column 19 (balcony drop!)
        (20, 18), (19, 18),
        # Down on (19, 18) to trigger the fall
        (19, 19)
    ]
    
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
