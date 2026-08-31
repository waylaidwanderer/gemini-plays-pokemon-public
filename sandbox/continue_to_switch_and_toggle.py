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
    # Currently at (4, 4) on 3F West.
    # Walk to (3, 5):
    path_to_switch = [
        (4, 5), (3, 5)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    for target in path_to_switch:
        walk_to_target(target)
        
    print("Reached (3, 5). Turning LEFT to face switch at (2, 5)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.8)
    
    # Toggle switch to State A (using 8 A/B presses to ensure dialogue is fully cleared!)
    print("Toggling switch to State A...")
    for i in range(8):
        mgba.press_buttons(["A"])
        time.sleep(0.6)
    
    # Clear residual dialog
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print("Toggled switch to State A. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
