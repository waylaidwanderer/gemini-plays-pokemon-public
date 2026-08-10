import bridge
import time

# Walk from (10, 23) down to Row 26, then Right to Column 19, then UP to find the Gold Teeth!
route = [
    (10, 23),
    (10, 24), (10, 25), (10, 26), # DOWN Column 10 to Row 26
    (11, 26), (12, 26), (13, 26), (14, 26), (15, 26), (16, 26), (17, 26), (18, 26), (19, 26), # RIGHT to Column 19
    (19, 25), (19, 24), (19, 23), (19, 22), (19, 21), (19, 20), (19, 19), (19, 18), (19, 17) # UP Column 19 to Row 17
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
print(f"Starting Gold Teeth search from {curr}")

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
            # Check if we are stuck because of an overworld item ball
            # Let's try pressing A to see if we can pick up the item!
            print("Trying to press A to pick up item...")
            bridge.press_buttons(["A", "sleep 1000"])
            
            # Dismiss any dialog with B presses
            print("Dismissing any dialog...")
            bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
            
            # Recheck coordinates
            after_a_curr = bridge.get_coordinates()
            if after_a_curr != curr:
                print(f"Moved/cleared block! New coordinates: {after_a_curr}")
                # Re-align
                for idx, coord in enumerate(route):
                    if after_a_curr == coord:
                        route_idx = idx
                        break
                stuck_count = 0
                continue
                
            # If still stuck, try running away
            run_away()
            after_run = bridge.get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        print(f"Re-aligned with route at index {route_idx}")
                        break
            stuck_count = 0
    else:
        stuck_count = 0

print(f"Teeth search finished. Final position: {bridge.get_coordinates()}")
