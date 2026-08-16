import mgba
import time
from PIL import Image

def get_textbox_ratio():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    
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

print("--- PAYING AND ENTERING SAFARI ZONE PERFECT ---")
blocked_edges = set()

# Stand at (3, 3) first and face Right to talk to the clerk
navigate_to_waypoint(3, 3, blocked_edges)
mgba.press_buttons(["Right"])
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Check if text box appeared
ratio = get_textbox_ratio()
print(f"TextBox ratio at (3, 3): {ratio:.3f}")

if ratio < 0.70:
    print("Could not talk to clerk at (3, 3). Trying (3, 2)...")
    navigate_to_waypoint(3, 2, blocked_edges)
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    ratio = get_textbox_ratio()
    print(f"TextBox ratio at (3, 2): {ratio:.3f}")

# Perform payment dialogue
print("Completing dialogue...")
for i in range(12):
    mgba.press_buttons(["A"])
    time.sleep(1.2)

# Walk to the turnstiles and enter
print("Navigating to turnstile at (1, 2)...")
blocked_edges = set()
navigate_to_waypoint(1, 2, blocked_edges)

print("Walking UP through the turnstile...")
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["Up"])
time.sleep(1.5)

final_pos = mgba.get_coordinates()
print("Position after entry attempt:", final_pos)
mgba.take_screenshot()

