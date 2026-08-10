import bridge
import time

# Walk from current position (1, 16) to Rest House 3 at (11, 11) using Column 2 to bypass Row 15 tree barrier
route = [
    (1, 16),
    (2, 16),
    (2, 15), (2, 14), # UP Column 2 to Row 14
    (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), # RIGHT along Row 14
    (11, 13), (11, 12), (11, 11) # UP Column 11 to Rest House 3 (door is at (11, 11))
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
print(f"Starting Rest House 3 path from {curr}")

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
            # Check if we can enter a building (if we are at the door at 11, 11)
            if target == (11, 11):
                print("Trying to press UP to enter Rest House 3...")
                bridge.press_buttons(["Up", "sleep 1000"])
                after_up = bridge.get_coordinates()
                if after_up != curr:
                    print(f"Entered Rest House 3 successfully! New coordinates: {after_up}")
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

print(f"Finished route. Final position: {bridge.get_coordinates()}")
