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
            # We didn't move. Let's check for battle or block.
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still no movement, try to flee
                flee_battle_safe()
                time.sleep(0.5)
                # Let the loop continue and try the movement again!

def main():
    # If we are currently in battle, let's flee first
    print("Fleeing current battle first...")
    flee_battle_safe()
    
    # We should be around (10, 16) or (10, 17)
    # Phase 1: Walk back to switch at (3, 11) on 3F West
    path_to_switch = [
        # Up Column 10 to Row 11
        (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11),
        # Left along Row 11 to Column 3
        (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    print("PHASE 1: Walking to switch at (2, 11)...")
    for target in path_to_switch:
        pos = mgba.get_coordinates()
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 5:
            # Skip if we are already past it
            continue
        walk_to_target(target)
        
    # Phase 2: Toggle switch to State A
    # Make sure we are at (3, 11)
    walk_to_target((3, 11))
    
    print("PHASE 2: Turning Left to face Mewtwo statue...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    print("Toggling switch to State A...")
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 300", "A", "sleep 300", "A", "sleep 300"])
    time.sleep(1.0)
    
    # Phase 3: Walk to the balcony drop in State A
    path_to_balcony = [
        # Right along Row 11 to Column 10
        (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
        # Down Column 10 to Row 16
        (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
        # Right along Row 16 to Column 20
        (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16), (20, 16),
        # Down to (20, 17) (open gate in State A!)
        (20, 17),
        # Left to (19, 17)
        (19, 17),
        # Down to (19, 18) (balcony drop!)
        (19, 18)
    ]
    
    print("PHASE 3: Walking to the balcony drop...")
    for target in path_to_balcony:
        pos = mgba.get_coordinates()
        # If coordinates changed drastically, we fell through to B1F West!
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 5:
            print("WARPED! We fell through to B1F West! Success!")
            break
        walk_to_target(target)
        
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
