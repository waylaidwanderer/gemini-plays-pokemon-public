import mgba
import time
from collections import deque

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
    # Currently at (2, 11) on 3F West in State B.
    # Initial path to northeastern room at (26, 3):
    path_to_ne = [
        # Walk to Column 12 on Row 11
        (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Walk UP Column 12 to Row 3
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
        # Walk RIGHT along Row 3 to Column 26
        (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3)
    ]
    
    print("Walking to northeastern room at (26, 3)...")
    for target in path_to_ne:
        walk_to_target(target)
        
    print("Reached (26, 3). Now pathfinding to balcony at (19, 18) in State B...")
    # Since we are in State B, let's systematically walk to the balcony using pathfinder_to_northeast.py approach or similar.
    # We will walk on:
    # UP to Column 21 Row 3? No, we are at (26, 3).
    # In State B:
    # Shutter gate at (25, 13) is CLOSED.
    # Balcony gate at (21, 17) is OPEN!
    # Let's try the State B path manually defined in notes:
    # "Walk UP Column 21 to Row 3, RIGHT to Column 23, DOWN Column 23 to Row 12, LEFT Row 12 to Column 21, DOWN Column 21 to Row 18, LEFT Row 18 to Column 19, and drop!"
    # Since we start at (26, 3), we can walk:
    # - (25, 3), (24, 3), (23, 3)
    # - DOWN Column 23 to Row 12 (if Row 4 Column 23 is open or bypassable)
    # - If we can't go down Column 23, let's explore all walkable routes dynamically!
    
    # We will write a BFS pathfinder here that dynamically probes and builds the route to (19, 18):
    # (Since wild battles might occur, we can just define a robust sequential list of candidate paths and let get_dir handle it!)
    # Let's define the candidate path to balcony:
    path_to_balcony = [
        # From (26, 3), walk to (23, 3)
        (25, 3), (24, 3), (23, 3),
        # Walk down Column 23 to Row 12
        (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12),
        # Walk left along Row 12 to Column 21
        (22, 12), (21, 12),
        # Walk down Column 21 to Row 18 (gate at (21, 17) is OPEN in State B!)
        (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18),
        # Walk left to (19, 18)
        (20, 18), (19, 18),
        # Step down to trigger drop!
        (19, 19)
    ]
    
    print("Walking path to balcony drop...")
    for target in path_to_balcony:
        pos_before = mgba.get_coordinates()
        walk_to_target(target)
        pos_after = mgba.get_coordinates()
        
        # Warp check: did our floor change drastically?
        if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED! From {pos_before} to {pos_after}. Map transition successful!")
            break
            
    print("Finished path. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
