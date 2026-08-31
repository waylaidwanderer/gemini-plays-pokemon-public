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
    print("Initial Position:", pos)
    
    # Path from (28, 5) to the southern half of 3F East
    # We want to go to (25, 2) first
    path = [
        ("Up", (28, 4)),
        ("Left", (27, 4)),
        ("Left", (26, 4)),
        ("Left", (25, 4)),
        ("Up", (25, 3)),
        ("Up", (25, 2)),
        # Row 2 Left to Column 21
        ("Left", (24, 2)),
        ("Left", (23, 2)),
        ("Left", (22, 2)),
        ("Left", (21, 2)),
        # Down Column 21 to Row 12
        ("Down", (21, 3)),
        ("Down", (21, 4)),
        ("Down", (21, 5)),
        ("Down", (21, 6)),
        ("Down", (21, 7)),
        ("Down", (21, 8)),
        ("Down", (21, 9)),
        ("Down", (21, 10)),
        ("Down", (21, 11)),
        ("Down", (21, 12)),
        # Right along Row 12 to Column 25
        ("Right", (22, 12)),
        ("Right", (23, 12)),
        ("Right", (24, 12)),
        ("Right", (25, 12)),
        # Down Column 25 to Row 14
        ("Down", (25, 13)),
        ("Down", (25, 14))
    ]
    
    # Let's find our current position in the path to support resume
    start_idx = 0
    min_dist = 9999
    for i, (dir, target) in enumerate(path):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Starting/resuming path from index {start_idx} (target: {path[start_idx][1]})")
    
    for idx in range(start_idx, len(path)):
        dir, target = path[idx]
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
                
            # If coordinates changed drastically, we fell!
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            if abs(tx - cx) + abs(ty - cy) > 2:
                print("WARPED! Map transition/fall detected! New position:", pos)
                return
                
            new_pos = walk_step(dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    print("Reached southern half target (25, 14)! Position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
