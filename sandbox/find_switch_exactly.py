import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    # Dialogue box border at y=112 (Check if solid black)
    r_border, g_border, b_border = img.getpixel((80, 112))
    is_border_black = r_border < 80 and g_border < 80 and b_border < 80
    
    # Dialogue box background at y=122 (Check if solid cream)
    r_bg, g_bg, b_bg = img.getpixel((80, 122))
    is_bg_cream = abs(r_bg - 247) < 10 and abs(g_bg - 231) < 10 and abs(b_bg - 214) < 10
    
    print(f"is_dialogue_open check: border=({r_border},{g_border},{b_border}) black={is_border_black}, bg=({r_bg},{g_bg},{b_bg}) cream={is_bg_cream}")
    return is_border_black and is_bg_cream

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

# We are at (1, 10). Let's list the open floor tiles
open_tiles = [
    (1, 10), (1, 11), (1, 12), (1, 13),
    (2, 13), (3, 13), (4, 13), (5, 13),
    (5, 12), (5, 11), (5, 10), (5, 8),
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

