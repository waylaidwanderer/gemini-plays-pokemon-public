import mgba
import time

def walk_to_target(path):
    print("Starting walk...")
    for target in path:
        pos = mgba.get_coordinates()
        print(f"Current pos: {pos}, Target: {target}")
        dx = target[0] - pos['x']
        dy = target[1] - pos['y']
        
        # We should only move one step at a time
        if abs(dx) + abs(dy) != 1:
            print(f"Error: Target {target} is not 1 step away from {pos}")
            return False
            
        if dx == 1:
            btn = "Right"
        elif dx == -1:
            btn = "Left"
        elif dy == 1:
            btn = "Down"
        elif dy == -1:
            btn = "Up"
        else:
            print("Already there?")
            continue
            
        mgba.press_buttons([btn])
        time.sleep(0.3) # Wait for movement animation and potential battle trigger
        
        # Verify if we reached the target
        new_pos = mgba.get_coordinates()
        if new_pos != pos:
            # We moved!
            if new_pos == {'x': target[0], 'y': target[1]}:
                print(f"Successfully reached {target}")
            else:
                print(f"Moved, but landed on unexpected tile {new_pos} (intended {target})")
                return False
        else:
            # We didn't move. Could be:
            # 1. Bounded by wall
            # 2. Battle started!
            # Let's take a screenshot to check
            screenshot = mgba.take_screenshot()
            print(f"Failed to move from {pos} to {target}. Captured screenshot.")
            return False
            
    print("Finished path successfully!")
    return True

path = [
    (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),
    (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11)
]

walk_to_target(path)
