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
    print("Initial Position on 3F East:", pos)
    
    # Strictly adjacent search path of pink checkered tiles:
    # Starting at (26, 3)
    path = [
        ("Right", (27, 3)),
        ("Down", (27, 4)),
        ("Left", (26, 4)),
        ("Left", (25, 4)),
        ("Down", (25, 5)),
        ("Right", (26, 5)),
        ("Right", (27, 5)),
        ("Right", (28, 5)),
        ("Up", (28, 4))
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
                
            # If coordinates changed drastically, we fell through the pitfall!
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            actual_dir = dir
            if abs(tx - cx) + abs(ty - cy) > 1:
                print("WARPED! Fell through the pitfall! New position:", pos)
                return
                
            new_pos = walk_step(actual_dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    time.sleep(1.0)
    print("Final position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
