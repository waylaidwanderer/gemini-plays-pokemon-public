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

def toggle_switch_to_b():
    print("Toggling switch back to State B...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print("Switch toggled back to State B.")

def main():
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # We are currently at (2, 11).
    # Step 1: Toggle the switch at (2, 11) to State B
    toggle_switch_to_b()
    
    # Step 2: Walk to (2, 6)
    path_to_northern_switch = [
        (3, 11),
        (4, 11),
        (4, 10), (4, 9), (4, 8), (4, 7), (4, 6),
        (3, 6), (2, 6)
    ]
    
    for target in path_to_northern_switch:
        walk_to_target(target)
        
    print("Finished. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
