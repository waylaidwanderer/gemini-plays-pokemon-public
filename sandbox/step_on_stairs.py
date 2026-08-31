import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Flee complete.")

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
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.3)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()
                time.sleep(0.3)

def main():
    print("Starting step_on_stairs.py...")
    # Walk from (25, 14) to (25, 16)
    # Then Left to (21, 16)
    # Then Down to (21, 17)
    path = [
        (25, 15), (25, 16),
        (24, 16), (23, 16), (22, 16), (21, 16),
        (21, 17)
    ]
    
    for target in path:
        walk_to_target(target)
        
    print("Final position reached:", mgba.get_coordinates())
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
