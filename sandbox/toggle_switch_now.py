import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # We check if there's a white background in the dialogue area
    bg_color = (247, 231, 214)
    found_bg = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if abs(r - 247) < 15 and abs(g - 231) < 15 and abs(b - 214) < 15:
                found_bg += 1
                
    # Also check if there's a black border on row 112
    # In overworld, y=112 is pink/checkered. In dialogue, y=112 of cropped (which is y=112 on screen) is solid black border
    # Let's check cropped y=8 (which is y=112 on screen)
    black_pixels = 0
    for x in range(cropped.width):
        r, g, b = cropped.getpixel((x, 8))
        if r < 80 and g < 80 and b < 80:
            black_pixels += 1
            
    print(f"Dialogue Check: found_bg={found_bg}, black_pixels_border={black_pixels}")
    # Standard dialogue box has border line of black pixels (>100) and white bg (>1000)
    return found_bg > 1500 and black_pixels > 120

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

# Currently we are at (1, 13)
pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos != {"x": 1, "y": 13}:
    # Walk to (1, 13)
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == {"x": 2, "y": 13}:
        walk_step("Left", {"x": 1, "y": 13})
    elif pos == {"x": 1, "y": 10}:
        walk_step("Down", {"x": 1, "y": 11})
        walk_step("Down", {"x": 1, "y": 12})
        walk_step("Down", {"x": 1, "y": 13})
        
pos = mgba.get_coordinates()
print("Position before toggle:", pos)

if pos == {"x": 1, "y": 13}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print("Dialogue opened! Advancing and selecting YES...")
        mgba.press_buttons(["A"]) # Advance "A secret switch!"
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Select YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
        time.sleep(1.2)
        print("Toggle completed!")
    else:
        print("No dialogue opened. Pressing B to dismiss.")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
    # Check gate state by walking up to (1, 9)
    print("Checking gate state...")
    walk_step("Up", {"x": 1, "y": 12})
    walk_step("Up", {"x": 1, "y": 11})
    walk_step("Up", {"x": 1, "y": 10})
    success = walk_step("Up", {"x": 1, "y": 9})
    if success:
        print("!!! SUCCESS !!! Gate at (1, 9) is now OPEN!")
    else:
        print("Gate at (1, 9) is CLOSED.")

