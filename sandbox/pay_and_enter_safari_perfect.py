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

# Initialize blocked edges
blocked_edges = set()
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

# We are currently at (1, 14) in Fuchsia City overworld.
# We will use the fully open and correct waypoints to navigate to the Gatehouse:
fuchsia_waypoints = [
    (35, 14), # Right along Row 14 to Column 35 (the east corridor)
    (35, 2),  # Up Column 35 to Row 2
    (22, 2),  # Left along Row 2 to Column 22
    (18, 4),  # Left/Down to Row 4 Column 18
    (18, 3)   # Up to enter Gatehouse
]

print("--- PHASE 1 CHUNK 2: WALKING TO SAFARI ZONE GATEHOUSE ---")
for wp in fuchsia_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("Stepping UP to enter Gatehouse...")
mgba.press_buttons(["Up"])
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Coordinates inside Gatehouse:", curr)

# ==========================================
# PHASE 2: PAY AND ENTER SAFARI ZONE
# ==========================================
print("--- PHASE 2: PAYING CLERK ---")
blocked_edges = set()
# Walk to (4, 3) (directly in front of the clerk counter)
# To avoid the counter wall on Column 4 Row 5, we walk via Column 3:
# Coords inside Gatehouse are (4, 6) on enter.
# We walk:
# - Left to (3, 6)
# - Up to (3, 3)
# - Right to (4, 3)
gatehouse_waypoints = [
    (3, 6),
    (3, 3),
    (4, 3)
]

for wp in gatehouse_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("Facing UP to speak to clerk...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Talking to clerk...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Completing payment dialogue...")
for _ in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.0)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Position inside Safari Zone Center:", final_pos)
mgba.take_screenshot()
