import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_battle_or_text():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    p1 = img.getpixel((240, 380))
    p2 = img.getpixel((100, 380))
    p3 = img.getpixel((380, 380))
    cream = (247, 231, 214)
    return (p1 == cream and p2 == cream and p3 == cream)

def handle_battle_or_text():
    print("  Battle or Textbox detected! Attempting to clear/flee...")
    # Clear any initial text
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(0.4)
    
    # Try running away (Down, Right, A)
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
    mgba.press_buttons(["Right"])
    time.sleep(0.1)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Press B to dismiss any post-run text
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    # Check if we are still in battle
    if check_battle_or_text():
        print("  Still in battle/textbox! Might be trainer fight or multi-dialog. Trying B...")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        if check_battle_or_text():
            print("  STILL in battle/textbox! Aborting script for safety.")
            return False
    return True

# Load existing map data if any
walkable_adj = {}
spin_transitions = {}
blocked = set()

# Initialize from current pos
start_pos = get_pos()
walkable_adj[start_pos] = []

to_explore = [start_pos]
visited_nodes = {start_pos}

def find_path(start, target):
    if start == target:
        return []
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        node = path[-1]
        for neighbor in walkable_adj.get(node, []):
            if neighbor not in visited:
                if neighbor == target:
                    return path[1:] + [neighbor]
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def walk_path(path):
    for node in path:
        pos = get_pos()
        dx = node[0] - pos[0]
        dy = node[1] - pos[1]
        if dx == 1 and dy == 0:
            d = "Right"
        elif dx == -1 and dy == 0:
            d = "Left"
        elif dx == 0 and dy == 1:
            d = "Down"
        elif dx == 0 and dy == -1:
            d = "Up"
        else:
            print(f"Error: path step from {pos} to {node} is invalid!")
            return False
        
        mgba.press_buttons([d])
        time.sleep(0.55)
        
        if check_battle_or_text():
            if not handle_battle_or_text():
                return False
        
        new_pos = get_pos()
        if new_pos != node:
            print(f"Error: failed to follow path. Expected {node}, got {new_pos}")
            return False
    return True

dirs = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

steps = 0
limit = 50

print("Starting robust mapping from:", start_pos)

try:
    while to_explore and steps < limit:
        curr_pos = get_pos()
        to_explore.sort(key=lambda p: abs(p[0] - curr_pos[0]) + abs(p[1] - curr_pos[1]))
        target = to_explore.pop(0)
        
        if get_pos() != target:
            path = find_path(get_pos(), target)
            if path is None:
                print(f"No safe path from {get_pos()} to {target}, skipping.")
                continue
            if not walk_path(path):
                print(f"Failed navigating to {target}, aborting.")
                break
        
        curr_pos = get_pos()
        print(f"\nExploring from {curr_pos}...")
        
        for d, (dx, dy) in dirs.items():
            expected = (curr_pos[0] + dx, curr_pos[1] + dy)
            
            if (curr_pos, d) in blocked:
                continue
            if not (0 <= expected[0] <= 19 and 0 <= expected[1] <= 15):
                continue
            
            print(f"  Testing {d} to {expected}...")
            mgba.press_buttons([d])
            time.sleep(0.55)
            steps += 1
            
            if check_battle_or_text():
                if not handle_battle_or_text():
                    break
            
            new_pos = get_pos()
            
            if new_pos == curr_pos:
                print(f"    BLOCKED.")
                blocked.add((curr_pos, d))
            elif new_pos == expected:
                print(f"    Normal walkable step to {new_pos}.")
                if curr_pos not in walkable_adj:
                    walkable_adj[curr_pos] = []
                if new_pos not in walkable_adj:
                    walkable_adj[new_pos] = []
                if new_pos not in walkable_adj[curr_pos]:
                    walkable_adj[curr_pos].append(new_pos)
                if curr_pos not in walkable_adj[new_pos]:
                    walkable_adj[new_pos].append(curr_pos)
                
                if new_pos not in visited_nodes:
                    visited_nodes.add(new_pos)
                    to_explore.append(new_pos)
                
                # Step back
                opp_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
                mgba.press_buttons([opp_d])
                time.sleep(0.55)
                
                if check_battle_or_text():
                    if not handle_battle_or_text():
                        break
                
                if get_pos() != curr_pos:
                    print(f"    WARNING: failed to step back from {new_pos} to {curr_pos}!")
                    break
            else:
                # We spun or warped
                print(f"    SPIN/WARP DETECTED! {curr_pos} + {d} -> {new_pos}")
                spin_transitions[(curr_pos, d)] = new_pos
                
                if new_pos not in visited_nodes:
                    visited_nodes.add(new_pos)
                    to_explore.append(new_pos)
                
                path_back = find_path(new_pos, curr_pos)
                if path_back:
                    print(f"    Walking back via known path...")
                    if not walk_path(path_back):
                        break
                else:
                    print(f"    No known path back from {new_pos} to {curr_pos}. Relocating search to {new_pos}.")
                    break

except Exception as e:
    print("Exception occurred:", e)

print("\n--- Final Results ---")
print("Walkable Adj:", walkable_adj)
print("Spin Transitions:", spin_transitions)
print("Blocked:", list(blocked))
print("Current Position:", get_pos())

with open("gym_map_data.txt", "w") as f:
    f.write(f"walkable_adj = {walkable_adj}\n")
    f.write(f"spin_transitions = {spin_transitions}\n")
    f.write(f"blocked = {list(blocked)}\n")
