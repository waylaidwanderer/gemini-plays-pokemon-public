import bridge
import os
import time

# Clean up obsolete files as requested by critique
for file in ['find_surf_test.py', 'go_back.py', 'test_up_columns.py', 'find_secret_house.py']:
    try:
        if os.path.exists(file):
            os.remove(file)
            print(f"Cleaned up obsolete file: {file}")
    except Exception as e:
        print(f"Error deleting {file}: {e}")

# Consolidated efficient route to Secret House door at (3, 8)
route = [
    (18, 4),
    (18, 5), (18, 6), (18, 7), (18, 8), # DOWN to row 8
    (17, 8), (16, 8), (15, 8), (14, 8), (13, 8), (12, 8), (11, 8), # LEFT to col 11
    (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), # DOWN to row 14
    (10, 14), (9, 14), (8, 14), (7, 14), (6, 14), (5, 14), (4, 14), (3, 14), (2, 14), (1, 14), (0, 14), # LEFT to col 0
    (0, 13), (0, 12), (0, 11), (0, 10), (0, 9), (0, 8), # UP to row 8
    (1, 8), (2, 8), (3, 8) # RIGHT to Secret House door
]

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

def run_away():
    print("Wild battle/interaction detected! Escuting RUN sequence...")
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    print("RUN sequence finished.")

curr = bridge.get_coordinates()
print(f"Starting Secret House run from {curr}")

route_idx = 0
for idx, coord in enumerate(route):
    if curr == coord:
        route_idx = idx
        break

print(f"Matched route index: {route_idx}")

stuck_count = 0
max_stuck = 3

while route_idx < len(route):
    target = route[route_idx]
    curr = bridge.get_coordinates()
    
    if curr == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    bridge.press_buttons([direction, "sleep 300"])
    
    new_curr = bridge.get_coordinates()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            # Check if we can enter the Secret House at (3, 8)
            if target == (3, 8):
                print("Trying to press UP to enter Secret House...")
                bridge.press_buttons(["Up", "sleep 1000"])
                after_up = bridge.get_coordinates()
                if after_up != curr:
                    print(f"Entered Secret House successfully! New coordinates: {after_up}")
                    break
                    
            run_away()
            after_run = bridge.get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        break
            stuck_count = 0
    else:
        stuck_count = 0

# If we reached (3, 8), try entering
curr = bridge.get_coordinates()
if curr == (3, 8):
    print("Arrived at (3, 8). Pressing UP to enter Secret House...")
    bridge.press_buttons(["Up", "sleep 1000"])
    after_up = bridge.get_coordinates()
    print(f"Final coordinates: {after_up}")
else:
    print(f"Did not reach (3, 8). Current position: {curr}")
