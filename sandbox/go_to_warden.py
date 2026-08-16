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

def check_and_handle_battle():
    ratio = get_textbox_ratio()
    if ratio < 0.70:
        return False
        
    print(f"Dialogue/TextBox detected. Pressing B to clear...")
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    return True

def get_path_bfs(start, target, blocked_edges):
    queue = [[start]]
    visited = {start}
    
    # Map boundaries in Fuchsia City (0-39)
    max_x, max_y = 39, 35
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
            
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if 0 <= neighbor[0] <= max_x and 0 <= neighbor[1] <= max_y:
                # Column 25 fence posts (blocked on rows 23-26, and 28-29)
                if neighbor[0] == 25 and neighbor[1] in [23, 24, 25, 26, 28, 29]:
                    continue
                # Row 29 fence posts on columns 25-29
                if neighbor[1] == 29 and 25 <= neighbor[0] <= 29:
                    continue
                    
                if neighbor not in visited:
                    edge = (curr, neighbor)
                    if edge not in blocked_edges:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def navigate_to_target(target_x, target_y):
    blocked_edges = set()
    steps = 0
    
    print(f"Navigating to Warden's House at ({target_x}, {target_y})...")
    
    while True:
        if steps >= 30:
            print("Step limit reached!")
            return False
            
        check_and_handle_battle()
        
        curr = mgba.get_coordinates()
        if curr is None:
            time.sleep(0.5)
            continue
            
        cx, cy = curr['x'], curr['y']
        if cx == target_x and cy == target_y:
            print("Arrived at target!")
            return True
            
        path = get_path_bfs((cx, cy), (target_x, target_y), blocked_edges)
        if not path or len(path) < 2:
            print("No path found!")
            return False
            
        next_step = path[1]
        dx = next_step[0] - cx
        dy = next_step[1] - cy
        
        if dx == 1: btn = "Right"
        elif dx == -1: btn = "Left"
        elif dy == 1: btn = "Down"
        else: btn = "Up"
        
        print(f"Step {steps+1}: At ({cx}, {cy}). Stepping {btn} to {next_step}...")
        mgba.press_buttons([btn])
        time.sleep(0.45)
        steps += 1
        
        post = mgba.get_coordinates()
        if post is None:
            time.sleep(0.5)
            continue
            
        px, py = post['x'], post['y']
        if (px, py) == (cx, cy):
            if check_and_handle_battle():
                continue
            else:
                print(f"BUMPED! Blocking edge {((cx, cy), next_step)}")
                blocked_edges.add(((cx, cy), next_step))
                blocked_edges.add((next_step, (cx, cy)))

# Run the navigation from current position (25, 26) to Warden's door (27, 27)
navigate_to_target(27, 27)

# Press UP once more to ensure we cross the threshold and enter the house
print("Entering Warden's House...")
mgba.press_buttons(["Up"])
time.sleep(1.5)

print("Current coordinates inside:", mgba.get_coordinates())
mgba.take_screenshot()
