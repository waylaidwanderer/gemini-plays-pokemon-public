import bridge
import time

# Move back to (6, 20) and walk east along Row 20, testing DOWN on each Column from 10 to 21
route = [
    (1, 23),
    (1, 22), (1, 21), (1, 20),
    (2, 20), (3, 20), (4, 20), (5, 20), (6, 20) # Back to (6, 20)
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
print(f"Moving back to (6, 20) from {curr}...")

route_idx = 0
for idx, coord in enumerate(route):
    if curr == coord:
        route_idx = idx
        break

while route_idx < len(route):
    target = route[route_idx]
    curr = bridge.get_coordinates()
    
    if curr == target:
        route_idx += 1
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        break
        
    bridge.press_buttons([direction, "sleep 300"])
    new_curr = bridge.get_coordinates()
    if new_curr == curr:
        run_away()
        after_run = bridge.get_coordinates()
        if after_run != curr:
            for idx, coord in enumerate(route):
                if after_run == coord:
                    route_idx = idx
                    break

print(f"Arrived at (6, 20). Testing all columns from 10 to 21...")

# We will walk east along Row 20, and at each column, try to walk DOWN
for col in range(10, 22):
    # Walk to (col, 20)
    curr = bridge.get_coordinates()
    while curr[0] != col:
        direction = "Right" if col > curr[0] else "Left"
        bridge.press_buttons([direction, "sleep 300"])
        new_curr = bridge.get_coordinates()
        if new_curr == curr:
            run_away()
            new_curr = bridge.get_coordinates()
        curr = new_curr
        
    # Now try to walk DOWN from (col, 20)
    print(f"Testing Column {col} at {curr}...")
    # Try to walk down up to 5 steps
    temp_curr = curr
    can_go_down = False
    for step in range(1, 6):
        bridge.press_buttons(["Down", "sleep 300"])
        new_curr = bridge.get_coordinates()
        if new_curr == temp_curr:
            # Blocked!
            # If we made at least 1 step, check if we can go further or if we jumped a ledge!
            break
        else:
            print(f"  Successfully moved Down to {new_curr}")
            temp_curr = new_curr
            can_go_down = True
            
    if can_go_down:
        print(f"SUCCESS! Found a path down Column {col} to {temp_curr}!")
        break
    else:
        # Walk back up to row 20 if we didn't move but got turned or slightly shifted
        curr = bridge.get_coordinates()
        while curr[1] != 20:
            bridge.press_buttons(["Up", "sleep 300"])
            new_curr = bridge.get_coordinates()
            if new_curr == curr:
                run_away()
                new_curr = bridge.get_coordinates()
            curr = new_curr

print("Column testing finished.")
