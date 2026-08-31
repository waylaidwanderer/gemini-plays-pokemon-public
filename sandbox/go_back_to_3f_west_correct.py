import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
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
    # Currently at (11, 7)
    # Correct path: Right to Column 12, Down to Row 11, Left to Column 3 (switch)
    path = [
        # Move Right to Column 12
        (12, 7),
        # Move Down Column 12 to Row 11
        (12, 8), (12, 9), (12, 10), (12, 11),
        # Move Left Row 11 to Column 3
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    print("Starting correct walk down Column 12 to 3F West switch...")
    for target in path:
        walk_to_target(target)
        
    print("Reached switch area at (3, 11). Turning LEFT and toggling...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        
    print("All done! Current coordinates:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
