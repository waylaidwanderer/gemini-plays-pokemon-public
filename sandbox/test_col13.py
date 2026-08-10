import bridge
import time

# Move back to (11, 12) if we are not there, then test the Column 13 route to the north!
curr = bridge.get_coordinates()
print(f"Starting Column 13 test from {curr}")

# If we are at (1, 23), walk UP to (1, 20), then right to (6, 20)
route = [
    (1, 23),
    (1, 22), (1, 21), (1, 20),
    (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), # Back to (6, 20)
    (6, 21), (6, 22), # DOWN to Row 22
    (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (12, 22), (13, 22), (14, 22), # Walk Right to Col 14
    (14, 21), (14, 20), # UP to Row 20
    (15, 20), (16, 20), (17, 20), # Walk Right past cliff
    (17, 21), (17, 22), # DOWN to Row 22
    (16, 22), (15, 22), (14, 22), (13, 22), (12, 22), (11, 22), (10, 22), (9, 22), (8, 22), (7, 22), (6, 22), (6, 21), (6, 20) # Dummy placeholder
]

# Wait, we are at (1, 23). Let's write a direct unblocked walk to (11, 12) from (1, 23):
# From (1, 23):
# - UP to (1, 20)
# - RIGHT to (6, 20)
# - UP stairs to (6, 16) (Wait! Climbing UP onto plateau is at (21, 17), but descending is at (6, 20)!
#   Wait, we can climb UP the west stairs at (6, 20) walking UP to (6, 19) -> (6, 16)!)
# - RIGHT across plateau to (21, 16)
# - DOWN stairs to (21, 18)
# - LEFT on row 18 to (11, 18)
# - UP to (11, 12)

go_back_route = [
    (1, 23),
    (1, 22), (1, 21), (1, 20),
    (2, 20), (3, 20), (4, 20), (5, 20), (6, 20),
    (6, 19), (6, 18), (6, 17), (6, 16), # Climb west stairs
    (7, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16), (20, 16), (21, 16), # Walk RIGHT across plateau
    (21, 17), (21, 18), # Descend stairs
    (20, 18), (19, 18), (18, 18), (17, 18), (16, 18), (15, 18), (14, 18), (13, 18), (12, 18), (11, 18), # LEFT on Row 18
    (11, 17), (11, 16), (11, 15), (11, 14), (11, 13), (11, 12) # UP to (11, 12)
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

# 1. Walk back to (11, 12)
route_idx = 0
for idx, coord in enumerate(go_back_route):
    if curr == coord:
        route_idx = idx
        break

while route_idx < len(go_back_route):
    target = go_back_route[route_idx]
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
            for idx, coord in enumerate(go_back_route):
                if after_run == coord:
                    route_idx = idx
                    break

print(f"Arrived back at (11, 12). Current: {bridge.get_coordinates()}")

# 2. Walk Column 13 route!
col13_route = [
    (11, 12),
    (11, 13), (11, 14), # Down to Row 14
    (12, 14), (13, 14), # Right to Column 13
    (13, 13), (13, 12), (13, 11), (13, 10), (13, 9), (13, 8), # UP Column 13 to Row 8
    (12, 8), (11, 8), (10, 8), (9, 8), (8, 8), (7, 8), (6, 8), (5, 8), (4, 8), (3, 8) # LEFT along Row 8 to Column 3 (Secret House)
]

route_idx = 0
while route_idx < len(col13_route):
    target = col13_route[route_idx]
    curr = bridge.get_coordinates()
    
    if curr == target:
        route_idx += 1
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        break
        
    print(f"Moving {direction} towards {target}")
    bridge.press_buttons([direction, "sleep 300"])
    new_curr = bridge.get_coordinates()
    if new_curr == curr:
        run_away()
        after_run = bridge.get_coordinates()
        if after_run != curr:
            for idx, coord in enumerate(col13_route):
                if after_run == coord:
                    route_idx = idx
                    break

print(f"Secret House door test complete. Final position: {bridge.get_coordinates()}")
