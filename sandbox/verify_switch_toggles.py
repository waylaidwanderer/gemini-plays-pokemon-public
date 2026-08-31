import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
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
    # Currently at (23, 3) on 3F East in State B.
    # Walk back to the switch at (2, 5) on 3F West:
    path_to_switch = [
        # Walk LEFT along Row 3 to Column 12
        (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
        # Up Column 12 to Row 2
        (12, 2),
        # Left Row 2 to Column 4
        (11, 2), (10, 2), (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2),
        # Down Column 4 and 3 to (3, 5)
        (4, 3), (4, 4), (4, 5), (3, 5)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path_to_switch):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Walking to switch from index {start_idx} (target: {path_to_switch[start_idx]})")
    for idx in range(start_idx, len(path_to_switch)):
        target = path_to_switch[idx]
        walk_to_target(target)
        
    print("Reached (3, 5). Turning LEFT to face switch at (2, 5)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.8)
    
    # Capture BEFORE screenshot
    print("Capturing BEFORE toggle screenshot...")
    scr_before = mgba.take_screenshot()
    
    # Toggle switch (exactly 6 A presses + 1 B press)
    print("Toggling switch...")
    mgba.press_buttons(["A"]) # Page 1: "A mysterious switch!"
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # Page 2: "Who'd press it?"
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # Chose Yes on Yes/No prompt -> "Who wouldn't?"
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # Page 4: "Pressed it!"
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # Page 5: "Shutter gates..."
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # Clear dialogue
    time.sleep(0.5)
    mgba.press_buttons(["B"]) # Residual clear
    time.sleep(1.0)
    
    # Capture AFTER screenshot
    print("Capturing AFTER toggle screenshot...")
    scr_after = mgba.take_screenshot()
    
    print("Switch toggle sequence completed.")
    print("BEFORE screenshot:", scr_before)
    print("AFTER screenshot:", scr_after)

if __name__ == "__main__":
    main()
