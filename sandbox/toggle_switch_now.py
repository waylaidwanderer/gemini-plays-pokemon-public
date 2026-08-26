import mgba
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    # Dialogue box border at y=112 (Check if solid black)
    r_border, g_border, b_border = img.getpixel((80, 112))
    is_border_black = r_border < 80 and g_border < 80 and b_border < 80
    
    # Dialogue box background at y=122 (Check if solid cream/white)
    r_bg, g_bg, b_bg = img.getpixel((80, 122))
    is_bg_cream = abs(r_bg - 247) < 15 and abs(g_bg - 231) < 15 and abs(b_bg - 214) < 15
    is_bg_white = r_bg > 220 and g_bg > 220 and b_bg > 220
    
    return is_border_black and (is_bg_cream or is_bg_white)

def handle_battle():
    # Simple check for black/white pixel density in dialogue area
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img.getpixel((x, y))
            total_pixels += 1
            if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print("Battle/Menu detected! Attempting to escape...")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        # Try to run
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(4):
            mgba.press_buttons(["B"])
            time.sleep(0.3)
        return True
    return False

def walk_to(x, y):
    for attempt in range(5):
        pos = get_pos()
        if pos == {"x": x, "y": y}:
            return True
            
        dx = x - pos["x"]
        dy = y - pos["y"]
        
        if dx > 0:
            d = "Right"
        elif dx < 0:
            d = "Left"
        elif dy > 0:
            d = "Down"
        elif dy < 0:
            d = "Up"
        else:
            return True
            
        mgba.press_buttons([d])
        time.sleep(0.45)
        
        new_pos = get_pos()
        if new_pos == pos:
            print(f"Blocked at {pos} trying to go {d} to ({x}, {y})")
            if handle_battle():
                time.sleep(0.5)
    return get_pos() == {"x": x, "y": y}

# Main sequence
print("Current position:", get_pos())

# Step 1: Walk to (1, 12)
if walk_to(1, 12):
    # Step 2: Walk to (1, 13)
    if walk_to(1, 13):
        # Step 3: Walk to (2, 13)
        if walk_to(2, 13):
            print("Successfully reached (2, 13)!")
            # Step 4: Face UP
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            
            # Step 5: Interact with switch
            mgba.press_buttons(["A"])
            time.sleep(0.8)
            
            if is_dialogue_open():
                print("Dialogue open! Activating switch...")
                mgba.press_buttons(["A"]) # "A secret switch!"
                time.sleep(1.2)
                mgba.press_buttons(["A"]) # Select YES
                time.sleep(1.2)
                mgba.press_buttons(["A"]) # "Pressed it!"
                time.sleep(1.2)
                print("Switch successfully toggled to State B!")
            else:
                print("Dialogue did not open after pressing A at (2, 13) facing UP.")
        else:
            print("Failed to reach (2, 13)")
    else:
        print("Failed to reach (1, 13)")
else:
    print("Failed to reach (1, 12)")

print("Final position:", get_pos())
mgba.take_screenshot()
