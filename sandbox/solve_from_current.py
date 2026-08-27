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

# Ensure battle screen is dismissed
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.3)

start = mgba.get_coordinates()
print("BFS Start position:", start)

queue = [start]
visited = { (start["x"], start["y"]) }
parent = {} # maps child_coord (tuple) -> (direction_to_child, parent_coord_tuple)

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
    path_start_to_curr = get_path_to(current_tuple)
    for d in reversed(path_start_to_curr):
        rev_d = rev_dirs[d]
        mgba.press_buttons([rev_d])
        time.sleep(0.4)
        handle_any_menu_or_battle()
        
    path_start_to_target = get_path_to(target_tuple)
    for d in path_start_to_target:
        mgba.press_buttons([d])
        time.sleep(0.4)
        handle_any_menu_or_battle()

current_pos = (start["x"], start["y"])
target_found = None

try:
    while queue:
        curr_coord = queue.pop(0)
        curr_tuple = (curr_coord["x"], curr_coord["y"])
        
        if curr_tuple == (5, 27):
            print("Found exit tile at (5, 27)!")
            target_found = curr_tuple
            break
            
        if curr_tuple != current_pos:
            navigate_to(curr_tuple, current_pos)
            current_pos = curr_tuple
            
        actual = mgba.get_coordinates()
        actual_tuple = (actual["x"], actual["y"])
        if actual_tuple != curr_tuple:
            print(f"Desync! Expected {curr_tuple}, got {actual_tuple}")
            break
            
        for d, (dx, dy) in dirs.items():
            neighbor_tuple = (curr_tuple[0] + dx, curr_tuple[1] + dy)
            if neighbor_tuple in visited:
                continue
                
            mgba.press_buttons([d])
            time.sleep(0.4)
            handle_any_menu_or_battle()
            pos_after = mgba.get_coordinates()
            pos_after_tuple = (pos_after["x"], pos_after["y"])
            
            if pos_after_tuple == neighbor_tuple:
                visited.add(neighbor_tuple)
                parent[neighbor_tuple] = (d, curr_tuple)
                queue.append(pos_after)
                
                rev_d = rev_dirs[d]
                mgba.press_buttons([rev_d])
                time.sleep(0.4)
                handle_any_menu_or_battle()
            else:
                pass
finally:
    actual = mgba.get_coordinates()
    actual_tuple = (actual["x"], actual["y"])
    print(f"Ending scan. Visited {len(visited)} tiles.")
    if target_found:
        print(f"Path to exit: {get_path_to(target_found)}")
        if actual_tuple != target_found:
            print("Navigating to exit...")
            navigate_to(target_found, actual_tuple)
        print("At exit, stepping Down...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0)
        print("Final position after exiting:", mgba.get_coordinates())
    else:
        if actual_tuple != (start["x"], start["y"]):
            print("Returning to start...")
            navigate_to((start["x"], start["y"]), actual_tuple)
            print("Returned to start:", mgba.get_coordinates())
