import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialogue background (high white/cream pixel count)
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    print(f"  Check dialogue box: white_cream_pixels={white_cream_pixels}")
    return white_cream_pixels > 3000

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

# BFS pathfinder to navigate between walkable coordinates on 2F West
walkable = {
    (1, 10), (1, 11), (1, 12), (1, 13),
    (2, 13),
    (3, 13),
    (4, 10), (4, 11), (4, 12), (4, 13),
    (5, 10), (5, 11), (5, 12), (5, 13),
    (6, 11), (7, 11)
}

def get_neighbors(node):
    x, y = node
    neighbors = []
    for dx, dy, d in [(-1, 0, 'Left'), (1, 0, 'Right'), (0, -1, 'Up'), (0, 1, 'Down')]:
        nxt = (x + dx, y + dy)
        if nxt in walkable:
            neighbors.append((nxt, d))
    return neighbors

def find_path(start, target):
    if start == target:
        return []
    queue = [(start, [])]
    visited = {start}
    while queue:
        curr, path = queue.pop(0)
        if curr == target:
            return path
        for nxt, d in get_neighbors(curr):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [(d, nxt)]))
    return None

def walk_step(direction, expected_coords):
    for i in range(15):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if (pos['x'], pos['y']) == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if (pos['x'], pos['y']) == expected_coords:
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}), current: {pos}")
        time.sleep(0.3)
    return False

def navigate_to(target):
    pos = mgba.get_coordinates()
    start_node = (pos['x'], pos['y'])
    if start_node == target:
        return True
    path = find_path(start_node, target)
    if not path:
        print(f"No path found from {start_node} to {target}")
        return False
    for d, c in path:
        if not walk_step(d, c):
            return False
    return True

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# Systematic search of all walkable positions and facing directions on 2F West
ordered_coords = [
    (1, 13), (1, 12), (1, 11), (1, 10),
    (2, 13),
    (3, 13),
    (4, 13), (4, 12), (4, 11), (4, 10),
    (5, 13), (5, 12), (5, 11), (5, 10),
    (6, 11), (7, 11)
]

directions = ["Up", "Down", "Left", "Right"]

print("Starting systematic search on 2F West...")
for coord in ordered_coords:
    print(f"\nNavigating to {coord}...")
    if not navigate_to(coord):
        print(f"Failed to navigate to {coord}, skipping...")
        continue
        
    for d in directions:
        print(f"  Facing {d}...")
        mgba.press_buttons([d])
        time.sleep(0.4)
        
        # Press A
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        if is_dialogue_open():
            current_pos = mgba.get_coordinates()
            print(f"\n🎉 SUCCESS!!! WORKING SWITCH FOUND AT {current_pos} FACING {d}!!!")
            # Let's save a screenshot to document it
            scr = mgba.take_screenshot()
            img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
            img.save("mansion_switch_dialogue_final.png")
            
            # Toggle it to State B!
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # toggle sound
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # dismiss text
            time.sleep(1.0)
            print("Switch successfully toggled to State B!")
            exit(0)
        else:
            # Dismiss any accidental menu
            mgba.press_buttons(["B"])
            time.sleep(0.35)

print("\nSearch complete. No working switch found in walkable area on 2F West!")
exit(1)
