import mgba
import time
import json
import os
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
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(0.4)
    
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    mgba.press_buttons(["Right"])
    time.sleep(0.15)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    if check_battle_or_text():
        print("  Still in battle/textbox! Trying B...")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        if check_battle_or_text():
            print("  STILL in battle/textbox! Aborting script.")
            return False
    return True

walkable_adj = {}
spin_transitions = {}
blocked = set()
visited_nodes = set()
to_explore = []

DATA_FILE = "gym_map_data.json"
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        for u, v in data.get("walkable_adj", []):
            tu, tv = tuple(u), tuple(v)
            if tu not in walkable_adj: walkable_adj[tu] = []
            if tv not in walkable_adj: walkable_adj[tv] = []
            if tv not in walkable_adj[tu]: walkable_adj[tu].append(tv)
            if tu not in walkable_adj[tv]: walkable_adj[tv].append(tu)
        for u, d, v in data.get("spin_transitions", []):
            spin_transitions[(tuple(u), d)] = tuple(v)
        for u, d in data.get("blocked", []):
            blocked.add((tuple(u), d))
        for u in data.get("visited_nodes", []):
            visited_nodes.add(tuple(u))
        for u in data.get("to_explore", []):
            to_explore.append(tuple(u))
        print("Loaded saved map data from:", DATA_FILE)
    except Exception as e:
        print("Error loading map, starting fresh:", e)

start_pos = get_pos()
if start_pos not in visited_nodes:
    visited_nodes.add(start_pos)
    to_explore.append(start_pos)
    walkable_adj[start_pos] = []

def save_progress():
    adj_list = []
    seen_edges = set()
    for u, neighbors in walkable_adj.items():
        for v in neighbors:
            edge = tuple(sorted([u, v]))
            if edge not in seen_edges:
                seen_edges.add(edge)
                adj_list.append([list(u), list(v)])
    spin_list = [[list(u), d, list(v)] for (u, d), v in spin_transitions.items()]
    blocked_list = [[list(u), d] for u, d in blocked]
    visited_list = [list(u) for u in visited_nodes]
    explore_list = [list(u) for u in to_explore]
    
    data = {
        "walkable_adj": adj_list,
        "spin_transitions": spin_list,
        "blocked": blocked_list,
        "visited_nodes": visited_list,
        "to_explore": explore_list
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

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

def step_and_verify(direction, expected_pos):
    start_pos = get_pos()
    mgba.press_buttons([direction])
    
    start_wait = time.time()
    is_battle = False
    while (time.time() - start_wait) < 5.0:
        if check_battle_or_text():
            is_battle = True
            break
        pos = get_pos()
        if pos != start_pos:
            time.sleep(0.5)
            if check_battle_or_text():
                is_battle = True
                break
            final_pos = get_pos()
            if final_pos == expected_pos:
                return "walk"
            else:
                return f"spin_to_{final_pos}"
        time.sleep(0.1)
        
    if is_battle:
        if handle_battle_or_text():
            return "battle_fled_on_new_tile"
        else:
            return "abort"
            
    return "blocked"

def walk_path(path):
    for node in path:
        pos = get_pos()
        dx = node[0] - pos[0]
        dy = node[1] - pos[1]
        if dx == 1 and dy == 0: d = "Right"
        elif dx == -1 and dy == 0: d = "Left"
        elif dx == 0 and dy == 1: d = "Down"
        elif dx == 0 and dy == -1: d = "Up"
        else:
            print(f"Error: path step from {pos} to {node} is invalid!")
            return False
            
        res = step_and_verify(d, node)
        if res == "walk" or res == "battle_fled_on_new_tile":
            continue
        else:
            print(f"Failed path node {node}. Result was {res}.")
            return False
    return True

dirs = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

steps = 0
limit = 35

print("Starting BFS mapping...")
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
                if target not in to_explore:
                    to_explore.append(target)
                save_progress()
                break
        
        curr_pos = get_pos()
        print(f"\nExploring from {curr_pos}...")
        
        # Ensure we are not in a battle/textbox before starting exploration tests from this node!
        if check_battle_or_text():
            if not handle_battle_or_text():
                print("Aborting exploration due to uncleared battle/textbox.")
                if target not in to_explore:
                    to_explore.append(target)
                break
        
        for d, (dx, dy) in dirs.items():
            expected = (curr_pos[0] + dx, curr_pos[1] + dy)
            if (curr_pos, d) in blocked:
                continue
            if not (0 <= expected[0] <= 19 and 0 <= expected[1] <= 15):
                continue
            
            print(f"  Testing {d} to {expected}...")
            res = step_and_verify(d, expected)
            steps += 1
            
            if res == "abort":
                print("  Aborting.")
                if target not in to_explore:
                    to_explore.append(target)
                save_progress()
                break
                
            if res == "blocked":
                print("    BLOCKED.")
                blocked.add((curr_pos, d))
                save_progress()
            elif res == "walk" or res == "battle_fled_on_new_tile":
                print(f"    Normal step. Result: {res}")
                new_pos = get_pos()
                
                # Check if we need to verify step back
                step_back_ok = True
                if res == "walk":
                    opp_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
                    back_res = step_and_verify(opp_d, curr_pos)
                    if back_res != "walk" and back_res != "battle_fled_on_new_tile":
                        print(f"    WARNING: failed to step back. Result: {back_res}")
                        step_back_ok = False
                
                if step_back_ok:
                    # Successfully verified bidirectionality! Add to graph.
                    if curr_pos not in walkable_adj: walkable_adj[curr_pos] = []
                    if new_pos not in walkable_adj: walkable_adj[new_pos] = []
                    if new_pos not in walkable_adj[curr_pos]: walkable_adj[curr_pos].append(new_pos)
                    if curr_pos not in walkable_adj[new_pos]: walkable_adj[new_pos].append(curr_pos)
                    
                    if new_pos not in visited_nodes:
                        visited_nodes.add(new_pos)
                        to_explore.append(new_pos)
                    
                    save_progress()
                else:
                    # Did not verify step back! Do NOT add to graph, and break to let user evaluate.
                    break
            elif res.startswith("spin_to_"):
                new_pos = get_pos()
                print(f"    SPIN/WARP DETECTED! {curr_pos} + {d} -> {new_pos}")
                spin_transitions[(curr_pos, d)] = new_pos
                
                if new_pos not in visited_nodes:
                    visited_nodes.add(new_pos)
                    to_explore.append(new_pos)
                
                save_progress()
                
                path_back = find_path(new_pos, curr_pos)
                if path_back:
                    print("    Walking back...")
                    if not walk_path(path_back):
                        break
                else:
                    print(f"    No path back. Relocating to {new_pos}.")
                    break

except Exception as e:
    print("Exception:", e)

save_progress()
print("\n--- Final Results ---")
print("Walkable Adj:", walkable_adj)
print("Spin Transitions:", spin_transitions)
print("Blocked:", list(blocked))
print("Current Position:", get_pos())
print("To Explore:", to_explore)
