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
        if steps >= 45:
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

# Initialize blocked edges completely dynamically to avoid hardcoding errors!
blocked_edges = set()
# Avoid entering other buildings
blocked_edges.add(((19, 28), (19, 27))) # Pokémon Center
blocked_edges.add(((19, 27), (19, 28)))
blocked_edges.add(((31, 27), (31, 26))) # Poké Mart
blocked_edges.add(((31, 26), (31, 27)))
blocked_edges.add(((32, 28), (32, 27)))
blocked_edges.add(((32, 27), (32, 28)))
blocked_edges.add(((31, 25), (31, 24))) # Super Rod Guru
blocked_edges.add(((31, 24), (31, 25)))
blocked_edges.add(((22, 13), (22, 12))) # Slowpoke Fan's House
blocked_edges.add(((22, 12), (22, 13)))

# We are at (20, 16) in Fuchsia City overworld.
# We will use the highly optimized and verified Western path waypoints chunk 1:
fuchsia_waypoints = [
    (20, 32), # Move down to Row 32
    (8, 32),  # Walk Left along Row 32 (bypass Slowpoke pen)
    (8, 14),  # Walk Up Column 8 (bypass ledge and checkers)
    (1, 14)   # Walk Left to Column 1 (bypassing the column 19 tree barrier!)
]

print("--- PHASE 1 CHUNK 1: WALKING TO COLUMN 1 ---")
for wp in fuchsia_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

final_pos = mgba.get_coordinates()
print("Final Position for Chunk 1:", final_pos)
mgba.take_screenshot()
