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
    
    # Path to (5, 10) on 3F West
    path = [
        ("Left", (12, 3)),
        # Down Column 12
        ("Down", (12, 4)), ("Down", (12, 5)), ("Down", (12, 6)), ("Down", (12, 7)),
        ("Down", (12, 8)), ("Down", (12, 9)), ("Down", (12, 10)),
        # Left along Row 10
        ("Left", (11, 10)), ("Left", (10, 10)), ("Left", (9, 10)), ("Left", (8, 10)),
        ("Left", (7, 10)), ("Left", (6, 10)), ("Left", (5, 10))
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
                
    # Final check of warp after stepping on (5, 10)
    time.sleep(1.0)
    print("Final Position after walk:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
