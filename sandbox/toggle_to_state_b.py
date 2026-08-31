import mgba
import time

def flee_battle():
    print("Wild battle! Fleeing...")
    # Clean up screen text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear "Got away safely!"
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(direction, target):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    print(f"Current: ({cx}, {cy}) | Pressing {direction} to go to {target}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Check for battle
        print("No movement, checking for battle...")
        flee_battle()
        new_pos = mgba.get_coordinates()
    return new_pos

def main():
    pos = mgba.get_coordinates()
    print("Initial Position on 3F West:", pos)
    
    # Strictly adjacent steps from (11, 10) to the switch stand at (2, 6):
    path = [
        ("Left", (10, 10)),
        ("Up", (10, 9)),
        ("Up", (10, 8)),
        ("Up", (10, 7)),
        ("Up", (10, 6)),
        ("Up", (10, 5)),
        ("Up", (10, 4)),
        ("Up", (10, 3)),
        ("Left", (9, 3)),
        ("Left", (8, 3)),
        ("Left", (7, 3)),
        ("Left", (6, 3)),
        ("Left", (5, 3)),
        ("Left", (4, 3)),
        ("Down", (4, 4)),
        ("Down", (4, 5)),
        ("Left", (3, 5)),
        ("Down", (3, 6)),
        ("Left", (2, 6))
    ]
    
    # Find our current position in the path (to handle resume if needed)
    start_idx = 0
    min_dist = 9999
    for i, (dir, target) in enumerate(path):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Resuming path from index {start_idx} / {len(path)-1} (target: {path[start_idx][1]})")
    
    for idx in range(start_idx, len(path)):
        dir, target = path[idx]
        pos = mgba.get_coordinates()
        # If we are already at the target, skip
        if pos['x'] == target[0] and pos['y'] == target[1]:
            continue
            
        # Try to step to the target
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
                
            # If we are completely off-track, recalculate direction dynamically
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                # Recalculate adjacent direction
                if tx > cx: actual_dir = "Right"
                elif tx < cx: actual_dir = "Left"
                elif ty > cy: actual_dir = "Down"
                elif ty < cy: actual_dir = "Up"
                
            new_pos = walk_step(actual_dir, target)
            if new_pos == pos:
                # We are blocked, try to clear battle or retry
                time.sleep(0.5)
                
    # Now stand at (2, 6) and face UP
    print("Facing Up to look at the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch (4 A-presses)
    print("Toggling Mewtwo Switch...")
    for press in range(1, 5):
        print(f"A-press {press}...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    print("Successfully toggled switch to State B!")
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
