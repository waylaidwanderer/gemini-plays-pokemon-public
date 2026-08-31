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

def walk_to_target_robust(target):
    retries = 0
    while retries < 3:
        pos = mgba.get_coordinates()
        if pos['x'] == target[0] and pos['y'] == target[1]:
            print(f"Reached target {target}")
            return True
            
        direction = get_dir(pos, target)
        if not direction:
            return False
            
        print(f"Current: ({pos['x']}, {pos['y']}) | Moving {direction} to target {target} (attempt {retries+1})")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Check if we got into a battle
            print("No movement. Pressing B to dismiss any dialogue or see if battle opened...")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos2 = mgba.get_coordinates()
            if new_pos2 == pos:
                # Still didn't move, let's try to flee battle
                flee_battle_safe()
                time.sleep(0.5)
                new_pos3 = mgba.get_coordinates()
                if new_pos3 == pos:
                    # Still didn't move, increment retries (could be a wall)
                    retries += 1
                else:
                    # We were in battle and fled, or were moved! Continue walking
                    print("Recovered from battle/movement. Continuing...")
            else:
                print("Recovered after pressing B. Continuing...")
        else:
            # We successfully moved! Reset retries and continue loop
            retries = 0

    print(f"Target {target} is blocked (wall/obstacle).")
    return False

def main():
    # Currently at (26, 3) on 3F East in State B.
    # We want to walk down Column 26 to Row 12, then LEFT along Row 12 to Column 21.
    path_down = [
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12)
    ]
    
    path_left = [
        (25, 12), (24, 12), (23, 12), (22, 12), (21, 12)
    ]
    
    pos = mgba.get_coordinates()
    print("Initial position:", pos)
    
    # 1. Walk down Column 26
    print("Walking down Column 26 to Row 12...")
    for target in path_down:
        success = walk_to_target_robust(target)
        if not success:
            print("Failed to walk down Column 26!")
            break
            
    # 2. Walk LEFT along Row 12
    pos = mgba.get_coordinates()
    if pos['y'] == 12:
        print("Walking left along Row 12...")
        for target in path_left:
            success = walk_to_target_robust(target)
            if not success:
                print("Failed to walk left along Row 12!")
                break
                
    print("Search finished. Current position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
