import time
import os
import sys
import bridge

route = [(15, 25), (15, 24), (15, 23), (15, 22), (15, 21), (16, 21), (17, 21), (18, 21), (19, 21), (20, 21), (21, 21), (22, 21), (22, 20), (22, 19), (22, 18), (22, 17), (22, 16), (22, 15), (22, 14), (22, 13), (22, 12), (22, 11), (22, 10), (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (30, 10), (0, 22), (0, 23), (0, 24), (1, 24), (2, 24), (3, 24), (4, 24), (5, 24), (6, 24), (7, 24), (8, 24), (9, 24), (10, 24), (11, 24), (12, 24), (13, 24), (14, 24), (16, 24), (17, 24), (18, 24), (19, 24), (20, 24), (20, 23), (20, 22), (20, 20), (19, 20), (18, 20), (17, 20), (16, 20), (15, 20), (14, 20), (13, 20), (12, 20), (12, 21), (12, 22), (11, 22), (10, 22), (9, 22), (8, 22), (8, 21), (8, 20), (8, 19), (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (12, 7), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (17, 7), (17, 8), (18, 8), (19, 8), (20, 8), (20, 7), (20, 6), (20, 5), (20, 4), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (-1, 5), (39, 31), (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31), (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31), (23, 31), (22, 31), (22, 30), (22, 29), (22, 28), (22, 27), (22, 26), (22, 25), (22, 24), (22, 23), (22, 22), (21, 22), (19, 22), (18, 22), (17, 22), (16, 22), (16, 23), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31), (16, 32), (16, 33), (15, 33), (14, 33), (13, 33), (12, 33), (11, 33), (10, 33), (9, 33), (9, 34), (9, 35), (9, 36), (9, 0), (9, 1), (9, 2), (9, 4), (9, 5), (9, 6), (9, 7), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (7, 13), (6, 13), (5, 13), (4, 13), (3, 13), (2, 13), (1, 13), (0, 13), (29, 25), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26), (21, 26), (20, 26), (19, 26), (19, 25), (19, 23), (19, 19), (19, 18), (19, 17), (18, 26), (17, 26), (15, 26), (14, 26), (13, 26), (12, 26), (11, 26), (10, 26), (9, 26), (8, 26), (7, 26), (6, 26), (5, 26), (5, 25), (5, 23), (5, 22), (5, 21), (5, 20), (5, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14)]

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx:
        return 'Right'
    if tx < cx:
        return 'Left'
    if ty > cy:
        return 'Down'
    if ty < cy:
        return 'Up'
    return None

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # First press B multiple times to clear the wild battle dialogue
    for i in range(5):
        print(f"Dismissing battle intro text ({i+1}/5)...")
        bridge.press_buttons(["B"])
        time.sleep(0.4)
    # Perform RUN sequence: Right, Down, A
    print("Pressing RUN options...")
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A"])
    time.sleep(2.0)
    print("RUN sequence finished.")

def run_safari_loop(max_steps=40):
    print(f"Starting Golden Speedrun (limit: {max_steps} steps)...")
    stuck_count = 0
    max_stuck = 3
    steps_taken = 0
    
    while True:
        if steps_taken >= max_steps:
            print(f"Reached max steps limit of {max_steps}. Pausing to return control.")
            break
            
        curr = bridge.get_coordinates()
        if curr is None:
            print("Could not read coordinates (we are likely in a battle or transition). Waiting...")
            time.sleep(0.5)
            continue
            
        print(f"Current Coordinates: {curr}")
        
        # Check if we arrived at the final target (5, 14)
        if curr == (5, 14):
            print("Arrived at final target (5, 14) outside Secret House! Entering...")
            bridge.press_buttons(["Up"])
            time.sleep(1.0)
            new_curr = bridge.get_coordinates()
            print(f"Entered Secret House! New coordinates: {new_curr}")
            break
            
        # Find index in route
        if curr not in route:
            print(f"Error: Current position {curr} not in route. Exiting.")
            sys.exit(1)
            
        idx = route.index(curr)
        print(f"Matched route index: {idx}/{len(route)-1}")
        
        # Determine next target
        target = route[idx + 1]
        print(f"Next Target: {target}")
        
        # Get direction
        direction = get_dir(curr, target)
        if direction is None:
            print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
            sys.exit(1)
            
        print(f"Moving {direction} towards {target}...")
        bridge.press_buttons([direction])
        time.sleep(0.6) # Wait 600ms to ensure coordinates fully update in emulator
        steps_taken += 1
        
        # Verify if we successfully moved
        new_curr = bridge.get_coordinates()
        if new_curr == curr:
            stuck_count += 1
            print(f"Stuck! Didn't move. Current {curr}. Stuck count: {stuck_count}")
            
            # If stuck at Gold Teeth coordinate, press A
            if curr == (19, 25):
                print("Trying to press A to pick up Gold Teeth...")
                bridge.press_buttons(["A"])
                time.sleep(1.0)
                stuck_count = 0
                continue
                
            if stuck_count >= max_stuck:
                # We are stuck, likely in a battle
                run_away()
                stuck_count = 0
                # Don't count stuck/battle steps as successful movement steps
                steps_taken = max(0, steps_taken - 1)
        else:
            stuck_count = 0

if __name__ == "__main__":
    run_safari_loop()
