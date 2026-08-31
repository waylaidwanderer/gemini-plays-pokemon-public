import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
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
    # Currently in battle at (4, 2). Flee first!
    flee_battle_safe()
    
    # Remaining path to switch at (2, 5) standing at (3, 5):
    path = [
        # Walk LEFT along Row 2 to Column 2
        (3, 2), (2, 2),
        # Walk DOWN Column 2 and 3 to stand at (3, 5)
        (2, 3), (2, 4), (3, 4), (3, 5)
    ]
    
    print("Starting path to switch area...")
    for target in path:
        walk_to_target(target)
        
    print("Reached switch area at (3, 5). Turning LEFT to face switch at (2, 5)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    print("Pressing A to interact with Mewtwo statue switch at (2, 5) to set to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Clear residual text / menu
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    print("Toggled switch. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
