import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press(btn):
    mgba.press_buttons([btn])
    time.sleep(0.1)

# Backtracking map-exploration algorithm
# Starting from current position (19, 5)
start = get_pos()
walkable = set()
walkable.add(start)

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

# We can perform a local exploration by systematically walking
# and backtracking to map out all walkable tiles.
import sys

def explore(current, path_from_start):
    # Try all 4 directions
    for d, (dx, dy) in directions.items():
        nxt = (current[0] + dx, current[1] + dy)
        if nxt in walkable:
            continue
        
        # Try moving
        press(d)
        pos = get_pos()
        if pos == current:
            # Blocked
            continue
        
        # We moved!
        if pos not in walkable:
            print(f"Discovered walkable: {pos}")
            walkable.add(pos)
        
        # Recursively explore from the new position
        explore(pos, path_from_start + [d])
        
        # Backtrack
        press(opposites[d])
        get_pos()

print("Starting systematic overworld room mapping...")
explore(start, [])
print("All walkable tiles discovered:")
print(sorted(list(walkable)))
