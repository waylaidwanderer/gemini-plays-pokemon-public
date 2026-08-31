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
    
    # Path from (28, 7) to (12, 11) on 3F
    path = [
        ("Up", (28, 6)),
        ("Up", (28, 5)),
        ("Left", (27, 5)),
        ("Left", (26, 5)),
        ("Left", (25, 5)),
        ("Up", (25, 4)),
        ("Up", (25, 3)),
        ("Up", (25, 2)),
        # Row 2 Left to Column 12
        ("Left", (24, 2)), ("Left", (23, 2)), ("Left", (22, 2)), ("Left", (21, 2)),
        ("Left", (20, 2)), ("Left", (19, 2)), ("Left", (18, 2)), ("Left", (17, 2)),
        ("Left", (16, 2)), ("Left", (15, 2)), ("Left", (14, 2)), ("Left", (13, 2)),
        ("Left", (12, 2)),
        # Down Column 12 to Row 11
        ("Down", (12, 3)), ("Down", (12, 4)), ("Down", (12, 5)), ("Down", (12, 6)),
        ("Down", (12, 7)), ("Down", (12, 8)), ("Down", (12, 9)), ("Down", (12, 10)),
        ("Down", (12, 11))
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
                
            # If coordinates changed drastically, we warped
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                print("WARPED! Map transition detected! New position:", pos)
                return
                
            new_pos = walk_step(actual_dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    # We reached (12, 11)
    pos = mgba.get_coordinates()
    print("Reached (12, 11)! Current position:", pos)
    
    # Take screenshot of the area
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
