import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def run_away():
    print("Wild battle detected! Running away...")
    # Clear any battle entrance animation text
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 350"])
    
    # Try running away using Right-Down-A
    # (The RUN button is in the bottom right corner of the battle menu)
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1500"])
    
    # Press B to clear "Got away safely!" or handle failed run attempts
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 350"])

# Target path nodes:
# Start: (26, 16)
# Node 1: (22, 16)  (Walk Left)
# Node 2: (22, 18)  (Walk Down)
# Node 3: (6, 18)   (Walk Left)
# Node 4: (6, 11)   (Walk Up)
# Node 5: (0, 11)   (Walk Left) - this should trigger transition to Area 3 (West) at (29, 23)

path = [
    (22, 16),
    (22, 18),
    (6, 18),
    (6, 11),
    (0, 11)
]

print("Starting walk_to_area3.py...")
node_idx = 0

while node_idx < len(path):
    tx, ty = path[node_idx]
    cx, cy = get_pos()
    print(f"Current: ({cx}, {cy}) -> Target: ({tx}, {ty})")
    
    if cx == tx and cy == ty:
        print(f"Reached node {node_idx}: ({tx}, {ty})")
        node_idx += 1
        continue
        
    # Check if we transitioned to Area 3 (West).
    # If cx is around 29 or 30 and cy is around 23, we transitioned!
    if cx >= 28 and cy == 23:
        print(f"Transitioned to Area 3 (West)! Position: ({cx}, {cy})")
        break
        
    # Determine next move direction
    if cx < tx:
        btn = "Right"
    elif cx > tx:
        btn = "Left"
    elif cy < ty:
        btn = "Down"
    else:
        btn = "Up"
        
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn, "sleep 400"])
    
    nx, ny = get_pos()
    if nx == cx and ny == cy:
        # We didn't move!
        print("Did not move. Checking for wild battle...")
        # Take a screenshot to help debug if needed
        mgba.take_screenshot()
        run_away()
        # Check coordinates again
        ax, ay = get_pos()
        if ax == cx and ay == cy:
            print("Still stuck. Pressing B...")
            mgba.press_buttons(["B", "sleep 300"])

print("Finished walk_to_area3.py.")
