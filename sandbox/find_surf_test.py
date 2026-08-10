import bridge
import time

# Walk to Row 14, walk left to Column 5, and test walking UP Column 5 as far as possible
route = [
    (11, 12),
    (11, 13), (11, 14), # DOWN to Row 14
    (10, 14), (9, 14), (8, 14), (7, 14), (6, 14), (5, 14) # LEFT to Column 5
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
print(f"Starting Column 5 test from {curr}")

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

print(f"Arrived at Column 5 ground. Current: {bridge.get_coordinates()}")

# Test walking UP Column 5 from Row 14 to Row 8
curr = bridge.get_coordinates()
for y in range(13, 7, -1):
    print(f"Trying to move UP from {curr} towards (5, {y})...")
    bridge.press_buttons(["Up", "sleep 300"])
    new_curr = bridge.get_coordinates()
    print(f"Now at {new_curr}")
    if new_curr == curr:
        print(f"Blocked walking UP Column 5 at {curr}!")
        break
    curr = new_curr

print(f"Column 5 test complete. Final position: {bridge.get_coordinates()}")
