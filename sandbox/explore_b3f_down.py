import mgba
import time

def opposite(d):
    return {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]

def delta(pos, d):
    x, y = pos['x'], pos['y']
    if d == "Up": return {'x': x, 'y': y - 1}
    if d == "Down": return {'x': x, 'y': y + 1}
    if d == "Left": return {'x': x - 1, 'y': y}
    if d == "Right": return {'x': x + 1, 'y': y}

visited = set()
path = []

def dfs(pos):
    visited.add((pos['x'], pos['y']))
    print(f"At {pos}, path length: {len(path)}")
    
    # Check if we arrived at B3F (21, 22) or B4F (since stepping on B3F 21, 22 warps us to B4F)
    if pos['x'] == 21 and pos['y'] == 22:
        print("FOUND STAIRS AT (21, 22)!")
        return True

    # Try 4 directions
    for d in ["Right", "Down", "Left", "Up"]:
        nbr = delta(pos, d)
        if (nbr['x'], nbr['y']) in visited:
            continue
            
        # Try walking
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        
        if new_pos != pos:
            # We moved!
            if new_pos == nbr:
                # Normal move
                path.append(d)
                found = dfs(new_pos)
                if found:
                    return True
                # Backtrack
                path.pop()
                mgba.press_buttons([opposite(d), "sleep 300"])
                time.sleep(0.5)
            else:
                # Unexpected move (could be spinner/warp)
                print(f"Unexpected move: {pos} -({d})-> {new_pos}")
                # Walk back if possible (might not work if we warped/slid, but let's try)
                mgba.press_buttons([opposite(d), "sleep 300"])
                time.sleep(0.5)
                # Check if we got back
                cur_pos = mgba.get_coordinates()
                if cur_pos != pos:
                    print(f"ERROR: Failed to backtrack from unexpected move! Current: {cur_pos}, expected: {pos}")
                    # If we warped, we might have to stop
                    return False
        else:
            # Blocked
            visited.add((nbr['x'], nbr['y']))
            
    return False

start_pos = mgba.get_coordinates()
print("Starting physical DFS from:", start_pos)
dfs(start_pos)
print("DFS finished.")
