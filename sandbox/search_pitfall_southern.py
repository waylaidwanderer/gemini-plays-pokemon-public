import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Dismiss any text with B
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
    # We start at (26, 12).
    # Sweep path covering rows 14, 15, 16 and columns 22 to 27
    path = [
        # Down Column 26 to Row 14
        (26, 13), (26, 14),
        # Sweep Row 14 (Right then Left)
        (27, 14), (26, 14), (25, 14), (24, 14), (23, 14), (22, 14),
        # Down to Row 15
        (22, 15),
        # Sweep Row 15 (Right)
        (23, 15), (24, 15), (25, 15), (26, 15), (27, 15),
        # Down to Row 16
        (27, 16),
        # Sweep Row 16 (Left)
        (26, 16), (25, 16), (24, 16), (23, 16), (22, 16)
    ]
    
    print("Starting comprehensive pitfall search in southern 3F East...")
    for target in path:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check: did our position change drastically?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. We fell through a pitfall!")
            break
            
    print("Search finished. Current position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
