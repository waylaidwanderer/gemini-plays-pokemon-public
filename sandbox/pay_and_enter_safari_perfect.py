import mgba
import time
from PIL import Image

def get_textbox_ratio():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    gray = img.convert("L")
    
    white_pixels = 0
    total_pixels = 0
    
    for x in range(60, 420):
        for y in range(360, 405):
            r, g, b, *a = img.getpixel((x, y))
            if r > 220 and g > 220 and b > 220 and abs(r - g) < 15 and abs(g - b) < 15:
                white_pixels += 1
            total_pixels += 1
            
    return white_pixels / total_pixels

def check_and_handle_battle():
    ratio = get_textbox_ratio()
    if ratio < 0.70:
        return False
        
    print(f"TextBox detected (ratio: {ratio:.3f}). Clearing...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    return True

def get_path_bfs(start, target, blocked_edges):
    queue = [[start]]
    visited = {start}
    
    max_x, max_y = 39, 35
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
            
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if 0 <= neighbor[0] <= max_x and 0 <= neighbor[1] <= max_y:
                # Fuchsia City overworld boundaries
                # Column 25 fence posts (rows 23-26, and 28-29)
                if neighbor[0] == 25 and neighbor[1] in [23, 24, 25, 26, 28, 29]:
                    continue
                # Row 29 fence posts (columns 25-29)
                if neighbor[1] == 29 and 25 <= neighbor[0] <= 29:
                    continue
                # Row 16 Tree Barrier (Columns 27-35)
                if neighbor[1] == 16 and 27 <= neighbor[0] <= 35:
                    continue
                    
                if neighbor not in visited:
                    edge = (curr, neighbor)
                    if edge not in blocked_edges:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def navigate_to_waypoint(target_x, target_y, blocked_edges):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    steps = 0
    
    while True:
        if steps >= 30:
            print("Waypoints step limit reached!")
            return False
            
        curr = mgba.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
                
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        path = get_path_bfs((cx, cy), (target_x, target_y), blocked_edges)
        if not path or len(path) < 2:
            print(f"No path found to ({target_x}, {target_y})!")
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
        time.sleep(0.45)
        steps += 1
        
        post = mgba.get_coordinates()
        if post is None:
            time.sleep(0.5)
            continue
                
        px, py = post['x'], post['y']
        if (px, py) == (cx, cy):
            print(f"BUMPED! Edge {((cx, cy), next_step)} is blocked.")
            blocked_edges.add(((cx, cy), next_step))
            blocked_edges.add((next_step, (cx, cy)))
        else:
            if abs(px - cx) > 5 or abs(py - cy) > 5:
                print("Map transition detected!")
                return True

# Initialize blocked edges
blocked_edges = set()
blocked_edges.add(((19, 28), (19, 27))) # Pokémon Center
blocked_edges.add(((19, 27), (19, 28)))
blocked_edges.add(((31, 27), (31, 26))) # Poké Mart
blocked_edges.add(((31, 26), (31, 27)))
blocked_edges.add(((32, 28), (32, 27)))
blocked_edges.add(((32, 27), (32, 28)))

# We are at (27, 20) in Fuchsia City overworld.
fuchsia_waypoints = [
    (27, 22), # Move down to Row 22
    (35, 22), # Right along Row 22 to Column 35
    (35, 2),  # Up Column 35 to Row 2
    (22, 2),  # Left along Row 2 to Column 22
    (22, 4),  # Down Column 22 to Row 4
    (18, 4),  # Left Row 4 to Column 18
    (18, 3)   # Up to enter Gatehouse
]

print("--- PHASE 1: WALKING TO SAFARI GATEHOUSE ---")
for wp in fuchsia_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("Stepping UP to enter Gatehouse...")
mgba.press_buttons(["Up"])
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Coordinates inside Gatehouse:", curr)

# Inside the gatehouse: pay and enter
print("--- PHASE 2: PAYING CLERK ---")
# Reset blocked edges for the gatehouse indoor map
blocked_edges = set()
# Walk to the clerk at (3, 2)
navigate_to_waypoint(3, 2, blocked_edges)

print("Facing RIGHT to speak to clerk...")
mgba.press_buttons(["Right"])
time.sleep(0.5)

print("Talking to clerk...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Completing dialogue...")
for _ in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.0)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Position inside Safari Zone Center:", final_pos)
mgba.take_screenshot()
