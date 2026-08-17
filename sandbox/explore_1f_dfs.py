import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.3)
    return get_pos()

# Let's perform a safe, backtracking DFS to map Saffron West Gatehouse 1F
# starting from our current position (18, 5)

start = get_pos()
print(f"Starting complete 1F DFS mapping from {start}...")

visited_states = set()
visited_states.add(start)

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

def run_dfs(curr):
    # Try all 4 directions
    for d, (dx, dy) in directions.items():
        nxt = (curr[0] + dx, curr[1] + dy)
        if nxt in visited_states:
            continue
        
        # Try moving
        pos = press_and_wait(d)
        if pos != curr:
            # We moved!
            # Check for drastic coordinate change indicative of warp
            if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
                print(f"WARPED! New position: {pos}")
                # We warped out of the map! Backtrack by walking back?
                # Actually, if we warp out of the map, we should stop DFS since we found an exit!
                return True
            
            visited_states.add(pos)
            print(f"Discovered walkable 1F tile: {pos}")
            
            # Recursive step
            warped = run_dfs(pos)
            if warped:
                return True
            
            # Backtrack
            press_and_wait(opposites[d])
        else:
            # Blocked
            pass
    return False

run_dfs(start)
print("DFS complete. Walkable tiles found on 1F:")
print(sorted(list(visited_states)))
