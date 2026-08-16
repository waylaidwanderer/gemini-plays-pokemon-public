import mgba
import time
import os
from PIL import Image

def get_textbox_ratio():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    gray = img.convert("L")
    
    white_pixels = 0
    total_pixels = 0
    
    # Bottom region coordinates scaled for 3x (480 x 432 image size)
    for x in range(60, 420):
        for y in range(360, 405):
            r, g, b, *a = img.getpixel((x, y))
            if r > 220 and g > 220 and b > 220 and abs(r - g) < 15 and abs(g - b) < 15:
                white_pixels += 1
            total_pixels += 1
            
    return white_pixels / total_pixels

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    
    # Highlight RUN slowly
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def check_and_handle_battle():
    ratio = get_textbox_ratio()
    if ratio < 0.70:
        return False # No text box active
        
    print(f"TextBox detected (ratio: {ratio:.3f}). Pressing B to clear potential dialogue...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
        
    ratio = get_textbox_ratio()
    if ratio < 0.70:
        print("Dialogue cleared successfully.")
        return False
        
    print("Dialogue did not clear. We are in a battle! Escaping...")
    escape_battle()
    return True

def get_path_bfs(start, target, blocked_edges):
    queue = [[start]]
    visited = {start}
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
            
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if 0 <= neighbor[0] <= 40 and 0 <= neighbor[1] <= 40:
                if neighbor not in visited:
                    edge = (curr, neighbor)
                    if edge not in blocked_edges:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def navigate_to_waypoint(target_x, target_y, blocked_edges):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    
    while True:
        # Check for battle first
        check_and_handle_battle()
        
        curr = mgba.get_coordinates()
        if curr is None:
            print("Coordinates are None on loop start. Checking battle...")
            check_and_handle_battle()
            time.sleep(0.5)
            continue
                
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        # Get path using BFS
        path = get_path_bfs((cx, cy), (target_x, target_y), blocked_edges)
        if not path or len(path) < 2:
            print(f"No path found to ({target_x}, {target_y}) with current knowledge!")
            return False
            
        next_step = path[1]
        dx = next_step[0] - cx
        dy = next_step[1] - cy
        
        if dx == 1: btn = "Right"
        elif dx == -1: btn = "Left"
        elif dy == 1: btn = "Down"
        else: btn = "Up"
        
        print(f"At ({cx}, {cy}). Stepping {btn} to {next_step}...")
        mgba.press_buttons([btn])
        time.sleep(0.42)
        
        # Verify movement
        post = mgba.get_coordinates()
        if post is None:
            print("Post-step coordinates are None. Checking battle...")
            check_and_handle_battle()
            time.sleep(0.5)
            continue
                
        px, py = post['x'], post['y']
        if (px, py) == (cx, cy):
            # We didn't move. Is it because of a battle/dialogue, or a real bump?
            if check_and_handle_battle():
                # It was a battle! We escaped, so try again without marking as blocked.
                continue
            else:
                # It was a real bump (wall). Add to blocked edges
                print(f"BUMPED! Edge {((cx, cy), next_step)} is blocked.")
                blocked_edges.add(((cx, cy), next_step))
                blocked_edges.add((next_step, (cx, cy)))
        else:
            # Successfully moved
            if (px, py) != next_step:
                print(f"Unexpected movement: expected {next_step}, got ({px}, {py})")
                if abs(px - cx) > 5 or abs(py - cy) > 5:
                    print("Map transition detected during navigation!")
                    return True

# Initialize blocked edges
blocked_edges = set()

# ==========================================
# PHASE 1: Center -> (0, 11) Transition
# ==========================================
print("--- PHASE 1: Navigating Center to Area 3 Transition ---")
center_waypoints = [
    (0, 11)
]

for wp in center_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("At transition (0, 11). Transitioning to Area 3 (West)...")
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
time.sleep(1.5)

# ==========================================
# PHASE 2: Area 3 (West) -> Gold Teeth (Plateau Route)
# ==========================================
curr = mgba.get_coordinates()
print("Starting coordinates in Area 3 (West):", curr)

# Reset blocked edges for Area 3
blocked_edges = set()

area3_waypoints = [
    (21, 18), # Walk to East Stairs of Plateau on Row 18
    (21, 16), # Climb East Stairs onto Plateau
    (6, 16),  # Walk Left across plateau
    (6, 20),  # Descend West Stairs to ground level
    (6, 26),  # Walk Down Column 6 to Row 26 Highway
    (19, 26)  # Walk East along Row 26 directly below Gold Teeth
]

print("--- PHASE 2: Navigating Area 3 (West) via Plateau Route ---")
for wp in area3_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("--- PHASE 3: Retrieving Gold Teeth ---")
# Face UP to look at the Gold Teeth at (19, 25)
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

screenshot_path = mgba.take_screenshot()
print(f"Verify screenshot before pickup: {screenshot_path}")

# Press A to pick up the teeth
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogues
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

final_pos = mgba.get_coordinates()
print("Final coordinates after pickup:", final_pos)

final_screenshot = mgba.take_screenshot()
print(f"Final screenshot: {final_screenshot}")

# ==========================================
# SECONDARY OBJECTIVE: Workspace Cleanup
# ==========================================
print("--- CLEANING UP OBSOLETE SCRIPTS ---")
obsolete_files = [
    "get_teeth_fast.py", "explore_plateau_stairs.py", "explore_water_boundary.py",
    "find_path_from_north.py", "find_southern_passage.py", "find_southern_passage_v2.py",
    "get_teeth_final.py", "get_teeth_from_gatehouse.py", "get_teeth_from_north.py",
    "go_to_area1_final.py", "go_to_area1_final_v2.py", "go_to_area1_final_v3.py",
    "go_to_area2_north.py", "go_to_area2_north_p2.py", "go_to_area3_final.py",
    "go_to_area3_final_v2.py", "go_to_gatehouse.py", "go_to_gatehouse_final.py",
    "go_to_gatehouse_from_pc.py", "go_to_gatehouse_from_position.py", "go_to_pc.py",
    "go_to_pc_interior.py", "go_to_western_ground.py", "go_to_western_ground_v2.py",
    "go_to_western_ground_v3.py", "go_to_western_ground_v4.py", "pay_and_enter_safari.py",
    "pay_and_enter_safari_chunk1.py", "re_enter_safari_from_36_2.py", "re_enter_safari_from_mart.py",
    "search_teeth.py", "teach_cut_forget.py", "teach_cut_now.py", "teach_cut_robust.py",
    "test_cut.py", "test_row6_walk.py", "retrieve_teeth_dynamic.py", "retrieve_teeth_final.py",
    "retrieve_teeth_final_p2.py", "retrieve_teeth_final_p3.py"
]

for filename in obsolete_files:
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"Deleted: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")

# Cleanup the nested notepads directory
nested_dir = "notepads/notepads/"
if os.path.exists(nested_dir):
    try:
        import shutil
        shutil.rmtree(nested_dir)
        print(f"Deleted nested directory: {nested_dir}")
    except Exception as e:
        print(f"Error deleting {nested_dir}: {e}")

print("Cleanup complete.")

