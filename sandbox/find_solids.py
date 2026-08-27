import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
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

def walk_to_coord(target_x, target_y):
    # Simple direct pathing (we assume no obstacles between us on the open checkerboard room)
    current = mgba.get_coordinates()
    while current["x"] != target_x or current["y"] != target_y:
        if handle_any_menu_or_battle():
            current = mgba.get_coordinates()
            continue
            
        dx = target_x - current["x"]
        dy = target_y - current["y"]
        
        if dx < 0:
            mgba.press_buttons(["Left"])
        elif dx > 0:
            mgba.press_buttons(["Right"])
        elif dy < 0:
            mgba.press_buttons(["Up"])
        elif dy > 0:
            mgba.press_buttons(["Down"])
            
        time.sleep(0.45)
        new_pos = mgba.get_coordinates()
        if new_pos == current:
            # We got blocked!
            print(f"  Blocked while trying to move to ({target_x}, {target_y})")
            return False
        current = new_pos
    return True

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

start_pos = mgba.get_coordinates()
print("Starting search from:", start_pos)

# We will scan the entire room.
# Let's map all walkable and solid tiles in x: [1, 4], y: [10, 15]
walkable = set()
solids = set()

# Initialize queue with starting position
queue = [start_pos]
walkable.add((start_pos["x"], start_pos["y"]))

directions = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

# Simple BFS to find all reachable tiles and identify solid boundaries
while queue:
    curr = queue.pop(0)
    curr_x, curr_y = curr["x"], curr["y"]
    
    # Walk to the current node
    if not walk_to_coord(curr_x, curr_y):
        continue
        
    # Check all 4 directions
    for d, (dx, dy) in directions.items():
        nx, ny = curr_x + dx, curr_y + dy
        if nx < 1 or nx > 6 or ny < 10 or ny > 16:
            continue
            
        if (nx, ny) in walkable or (nx, ny) in solids:
            continue
            
        # Try to step in direction d
        mgba.press_buttons([d])
        time.sleep(0.45)
        
        # Check if we moved
        pos = mgba.get_coordinates()
        if pos == {"x": nx, "y": ny}:
            # It's walkable!
            walkable.add((nx, ny))
            queue.append(pos)
            # Walk back
            back_d = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[d]
            mgba.press_buttons([back_d])
            time.sleep(0.45)
        else:
            # It's solid!
            solids.add((nx, ny))

print("\n--- Map Scan Completed ---")
print("Walkable tiles:", sorted(list(walkable)))
print("Solid tiles:", sorted(list(solids)))

# Now, test every solid tile to see if it's a switch!
print("\n--- Testing Solid Tiles for Switches ---")
found = False
for sx, sy in sorted(list(solids)):
    # Find adjacent walkable tile to stand on and face the solid tile
    for d, (dx, dy) in directions.items():
        wx, wy = sx - dx, sy - dy # Walkable tile is opposite of offset
        if (wx, wy) in walkable:
            print(f"Testing solid tile ({sx}, {sy}) from ({wx}, {wy}) facing {d}...")
            # Walk to the standing tile
            if not walk_to_coord(wx, wy):
                continue
                
            # Face the solid tile
            mgba.press_buttons([d])
            time.sleep(0.45)
            
            # Double check we didn't move
            pos = mgba.get_coordinates()
            if pos != {"x": wx, "y": wy}:
                print(f"  Error: moved to {pos} instead of facing!")
                continue
                
            # Press A
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            
            if is_dialogue_open():
                print(f"  SUCCESS!!! Opened Mewtwo switch dialogue at solid ({sx}, {sy}) from ({wx}, {wy}) facing {d}!")
                # Toggle it!
                mgba.press_buttons(["A"]) # YES
                time.sleep(1.2)
                mgba.press_buttons(["A"]) # Result
                time.sleep(1.2)
                mgba.press_buttons(["A"]) # Dismiss
                time.sleep(1.0)
                found = True
                break
            else:
                mgba.press_buttons(["B"])
                time.sleep(0.3)
    if found:
        break

if found:
    print("Switch toggled successfully!")
else:
    print("No switch found among the solid tiles.")
