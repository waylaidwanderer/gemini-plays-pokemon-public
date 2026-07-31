import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

# We start at (19, 15)
print("Start Position:", mgba.get_coordinates())

# Let's explore the Right Room comprehensively.
# We will walk around all columns 18-28 and rows 10-15 and print every walkable tile!
walkable_tiles = set()
visited = set()

# To keep it safe and avoid getting lost, we will use a stack and trace our moves carefully.
# Since there are no spinners in the Right Room, we can do standard grid DFS!

def dfs(pos):
    walkable_tiles.add(pos)
    visited.add(pos)
    
    # Try all 4 directions
    directions = ['Up', 'Down', 'Left', 'Right']
    opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
    
    for move in directions:
        dx, dy = 0, 0
        if move == 'Up': dy = -1
        elif move == 'Down': dy = 1
        elif move == 'Left': dx = -1
        elif move == 'Right': dx = 1
        
        nxt = (pos[0] + dx, pos[1] + dy)
        
        # We don't want to walk out of the Right Room bounds (X between 18 and 28, Y between 10 and 15)
        # to avoid stepping on spinners
        if 18 <= nxt[0] <= 28 and 10 <= nxt[1] <= 15:
            if nxt not in visited:
                # Try the move
                mgba.press_buttons([move])
                p_new_coords = wait_for_movement()
                p_new = (p_new_coords['x'], p_new_coords['y'])
                
                if p_new == nxt:
                    # Move succeeded!
                    dfs(p_new)
                    # Walk back
                    mgba.press_buttons([opposite[move]])
                    wait_for_movement()
                else:
                    # Blocked (wall, grunt, etc.)
                    visited.add(nxt) # Mark as visited so we don't try it again

# Run DFS starting from current position
dfs((19, 15))

print("ALL REACHABLE WALKABLE TILES IN RIGHT ROOM:")
print(sorted(list(walkable_tiles)))

# Take a screenshot
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
