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
            return True
            
        direction = get_dir(pos, target)
        if not direction:
            return False
            
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We bumped! This means target is blocked in this direction.
            # Clear text/battle if needed
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos2 = mgba.get_coordinates()
            if new_pos2 == pos:
                flee_battle_safe()
                time.sleep(0.5)
                new_pos2 = mgba.get_coordinates()
            return False

def main():
    # Currently at (22, 3) on 3F East.
    # Let's dynamically test different possible vertical columns to see if we can go down!
    # We will test Column 23 first:
    print("Testing Column 23...")
    # Walk to (23, 3)
    walk_to_target((23, 3))
    pos = mgba.get_coordinates()
    print("Position:", pos)
    
    # Try to step Down to (23, 4)
    print("Trying to step Down to (23, 4)...")
    success_23 = walk_to_target((23, 4))
    pos_after = mgba.get_coordinates()
    print(f"Step to (23, 4) success: {success_23} | Position: {pos_after}")
    
    # If blocked, walk back to (22, 3) and try Column 26:
    if pos_after['y'] == 3:
        print("Column 23 is indeed blocked at Row 4. Walk back to (22, 3) and test Column 26...")
        walk_to_target((22, 3))
        walk_to_target((23, 3))
        walk_to_target((24, 3))
        walk_to_target((25, 3))
        walk_to_target((26, 3))
        
        print("Trying to step Down to (26, 4)...")
        success_26 = walk_to_target((26, 4))
        pos_after_26 = mgba.get_coordinates()
        print(f"Step to (26, 4) success: {success_26} | Position: {pos_after_26}")
        
        if pos_after_26['y'] == 4:
            print("Step to (26, 4) succeeded! Let's see if we can walk DOWN Column 26 past Row 13...")
            # Walk down Column 26 to Row 12
            for row in range(5, 13):
                walk_to_target((26, row))
            print("Position at Row 12:", mgba.get_coordinates())
            
            # Try to step Down to (26, 13)
            print("Trying to step Down to (26, 13)...")
            success_13 = walk_to_target((26, 13))
            print(f"Step to (26, 13) success: {success_13} | Position: {mgba.get_coordinates()}")
            
    # Save final screen
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
