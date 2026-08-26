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
            r, g, b = img_std.getpixel((x, y))
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
                r, g, b = img_std2.getpixel((x, y))
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

# Open start menu to see current map name
mgba.press_buttons(["B"])
time.sleep(0.5)

pos = mgba.get_coordinates()
print("Starting map check at position:", pos)

# Let's map out the room by systematically trying to walk onto every tile
# from Column 1 to 3, Row 10 to 16.
grid = {}

# We start at (1, 12). Let's go to (1, 10) first.
# To make it safe, we'll use single-step movements.
def try_move(direction, target):
    if handle_any_menu_or_battle():
        pass
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    if new_pos == target:
        return True
    return False

# Walk up to (1, 10)
try_move("Up", {"x": 1, "y": 11})
try_move("Up", {"x": 1, "y": 10})
pos = mgba.get_coordinates()
print("Arrived at:", pos)

# Now, let's probe all tiles by trying to step onto them and recording success
# We can do a simple breadth-first or depth-first search of walkable tiles in the room.
visited = set()
walkable = []
blocked = []

# Queue of tiles to explore: starting with current position
queue = [pos]
visited.add((pos["x"], pos["y"]))

directions = {
    "Up": lambda p: {"x": p["x"], "y": p["y"] - 1},
    "Down": lambda p: {"x": p["x"], "y": p["y"] + 1},
    "Left": lambda p: {"x": p["x"] - 1, "y": p["y"]},
    "Right": lambda p: {"x": p["x"] + 1, "y": p["y"]},
}

opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}

# Let's explore up to 30 tiles
for _ in range(40):
    if not queue:
        break
    curr = queue.pop(0)
    walkable.append(curr)
    
    # Try all 4 directions from curr
    for d, get_next in directions.items():
        nxt = get_next(curr)
        # Limit to the local room
        if nxt["x"] < 1 or nxt["x"] > 3 or nxt["y"] < 8 or nxt["y"] > 17:
            continue
        if (nxt["x"], nxt["y"]) in visited:
            continue
            
        # Try to step to nxt
        print(f"Trying to move from {curr} {d} to {nxt}...")
        if try_move(d, nxt):
            # Success! nxt is walkable. Add to queue
            print(f"-> Walkable: {nxt}")
            visited.add((nxt["x"], nxt["y"]))
            queue.append(nxt)
            # Step back to curr
            try_move(opposite[d], curr)
        else:
            # Blocked! nxt is solid (wall, gate, cabinet, or statue)
            print(f"-> Blocked: {nxt}")
            blocked.append(nxt)
            visited.add((nxt["x"], nxt["y"]))

print("Walkable tiles:", walkable)
print("Blocked tiles:", blocked)
