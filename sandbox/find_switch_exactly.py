import mgba
import time
from PIL import Image

def check_for_dialogue():
    time.sleep(0.1)
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
        return True
    return False

def try_interact(pos, direction):
    # Turn in direction
    mgba.press_buttons([direction])
    time.sleep(0.4)
    # Check if we moved
    new_pos = mgba.get_coordinates()
    if new_pos != pos:
        # Move back and return False
        opp = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([opp])
        time.sleep(0.4)
        return False, new_pos
    
    # We didn't move, so we are facing a solid tile! Let's press A to check if it's the switch statue!
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    if check_for_dialogue():
        print(f"SWITCH FOUND! Standing at {pos} facing {direction}!")
        # Dismiss dialogue
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True, pos
    return False, pos

# Start of search
pos = mgba.get_coordinates()
print("Starting search from position:", pos)

walkable_tiles = [
    {"x": 2, "y": 11},
    {"x": 2, "y": 12},
    {"x": 2, "y": 13},
    {"x": 1, "y": 13},
    {"x": 1, "y": 12},
    {"x": 1, "y": 11},
]

def walk_to(target_pos):
    current = mgba.get_coordinates()
    # Walk X
    while current["x"] != target_pos["x"]:
        d = "Right" if target_pos["x"] > current["x"] else "Left"
        mgba.press_buttons([d])
        time.sleep(0.4)
        current = mgba.get_coordinates()
    # Walk Y
    while current["y"] != target_pos["y"]:
        d = "Down" if target_pos["y"] > current["y"] else "Up"
        mgba.press_buttons([d])
        time.sleep(0.4)
        current = mgba.get_coordinates()

for tile in walkable_tiles:
    print(f"Testing tile: {tile}")
    walk_to(tile)
    curr = mgba.get_coordinates()
    if curr != tile:
        print(f"Skipping blocked tile {tile}")
        continue
    
    # Try facing all 4 directions and pressing A
    for d in ["Up", "Down", "Left", "Right"]:
        found, _ = try_interact(curr, d)
        if found:
            exit(0)

print("Statue search complete, none found.")
