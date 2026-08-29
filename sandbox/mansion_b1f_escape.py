import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

path = [
    ("Right", (25, 3)),
    ("Right", (26, 3)),
    ("Up", (26, 2)),
    ("Up", (26, 1)),
    ("Left", (25, 1)),
    ("Left", (24, 1)),
    ("Left", (23, 1)),
    ("Left", (22, 1)),
    ("Left", (21, 1)),
    ("Left", (20, 1)),
    ("Down", (20, 2)),
    ("Down", (20, 3)),
    ("Down", (20, 4)),
    ("Down", (20, 5)),
    ("Right", (21, 5)),
    ("Right", (22, 5))
]

print("Starting clean overworld escape walk...")
for direction, target in path:
    curr = get_pos()
    if curr == target:
        continue
    
    # Adjust direction dynamically if needed
    dx = abs(curr[0] - target[0])
    dy = abs(curr[1] - target[1])
    if dx + dy != 1:
        print(f"Off-path! At {curr}, next target is {target}")
        if curr[0] < target[0]: direction = "Right"
        elif curr[0] > target[0]: direction = "Left"
        elif curr[1] < target[1]: direction = "Down"
        elif curr[1] > target[1]: direction = "Up"
        else:
            continue
            
    print(f"Step: {direction} from {curr} to {target}")
    mgba.press_buttons([direction])
    time.sleep(0.6) # Wait for movement animation
    
    pos = get_pos()
    if pos != target:
        print(f"Movement failed! Expected {target}, got {pos}. Aborting script to avoid desync.")
        break
    else:
        print(f"  Reached {pos}")

print("Clean escape walk finished. Current position:", get_pos())
