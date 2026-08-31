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
    
    # We are at (12, 8). Let's go to (12, 11)
    path = [
        ("Down", (12, 9)),
        ("Down", (12, 10)),
        ("Down", (12, 11)),
        # Left to Column 10
        ("Left", (11, 11)),
        ("Left", (10, 11)),
        # Down Column 10 to Row 16
        ("Down", (10, 12)),
        ("Down", (10, 13)),
        ("Down", (10, 14)),
        ("Down", (10, 15)),
        ("Down", (10, 16)),
        # Try to walk Right to Column 20 along Row 16
        ("Right", (11, 16)),
        ("Right", (12, 16)),
        ("Right", (13, 16)),
        ("Right", (14, 16)),
        ("Right", (15, 16)),
        ("Right", (16, 16)),
        ("Right", (17, 16)),
        ("Right", (18, 16)),
        ("Right", (19, 16)),
        ("Right", (20, 16)),
        # Walk DOWN to (20, 17) and Left to (19, 18)
        ("Down", (20, 17)),
        ("Left", (19, 17)),
        ("Down", (19, 18))
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
                
            # If coordinates changed drastically, we fell through balcony drop!
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                print("WARPED! Fell through balcony drop! New position:", pos)
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
