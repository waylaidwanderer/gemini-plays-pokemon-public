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
    
    # 1. On 3F East, walk to (22, 1) stairs
    path_to_stairs = [
        ("Left", (23, 3)),
        ("Left", (22, 3)),
        ("Up", (22, 2)),
        ("Up", (22, 1)) # Stairs warp down to 2F East!
    ]
    
    for dir, target in path_to_stairs:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                print("WARPED! Descended to 2F East! New position:", pos)
                break
            new_pos = walk_step(actual_dir, target)
            if new_pos == pos:
                time.sleep(0.5)
        # If we warped, break the loop
        pos = mgba.get_coordinates()
        if pos['y'] > 3 or (pos['x'] != 22 and pos['x'] != 23):
            # We warped to 2F East
            break
            
    # Wait for map transition to complete
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Coordinates on 2F East:", pos)
    
    # 2. On 2F East/West, walk to (5, 10) stairs
    # Path: from wherever we are on 2F East, walk to Column 19 Row 2, then to Column 6 Row 2, then to (5, 10)
    # Let's define the path dynamically or step-by-step
    # Since we are on 2F East, let's walk:
    # - Left to Column 20 Row 2
    # - Left to Column 19 Row 2
    # - Down, Down, Right, Down, Down, Left, Down, Left to Column 6 Row 6 (Row 6 bypass)
    # - Left along Row 6 to Column 6
    # - Down Column 6 to (6, 11)
    # - Left to (5, 11)
    # - Up to (5, 10) (stairs UP to 3F West!)
    path_to_2f_stairs = [
        ("Left", (21, 2)), ("Left", (20, 2)), ("Left", (19, 2)),
        ("Down", (19, 3)), ("Down", (19, 4)),
        ("Right", (20, 4)),
        ("Down", (20, 5)), ("Down", (20, 6)),
        ("Left", (19, 6)), ("Left", (18, 6)), ("Left", (17, 6)), ("Left", (16, 6)),
        ("Left", (15, 6)), ("Left", (14, 6)), ("Left", (13, 6)), ("Left", (12, 6)),
        ("Left", (11, 6)), ("Left", (10, 6)), ("Left", (9, 6)), ("Left", (8, 6)),
        ("Left", (7, 6)), ("Left", (6, 6)),
        # Down Column 6
        ("Down", (6, 7)), ("Down", (6, 8)), ("Down", (6, 9)), ("Down", (6, 10)), ("Down", (6, 11)),
        ("Left", (5, 11)),
        ("Up", (5, 10)) # Stairs warp UP to 3F West!
    ]
    
    # Let's find where we are on 2F to start
    pos = mgba.get_coordinates()
    start_idx = 0
    min_dist = 9999
    for i, (dir, target) in enumerate(path_to_2f_stairs):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Starting 2F path from index {start_idx} (target: {path_to_2f_stairs[start_idx][1]})")
    for idx in range(start_idx, len(path_to_2f_stairs)):
        dir, target = path_to_2f_stairs[idx]
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                print("WARPED! Ascended to 3F West! New position:", pos)
                return
            new_pos = walk_step(actual_dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    time.sleep(1.5)
    print("Final Position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
