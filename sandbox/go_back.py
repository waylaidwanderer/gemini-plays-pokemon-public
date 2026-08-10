import bridge
import time

# Walk back to (11, 12) in front of Rest House 3 safely
route = [
    (1, 16),
    (2, 16), (3, 16),
    (3, 15), (3, 14), # UP to Row 14
    (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), # RIGHT along Row 14
    (11, 13), (11, 12) # UP to (11, 12)
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
print(f"Moving back to (11, 12) from {curr}...")

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

print(f"Arrived at: {bridge.get_coordinates()}")
