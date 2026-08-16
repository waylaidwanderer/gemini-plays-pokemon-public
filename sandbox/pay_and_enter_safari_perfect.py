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
        time.sleep(0.42)
        
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
            if (px, py) != next_step:
                if abs(px - cx) > 5 or abs(py - cy) > 5:
                    print("Map transition detected!")
                    return True

print("--- PAYING AND ENTERING SAFARI PERFECT ---")
blocked_edges = set()

# Block doors we want to avoid entering in Fuchsia City overworld
blocked_edges.add(((19, 28), (19, 27))) # Pokémon Center
blocked_edges.add(((19, 27), (19, 28)))
blocked_edges.add(((32, 28), (32, 27))) # Slowpoke Fan's House
blocked_edges.add(((32, 27), (32, 28)))
blocked_edges.add(((27, 28), (27, 27))) # Warden's House
blocked_edges.add(((27, 27), (27, 28)))
blocked_edges.add(((31, 27), (31, 26))) # Block entering Poké Mart again
blocked_edges.add(((31, 26), (31, 27)))

# Block Warden's solid wall at (26, 27) and (28, 27) to avoid bumps
blocked_edges.add(((26, 28), (26, 27)))
blocked_edges.add(((26, 27), (26, 28)))
blocked_edges.add(((28, 28), (28, 27)))
blocked_edges.add(((28, 27), (28, 28)))

fuchsia_waypoints = [
    (26, 28), # Walk Left to Column 26 Row 28
    (26, 30), # Walk DOWN Column 26 to Row 30 (Warden house wall bypass)
    (24, 30), # Walk LEFT Row 30 through Column 25 fence gap to Column 24
    (24, 14), # UP Column 24 to Row 14
    (37, 14), # RIGHT along Row 14 to Column 37 (passes above Zoo fence)
    (37, 2),  # Up Column 37 to Row 2
    (22, 2),  # Left along Row 2 to Column 22
    (22, 4),  # Down Column 22 to Row 4
    (18, 4),  # Left Row 4 to Column 18
    (18, 3)   # Up to enter Gatehouse
]

for wp in fuchsia_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("Stepping UP to enter the Gatehouse...")
mgba.press_buttons(["Up"])
time.sleep(1.5)

curr = mgba.get_coordinates()
print("Coordinates inside Gatehouse:", curr)

print("Standing in front of clerk at (3, 2)...")
blocked_edges = set()
navigate_to_waypoint(3, 2, blocked_edges)

print("Facing RIGHT to speak to clerk...")
mgba.press_buttons(["Right"])
time.sleep(0.5)

print("Talking to clerk...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Perform payment dialogue
print("Completing dialogue...")
for i in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.2)

# Emerge in Safari Zone Center at (15, 25)
curr = mgba.get_coordinates()
print("Coordinates after warp (Safari Zone Center):", curr)

# Navigate through Safari Zone Center to Area 1 (East) transition at (30, 10)
blocked_edges = set()
center_waypoints = [
    (15, 22), # Up 3 steps
    (28, 22), # Right to Column 28
    (28, 10), # Up to Row 10
    (30, 10)  # Transition to Area 1 (East)
]

for wp in center_waypoints:
    navigate_to_waypoint(wp[0], wp[1], blocked_edges)

print("Transitioning to Area 1 (East)...")
for _ in range(4):
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
time.sleep(1.5)

final_pos = mgba.get_coordinates()
print("Final coordinates inside Area 1 (East):", final_pos)
mgba.take_screenshot()

