import mgba
import time
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
# PHASE 2: Area 1 (East) -> Area 2 (North) (Resuming from (0, 21))
# ==========================================
curr = mgba.get_coordinates()
print("Starting coordinates in Area 1 (East):", curr)

area1_waypoints = [
    (20, 21), # Walk East along Row 21 to Column 20 (Open corridor)
    (20, 20), # Climb southern plateau stairs
    (12, 20), # Walk Left across plateau
    (12, 22), # Descend stairs to ground
    (8, 22),  # Walk Left
    (8, 8),   # Walk Up Column 8
    (12, 8),  # Walk Right
    (12, 6),  # Climb northern plateau stairs
    (17, 6),  # Walk Right across plateau
    (17, 8),  # Descend stairs to ground
    (20, 8),  # Walk Right
    (20, 3),  # Walk Up Column 20
    (7, 3),   # Walk Left along Row 3
    (7, 5),   # Walk Down
    (0, 5)    # Walk Left to transition
]

print("--- PHASE 2: Navigating Area 1 (East) ---")
for wp in area1_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("At transition (0, 5). Transitioning to Area 2 (North)...")
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
time.sleep(1.5)

# ==========================================
# PHASE 3: Area 2 (North) -> Area 3 (West)
# ==========================================
curr = mgba.get_coordinates()
print("Coordinates in Area 2 (North):", curr)

# Reset blocked edges for the new map
blocked_edges = set()

area2_waypoints = [
    (22, 31),
    (22, 22),
    (16, 22),
    (16, 28),
    (12, 28),
    (12, 30),
    (8, 30),
    (8, 35)
]

print("--- PHASE 3: Navigating Area 2 (North) ---")
for wp in area2_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("At transition (8, 35). Transitioning to Area 3 (West)...")
for _ in range(4):
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
time.sleep(1.5)

# ==========================================
# PHASE 4: Area 3 (West) -> (19, 26)
# ==========================================
curr = mgba.get_coordinates()
print("Coordinates in Area 3 (West):", curr)

# Reset blocked edges for the new map
blocked_edges = set()

area3_waypoints = [
    (25, 2),
    (25, 18),
    (21, 18),
    (21, 26),
    (19, 26)
]

print("--- PHASE 4: Navigating Area 3 (West) to Gold Teeth ---")
for wp in area3_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("--- PHASE 5: Retrieving Gold Teeth ---")
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

