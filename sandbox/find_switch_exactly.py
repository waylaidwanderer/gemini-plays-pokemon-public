import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    # Check if a horizontal black border line of at least 110 pixels is present at y=112
    black_pixels = 0
    for x in range(10, 150):
        r, g, b = img.getpixel((x, 112))
        if r < 80 and g < 80 and b < 80:
            black_pixels += 1
            
    # Also check if the dialogue box area contains a solid white/cream background
    bg_pixels = 0
    for y in range(116, 140):
        for x in range(20, 140):
            r, g, b = img.getpixel((x, y))
            if abs(r - 247) < 10 and abs(g - 231) < 10 and abs(b - 214) < 10:
                bg_pixels += 1
                
    print(f"DEBUG Check: black_pixels={black_pixels}, bg_pixels={bg_pixels}")
    return black_pixels > 120 and bg_pixels > 1500

def handle_any_menu_or_battle():
    time.sleep(0.1)
    if is_dialogue_open():
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True
    return False

def walk_to_coord(target_x, target_y):
    retries = 10
    for _ in range(retries):
        pos = mgba.get_coordinates()
        if pos == {"x": target_x, "y": target_y}:
            return True
            
        dx = target_x - pos["x"]
        dy = target_y - pos["y"]
        
        if dx > 0:
            direction = "Right"
        elif dx < 0:
            direction = "Left"
        elif dy > 0:
            direction = "Down"
        elif dy < 0:
            direction = "Up"
        else:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.45)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            handle_any_menu_or_battle()
            time.sleep(0.3)
            
    return mgba.get_coordinates() == {"x": target_x, "y": target_y}

# Dismiss any active text boxes first
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting search at position:", pos)

# We are at (1, 10). Let's list all walkable/open floor tiles on the west side
open_tiles = [
    (1, 10), (1, 11), (1, 12), (1, 13),
    (2, 13), (3, 13), (4, 13), (5, 13),
    (5, 12), (5, 11), (5, 10), (5, 9), (5, 8),
    (4, 10), (4, 11), (4, 12),
]

directions = ["Up", "Right", "Down", "Left"]

found_switch = False
for tile in open_tiles:
    tx, ty = tile
    print(f"Moving to tile ({tx}, {ty})...")
    if not walk_to_coord(tx, ty):
        print(f"Failed to reach tile ({tx}, {ty}), skipping.")
        continue
        
    for d in directions:
        print(f"At ({tx}, {ty}), facing {d}...")
        mgba.press_buttons([d])
        time.sleep(0.4)
        
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        if is_dialogue_open():
            print(f"!!! SUCCESS !!! Found active switch at tile ({tx}, {ty}) facing {d}!")
            found_switch = True
            
            mgba.press_buttons(["A"]) # Advance "A secret switch!"
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Select YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
            time.sleep(1.2)
            print("Switch successfully toggled!")
            break
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.3)
            
    if found_switch:
        break

if not found_switch:
    print("Failed to find any active switch statue in the entire 3F West room!")

