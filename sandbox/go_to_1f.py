import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))[:3]
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss run text
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

# Ensure any menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

start = mgba.get_coordinates()
start_tuple = (start["x"], start["y"])
print("Starting BFS search for stairs from:", start_tuple)

# Target stairs are at (5, 10)
target_stairs = (5, 10)

queue = [start_tuple]
visited = { start_tuple }
parent = {} # child_tuple -> (direction, parent_tuple)

dirs = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}
rev_dirs = {
    "Up": "Down",
    "Down": "Up",
    "Left": "Right",
    "Right": "Left"
}

button_press_count = 0
max_buttons = 80 # Safe limit to avoid the 100-button abort

def get_path_to(target_tuple):
    path = []
    curr = target_tuple
    while curr in parent:
        d, p = parent[curr]
        path.append(d)
        curr = p
    path.reverse()
    return path

def navigate_to(target_tuple, current_tuple):
    global button_press_count
    # Walk back to start
    path_start_to_curr = get_path_to(current_tuple)
    for d in reversed(path_start_to_curr):
        if button_press_count >= max_buttons:
            return False
        rev_d = rev_dirs[d]
        mgba.press_buttons([rev_d])
        button_press_count += 1
        time.sleep(0.4)
        handle_any_menu_or_battle()
        
    # Walk from start to target
    path_start_to_target = get_path_to(target_tuple)
    for d in path_start_to_target:
        if button_press_count >= max_buttons:
            return False
        mgba.press_buttons([d])
        button_press_count += 1
        time.sleep(0.4)
        handle_any_menu_or_battle()
    return True

current_pos = start_tuple
target_found = None

try:
    while queue and button_press_count < max_buttons:
        curr_tuple = queue.pop(0)
        
        if curr_tuple == target_stairs:
            print("FOUND PATH TO STAIRS!")
            target_found = curr_tuple
            break
            
        if curr_tuple != current_pos:
            if not navigate_to(curr_tuple, current_pos):
                break
            current_pos = curr_tuple
            
        # Verify arrival
        actual = mgba.get_coordinates()
        actual_tuple = (actual["x"], actual["y"])
        if actual_tuple != curr_tuple:
            print(f"Desync! Expected {curr_tuple}, got {actual_tuple}")
            break
            
        # Try all 4 directions from current node
        for d, (dx, dy) in dirs.items():
            neighbor_tuple = (curr_tuple[0] + dx, curr_tuple[1] + dy)
            if neighbor_tuple in visited:
                continue
                
            if button_press_count >= max_buttons:
                break
                
            print(f"Testing step {d} to {neighbor_tuple}...")
            mgba.press_buttons([d])
            button_press_count += 1
            time.sleep(0.4)
            handle_any_menu_or_battle()
            
            pos_after = mgba.get_coordinates()
            pos_after_tuple = (pos_after["x"], pos_after["y"])
            
            if pos_after_tuple == neighbor_tuple:
                visited.add(neighbor_tuple)
                parent[neighbor_tuple] = (d, curr_tuple)
                queue.append(neighbor_tuple)
                
                # Step back
                if button_press_count >= max_buttons:
                    break
                rev_d = rev_dirs[d]
                mgba.press_buttons([rev_d])
                button_press_count += 1
                time.sleep(0.4)
                handle_any_menu_or_battle()
            else:
                # Solid
                pass
finally:
    actual = mgba.get_coordinates()
    actual_tuple = (actual["x"], actual["y"])
    print(f"BFS iteration ended. Button presses: {button_press_count}/{max_buttons}")
    print(f"Visited {len(visited)} tiles: {sorted(list(visited))}")
    
    if target_found:
        print("At target stairs! Current position:", actual_tuple)
        path = get_path_to(target_found)
        print("Path from start to stairs:", path)
        if actual_tuple != target_found:
            print("Navigating to target stairs...")
            navigate_to(target_found, actual_tuple)
        print("At stairs! Stepping UP to warp to 1F...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        print("Final position after warping:", mgba.get_coordinates())
    else:
        # Return to start to be safe
        if actual_tuple != start_tuple:
            print("Returning to start position to preserve location state...")
            navigate_to(start_tuple, actual_tuple)
            print("Returned to start:", mgba.get_coordinates())
