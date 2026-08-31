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
    
    # Path to (26, 6)
    path = [
        ("Right", (3, 6)),
        ("Up", (3, 5)),
        ("Right", (4, 5)),
        ("Up", (4, 4)),
        ("Up", (4, 3)),
        ("Up", (4, 2)),
        # Row 2 Right to Column 26
        ("Right", (5, 2)), ("Right", (6, 2)), ("Right", (7, 2)), ("Right", (8, 2)),
        ("Right", (9, 2)), ("Right", (10, 2)), ("Right", (11, 2)), ("Right", (12, 2)),
        ("Right", (13, 2)), ("Right", (14, 2)), ("Right", (15, 2)), ("Right", (16, 2)),
        ("Right", (17, 2)), ("Right", (18, 2)), ("Right", (19, 2)), ("Right", (20, 2)),
        ("Right", (21, 2)), ("Right", (22, 2)), ("Right", (23, 2)), ("Right", (24, 2)),
        ("Right", (25, 2)), ("Right", (26, 2)),
        # Down Column 26 to Row 6
        ("Down", (26, 3)),
        ("Down", (26, 4)),
        ("Down", (26, 5)),
        ("Down", (26, 6))
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
                
            # If coordinates changed drastically, we fell through pitfall!
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                # If we fell, we land on 1F East (coordinates around x=26, y=4 or 5)
                # But since the map changes, coordinates might be very different or we are not on 3F
                print("WARPED! Map transition detected during walk! Final Position:", pos)
                return
                
            new_pos = walk_step(actual_dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    pos = mgba.get_coordinates()
    print("Reached final target (26, 6)! Position:", pos)
    
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
