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
        # Up to Row 3
        (26, 5), (26, 4), (26, 3),
        # Left Row 3 to Column 21
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3),
        # Down Column 21 to Row 6
        (21, 4), (21, 5), (21, 6),
        # Left Row 6 to Column 19
        (20, 6), (19, 6),
        # Down Column 19 to Row 12 (since gate at 19,8 is open in State B)
        (19, 7), (19, 8), (19, 9), (19, 10), (19, 11), (19, 12),
        # Right on Row 12 to Column 25
        (20, 12), (21, 12), (22, 12), (23, 12), (24, 12), (25, 12),
        # Try to explore around (25,12), (26,12), (27,12), (28,12)
        (26, 12), (27, 12), (28, 12)
    ]
    
    print("Starting search for pitfall in southern room of 3F East in State B...")
    for target in path:
        pos = mgba.get_coordinates()
        # If we fell, we land on 1F East inside the fenced room.
        # Check if coordinates changed drastically from the expected target.
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 5:
            print(f"Warped! Position {pos} is far from expected target {target}. We must have fallen!")
            break
            
        walk_to_target(target)
        
    print("Search finished. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
