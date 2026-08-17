import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    # Press button
    mgba.press_buttons([btn])
    time.sleep(0.3) # Increased sleep to 300ms to allow frame emulation to complete fully
    return get_pos()

# Let's do a safe grid scan of adjacent tiles to find walkable ones.
# We are currently at (0, 4).
start = get_pos()
print(f"Starting reliable BFS from {start}")

# We will maintain:
# - walkable: set of all verified walkable coordinates
# - parents: mapping from node to parent node to reconstruct backpaths
walkable = {start}
queue = [start]
parent_map = {}

# Standard BFS to explore the room
# This script will run turn-by-turn inside python, which is safe.
# Since we have up to 100 presses per run_code, we can do quite a few steps.

# Let's explore neighbors of (0,4)
directions = {
    "Left": (-1, 0),
    "Right": (1, 0),
    "Up": (0, -1),
    "Down": (0, 1)
}

opposites = {
    "Left": "Right",
    "Right": "Left",
    "Up": "Down",
    "Down": "Up"
}

# We can systematically try to move, and if successful, backtrack immediately.
# This prevents getting lost.
x, y = start
for d, (dx, dy) in directions.items():
    nx, ny = x + dx, y + dy
    pos = press_and_wait(d)
    if pos != (x, y):
        print(f"Verified walkable neighbor in dir {d}: {pos}")
        walkable.add(pos)
        # Backtrack
        press_and_wait(opposites[d])
    else:
        print(f"Blocked in dir {d}")

print("Local probe complete. Current position:", get_pos())
