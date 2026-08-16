import mgba
import time
from PIL import Image

def get_textbox_ratio():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    
    white_pixels = 0
    total_pixels = 0
    
    for x in range(60, 420):
        for y in range(360, 405):
            r, g, b, *a = img.getpixel((x, y))
            if r > 220 and g > 220 and b > 220 and abs(r - g) < 15 and abs(g - b) < 15:
                white_pixels += 1
            total_pixels += 1
            
    return white_pixels / total_pixels

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    for _ in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    print("Escape sequence complete.")

def check_and_handle_battle():
    ratio = get_textbox_ratio()
    if ratio < 0.70:
        return False
        
    print(f"TextBox detected. Pressing B...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
        
    ratio = get_textbox_ratio()
    if ratio < 0.70:
        return False
        
    print("In battle! Escaping...")
    escape_battle()
    return True

def get_path_bfs(start, target, blocked_edges, current_map):
    queue = [[start]]
    visited = {start}
    max_x, max_y = 40, 40
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
            
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if 0 <= neighbor[0] <= max_x and 0 <= neighbor[1] <= max_y:
                # Basic collision filters
                if current_map == "center":
                    # Pond & Rest House 1 blocks rows 10-15, columns 9-19
                    if 9 <= neighbor[0] <= 19 and 10 <= neighbor[1] <= 15:
                        continue
                    # Row 25 barrier
                    if neighbor[1] == 25 and neighbor[0] != 15:
                        continue
                    # Ledge row 23
                    if neighbor[1] == 23 and curr[1] == 24:
                        continue
                elif current_map == "area3":
                    # Row 24 shrub cols 22-29
                    if neighbor[1] == 24 and 22 <= neighbor[0] <= 29:
                        continue
                        
                if neighbor not in visited:
                    edge = (curr, neighbor)
                    if edge not in blocked_edges:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def navigate_to_waypoint(target_x, target_y, blocked_edges, current_map):
    print(f"Navigating to ({target_x}, {target_y}) in {current_map}...")
    while True:
        check_and_handle_battle()
        curr = mgba.get_coordinates()
        if curr is None:
            check_and_handle_battle()
            time.sleep(0.5)
            continue
            
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            return True
            
        path = get_path_bfs((cx, cy), (target_x, target_y), blocked_edges, current_map)
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
        
        mgba.press_buttons([btn])
        time.sleep(0.42)
        
        post = mgba.get_coordinates()
        if post is None:
            check_and_handle_battle()
            time.sleep(0.5)
            continue
            
        px, py = post['x'], post['y']
        if (px, py) == (cx, cy):
            if check_and_handle_battle():
                continue
            else:
                print(f"BUMPED! Edge {((cx, cy), next_step)} is blocked.")
                blocked_edges.add(((cx, cy), next_step))
                blocked_edges.add((next_step, (cx, cy)))
        else:
            if abs(px - cx) > 5 or abs(py - cy) > 5:
                print("Map transition detected!")
                return True

blocked_edges = set()

# ==========================================
# PHASE 1: Area 3 (West) -> Center
# ==========================================
print("Current position:", mgba.get_coordinates())

# Waypoints to get to the Center warp at (29, 23) in Area 3
area3_waypoints = [
    (19, 23), # Walk up to Row 23
    (29, 23)  # Walk Right along Row 23
]

for wp in area3_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges, "area3")

# Transition to Center
print("Transitioning RIGHT to Center...")
for _ in range(4):
    mgba.press_buttons(["Right"])
    time.sleep(0.5)

time.sleep(1.5)
print("Entered Safari Zone Center:", mgba.get_coordinates())

# ==========================================
# PHASE 2: Center -> Gatehouse Exit
# ==========================================
center_waypoints = [
    (8, 11),  # Walk right/down to bypass pond
    (8, 22),  # Walk down column 8
    (15, 22), # Walk right along row 22
    (15, 25)  # Walk down column 15 to the Gatehouse exit
]

for wp in center_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges, "center")

print("At Gatehouse exit. Walking DOWN to exit to Fuchsia...")
for _ in range(4):
    mgba.press_buttons(["Down"])
    time.sleep(0.5)

time.sleep(1.5)
print("Final Position outside:", mgba.get_coordinates())
mgba.take_screenshot()
