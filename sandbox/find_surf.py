import bridge
import time

# Walk from current position (5, 14) left to Column 0 Row 14, up Column 0 past tree wall, and right to Secret House
route = [
    (5, 14),
    (4, 14), (3, 14), (2, 14), (1, 14), (0, 14), # LEFT to Column 0 Row 14
    (0, 13), (0, 12), (0, 11), (0, 10), (0, 9), (0, 8), # UP Column 0 to Row 8
    (1, 8), (2, 8), (3, 8) # RIGHT along Row 8 to Column 3 (Secret House)
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
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
    print("RUN sequence finished.")

curr = bridge.get_coordinates()
print(f"Starting Secret House path along Column 0 from {curr}")

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
            # Check if we can enter a building (if we are at the door at 3, 8)
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

# Test entering the Secret House at (3, 8)
curr = bridge.get_coordinates()
if curr == (3, 8):
    print("Arrived at (3, 8). Pressing UP to enter Secret House...")
    bridge.press_buttons(["Up", "sleep 1000"])
    after_up = bridge.get_coordinates()
    print(f"Final coordinates: {after_up}")
else:
    print(f"Did not reach (3, 8). Current position: {curr}")
