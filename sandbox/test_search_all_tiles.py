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
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        handle_any_menu_or_battle()
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

print("Running test_search_all_tiles.py...")
# Walk back to Column 2 Row 11
pos = mgba.get_coordinates()
if pos == {"x": 3, "y": 11}:
    walk_step("Left", {"x": 2, "y": 11})

pos = mgba.get_coordinates()
print("Starting search from:", pos)

# List of all tiles we want to visit and test
tiles_to_test = [
    {"x": 2, "y": 11},
    {"x": 2, "y": 12},
    {"x": 2, "y": 13},
    {"x": 2, "y": 14},
    {"x": 2, "y": 15},
    {"x": 1, "y": 15},
    {"x": 1, "y": 14},
    {"x": 1, "y": 13},
    {"x": 1, "y": 12},
    {"x": 1, "y": 11},
]

# We are at (2, 11) now.
# Let's write a route that visits these tiles and tests all 4 directions on each tile.
for tile in tiles_to_test:
    # Walk to tile
    curr = mgba.get_coordinates()
    if curr != tile:
        # Move vertically/horizontally
        dx = tile["x"] - curr["x"]
        dy = tile["y"] - curr["y"]
        if dx != 0:
            d = "Right" if dx > 0 else "Left"
            walk_step(d, {"x": curr["x"] + dx, "y": curr["y"]})
        curr = mgba.get_coordinates()
        if dy != 0:
            d = "Down" if dy > 0 else "Up"
            # Since walking UP or DOWN might be blocked if we do it wrong, 
            # let's just use walk_step
            walk_step(d, {"x": curr["x"], "y": curr["y"] + dy})
            
    # Now we are at tile. Let's test all 4 directions!
    curr = mgba.get_coordinates()
    print(f"Testing tile {curr}...")
    for direction in ["Up", "Right", "Down", "Left"]:
        # Turn to face direction
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        # Check if we walked onto another tile (if we did, we must walk back)
        new_pos = mgba.get_coordinates()
        if new_pos != curr:
            # We walked onto new_pos! Walk back to curr.
            opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
            mgba.press_buttons([opposite])
            time.sleep(0.45)
            continue
            
        # If we didn't move, we are facing direction! Press A to interact.
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        
        if is_dialogue_open():
            print(f"  SUCCESS!!! Switch dialogue opened standing at {curr} facing {direction}!")
            # Toggle switch to State B
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Result
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            print("Switch successfully toggled!")
            exit(0)
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.3)

print("Failed to find any active switch on these tiles.")
exit(1)
