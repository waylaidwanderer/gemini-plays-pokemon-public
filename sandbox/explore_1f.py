import mgba
import time

# We are at (22, 3) on 1F East.
# Let's explore the walkable area of 1F East to find the stairs!
# We will do a flood-fill or simple systematic grid search using DFS/BFS in Python.

visited = set()
path_stack = []

def get_neighbors(pos):
    # Neighbors: Up, Down, Left, Right
    return [
        ((pos[0], pos[1]-1), "Up"),
        ((pos[0], pos[1]+1), "Down"),
        ((pos[0]-1, pos[1]), "Left"),
        ((pos[0]+1, pos[1]), "Right")
    ]

# Start exploration
start_pos = (22, 3)
visited.add(start_pos)

# Let's try to walk to all open tiles near us
# Since we have up to 100 buttons, let's write a simple path test.
# We want to check columns 14 to 25, rows 1 to 7.
# Let's test walking to some coordinates on the East side:

# Let's walk to (24, 3) and test Up
path_test = [
    "Right", "Right", # to (24, 3)
    "Up", "Up",       # to (24, 1)
    "Down", "Down",   # back to (24, 3)
    "Left", "Left",   # back to (22, 3)
    "Left", "Left",   # to (20, 3)
    "Up", "Up",       # to (20, 1)
    "Down", "Down",   # back to (20, 3)
    "Right", "Right"  # back to (22, 3)
]

print("Starting systematic exploration on 1F East...")
for idx, direction in enumerate(path_test):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Step {idx} ({direction}): {pos_before} -> {pos_after}")
    if pos_before == pos_after:
        print(f"Blocked trying to move {direction} from {pos_before}")
    # If coordinate change is large, we warped!
    if abs(pos_before['x'] - pos_after['x']) > 2 or abs(pos_before['y'] - pos_after['y']) > 2:
        print(f"WARPED! New map coordinates: {pos_after}")
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
