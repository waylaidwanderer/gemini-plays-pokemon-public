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

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    
    # Run away is at bottom-right of the fight menu: Down, Right, A
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

def get_path_bfs(start, target, blocked_edges, current_map):
    queue = [[start]]
    visited = {start}
    
    # Map dimensions / boundaries
    max_x, max_y = 40, 40
    
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
            
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (curr[0] + dx, curr[1] + dy)
            if 0 <= neighbor[0] <= max_x and 0 <= neighbor[1] <= max_y:
                # Map specific hard-coded wall filters
                if current_map == "area1":
                    # Area 1 specific blockages
                    # Rhydon statues at column 6 row 22-23
                    if neighbor in [(6, 22), (6, 23)] and curr[1] in [22, 23]:
                        continue
                    # Row 6 tree barrier on west side
                    if neighbor[1] == 6 and neighbor[0] <= 10:
                        continue
                    # Row 12 NPC block
                    if neighbor == (15, 12):
                        continue
                    # Middle pond
                    if 11 <= neighbor[0] <= 17 and 10 <= neighbor[1] <= 14:
                        continue
                        
                elif current_map == "area2":
                    # Area 2 specific blockages
                    # Row 10 trees
                    if neighbor[1] == 10 and 27 <= neighbor[0] <= 31:
                        continue
                    # Column 16 bush rows 12-19
                    if neighbor[0] == 16 and 12 <= neighbor[1] <= 19:
                        continue
                    # Row 11 Rhydon statues / trees
                    if neighbor[1] == 11 and 21 <= neighbor[0] <= 31:
                        continue
                    if neighbor[1] == 11 and 16 <= neighbor[0] <= 17:
                        continue
                    # Pond at rows 17-18 cols 9-11
                    if 9 <= neighbor[0] <= 11 and 17 <= neighbor[1] <= 18:
                        continue
                        
                elif current_map == "area3":
                    # Area 3 specific blockages
                    # Vertical hedge col 24 rows 0-13
                    if neighbor[0] == 24 and neighbor[1] <= 13:
                        continue
                    # Column 18 shrub rows 20-23
                    if neighbor[0] == 18 and 20 <= neighbor[1] <= 23:
                        continue
                    # Row 24 shrub cols 22-29
                    if neighbor[1] == 24 and 22 <= neighbor[0] <= 29:
                        continue
                    # Col 0-1 tree rows 24-25
                    if neighbor[0] <= 1 and 24 <= neighbor[1] <= 25:
                        continue

                if neighbor not in visited:
                    edge = (curr, neighbor)
                    if edge not in blocked_edges:
                        visited.add(neighbor)
                        queue.append(path + [neighbor])
    return None

def navigate_chunk(target_waypoints, current_map, max_steps=20):
    blocked_edges = set()
    steps_taken = 0
    
    print(f"Starting chunk navigation in {current_map}. Max steps: {max_steps}")
    
    for wp in target_waypoints:
        print(f"Targeting waypoint {wp}...")
        while True:
            if steps_taken >= max_steps:
                print(f"Reached max steps limit ({max_steps}). Exiting chunk.")
                return steps_taken, False
                
            check_and_handle_battle()
            
            curr = mgba.get_coordinates()
            if curr is None:
                print("Coordinates are None. Checking battle...")
                check_and_handle_battle()
                time.sleep(0.5)
                continue
                
            cx, cy = curr['x'], curr['y']
            if cx == wp[0] and cy == wp[1]:
                print(f"Reached waypoint {wp}!")
                break # Move to next waypoint
                
            # Find path to waypoint
            path = get_path_bfs((cx, cy), wp, blocked_edges, current_map)
            if not path or len(path) < 2:
                print(f"No path found to {wp} with current knowledge. Trying next waypoint if any.")
                break
                
            next_step = path[1]
            dx = next_step[0] - cx
            dy = next_step[1] - cy
            
            if dx == 1: btn = "Right"
            elif dx == -1: btn = "Left"
            elif dy == 1: btn = "Down"
            else: btn = "Up"
            
            print(f"Step {steps_taken+1}/{max_steps}: At ({cx}, {cy}). Stepping {btn} to {next_step}...")
            mgba.press_buttons([btn])
            time.sleep(0.42)
            steps_taken += 1
            
            # Verify movement
            post = mgba.get_coordinates()
            if post is None:
                print("Post-step coordinates are None. Checking battle...")
                check_and_handle_battle()
                time.sleep(0.5)
                continue
                
            px, py = post['x'], post['y']
            if (px, py) == (cx, cy):
                # We didn't move. Check battle first
                if check_and_handle_battle():
                    continue
                else:
                    print(f"BUMPED! Edge {((cx, cy), next_step)} is blocked.")
                    blocked_edges.add(((cx, cy), next_step))
                    blocked_edges.add((next_step, (cx, cy)))
            else:
                # Successfully moved
                # If we detect a massive coordinate jump, it means map transition!
                if abs(px - cx) > 5 or abs(py - cy) > 5:
                    print(f"Map transition detected! Moved from ({cx}, {cy}) to ({px}, {py})")
                    return steps_taken, True
                    
    print("All waypoints in this chunk completed!")
    return steps_taken, False
