import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dark grey color (57, 57, 57) of the text box border
    target_color = (57, 57, 57)
    found_target = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            # Match close to (57, 57, 57)
            if abs(r - 57) < 10 and abs(g - 57) < 10 and abs(b - 57) < 10:
                found_target += 1
                
    # Also check for the white/cream background (247, 231, 214) or similar
    bg_color = (247, 231, 214)
    found_bg = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if abs(r - 247) < 15 and abs(g - 231) < 15 and abs(b - 214) < 15:
                found_bg += 1
                
    print(f"Check: found_border={found_target}, found_bg={found_bg}")
    # A standard dialogue box has a border of at least 150 pixels and bg of at least 1000 pixels
    return found_target > 80 and found_bg > 500

def handle_any_menu_or_battle():
    time.sleep(0.1)
    if is_dialogue_open():
        # Dismiss any accidental dialogue or menu
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True
    return False

def walk_to_coord(target_x, target_y):
    # Standard walk function with battle handling
    retries = 10
    for _ in range(retries):
        pos = mgba.get_coordinates()
        if pos == {"x": target_x, "y": target_y}:
            return True
            
        # Determine direction
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
        
        # Check if we got into a battle
        # Simple battle detection or run-away
        # Let's see if our position changed
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We bumped or battle
            # Try to handle battle/menu
            handle_any_menu_or_battle()
            time.sleep(0.3)
            
    return mgba.get_coordinates() == {"x": target_x, "y": target_y}

# Dismiss any active text boxes first
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting search at position:", pos)

# List of open floor tiles in the 3F West room
open_tiles = [
    (1, 13), (2, 13), (3, 13), (4, 13), (5, 13),
    (1, 12), (4, 12), (5, 12),
    (1, 11), (4, 11), (5, 11),
    (1, 10), (4, 10), (5, 10),
]

# We are currently at (1, 11). Let's systematically visit each open tile and interact in 4 directions
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
        time.sleep(1.2)
        
        if is_dialogue_open():
            print(f"!!! SUCCESS !!! Found active switch at tile ({tx}, {ty}) facing {d}!")
            found_switch = True
            # Toggling switch
            mgba.press_buttons(["A"]) # Advance "A secret switch!"
            time.sleep(1.5)
            mgba.press_buttons(["A"]) # Select YES
            time.sleep(1.5)
            mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
            time.sleep(1.5)
            print("Switch successfully toggled!")
            break
        else:
            # If no dialogue, press B just in case we opened something else
            mgba.press_buttons(["B"])
            time.sleep(0.3)
            
    if found_switch:
        break

if not found_switch:
    print("Failed to find any active switch statue in the entire 3F West room!")
