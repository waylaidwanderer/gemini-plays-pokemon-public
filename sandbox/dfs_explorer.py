import mgba
import time
import sys

# List of doors/warps to avoid stepping onto directly
WARPS = {
    (19, 17),  # Pokémon Center
    (13, 25),  # Bike Shop
    (25, 25),  # Poké Mart
    (13, 15),  # Melanie's House
    (9, 11),   # Badge Guy's House
    (30, 19),  # Cerulean Gym
    (27, 11),  # Burgled House
}

OPPOSITE = {
    "Up": "Down",
    "Down": "Up",
    "Left": "Right",
    "Right": "Left"
}

DIRECTIONS = ["Up", "Down", "Left", "Right"]

# To store grid information: True for walkable, False for blocked
grid = {}
visited = set()

def get_pos():
    # Loop to make sure we get a valid coordinate
    for _ in range(5):
        pos = mgba.get_coordinates()
        if pos != {'x': 0, 'y': 0}:
            return pos['x'], pos['y']
        time.sleep(0.1)
    return 0, 0

start_x, start_y = get_pos()
print(f"Starting DFS from: ({start_x}, {start_y})")

grid[(start_x, start_y)] = True
visited.add((start_x, start_y))

step_count = 0

def step(direction):
    global step_count
    step_count += 1
    mgba.press_buttons([direction])
    # Give a tiny sleep to let the emulator process movement
    time.sleep(0.05)
    return get_pos()

def dfs(cx, cy):
    print(f"At ({cx}, {cy})")
    
    # Check neighbors
    for d in DIRECTIONS:
        nx, ny = cx, cy
        if d == "Up": ny -= 1
        elif d == "Down": ny += 1
        elif d == "Left": nx -= 1
        elif d == "Right": nx += 1
        
        # Don't step onto known warps
        if (nx, ny) in WARPS:
            grid[(nx, ny)] = False
            continue
            
        # Don't cross map boundaries
        if nx < 0 or nx >= 40 or ny < 0 or ny >= 36:
            grid[(nx, ny)] = False
            continue
            
        if (nx, ny) not in visited:
            # Try to step
            rx, ry = step(d)
            if (rx, ry) == (nx, ny):
                # We successfully moved!
                grid[(nx, ny)] = True
                visited.add((nx, ny))
                dfs(nx, ny)
                # Backtrack
                bx, by = step(OPPOSITE[d])
                if (bx, by) != (cx, cy):
                    print(f"FATAL: Backtrack failed! Expected ({cx}, {cy}), got ({bx}, {by})")
                    sys.exit(1)
            else:
                # We hit a wall or ledge, or some obstacle
                grid[(nx, ny)] = False
                visited.add((nx, ny))
                # If we moved somewhere else entirely (unlikely unless warp/ledge), handle it
                if (rx, ry) != (cx, cy):
                    print(f"Unexpected movement! Tried {d} from ({cx}, {cy}), ended at ({rx}, {ry})")
                    # Try to return
                    # (This is just in case of ledges, but we shouldn't jump ledges during DFS)

# Run DFS with a safeguard limit
try:
    dfs(start_x, start_y)
except Exception as e:
    print(f"Exception: {e}")

# Print the map of reachable coords
print("\nReachable Map:")
min_x = min(x for x, y in grid.keys()) if grid else 0
max_x = max(x for x, y in grid.keys()) if grid else 39
min_y = min(y for x, y in grid.keys()) if grid else 0
max_y = max(y for x, y in grid.keys()) if grid else 35

for y in range(min_y, max_y + 1):
    row_str = f"Y={y:02d}: "
    for x in range(min_x, max_x + 1):
        if (x, y) == (start_x, start_y):
            row_str += "S"
        elif grid.get((x, y)) == True:
            row_str += "."
        elif grid.get((x, y)) == False:
            row_str += "#"
        else:
            row_str += " "
    print(row_str)

print(f"Total steps: {step_count}")
