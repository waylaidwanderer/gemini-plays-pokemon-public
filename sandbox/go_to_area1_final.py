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
# PHASE 1: Safari Zone Center -> Area 1 (East) (30, 10)
# ==========================================
print("--- PHASE 1: NAVIGATING SAFARI ZONE CENTER ---")
curr = mgba.get_coordinates()
print("Starting coordinates:", curr)

center_waypoints = [
    (15, 22), # Up 3 steps
    (28, 22), # Right to Column 28
    (28, 10), # Up to Row 10
    (30, 10)  # Transition to Area 1 (East)
]

for wp in center_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

# Emerge transition to Area 1 (East)
print("Transitioning to Area 1 (East)...")
for _ in range(4):
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
time.sleep(1.5)

# ==========================================
# PHASE 2: Area 1 (East) -> Northern Plateau Entrance at (12, 6)
# ==========================================
curr = mgba.get_coordinates()
print("Coordinates in Area 1 (East):", curr)

# Reset blocked edges for the new map
blocked_edges = set()

area1_waypoints = [
    (0, 24),  # Down Column 0 Row 24
    (4, 24),  # Right Column 4 Row 24
    (4, 22),  # Up Column 4 Row 22 (open grass corridor)
    (20, 22), # Right Row 22 to Column 20
    (20, 20), # Climb southern plateau stairs
    (12, 20), # Left along plateau
    (12, 22), # Descend southern plateau stairs
    (8, 22),  # Left Column 8 Row 22
    (8, 8),   # Up Column 8 Row 8
    (12, 8),  # Right to Column 12 Row 8
    (12, 6)   # Climb northern plateau stairs
]

print("--- PHASE 2: Navigating Area 1 (East) to (12, 6) ---")
for wp in area1_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

final_pos = mgba.get_coordinates()
print("Final coordinates inside Area 1 (East):", final_pos)
mgba.take_screenshot()

