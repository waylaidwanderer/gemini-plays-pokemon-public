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
    if 0.90 < percentage < 0.999:
        print("Dialogue box detected!")
        return True
    return False

def walk_step(direction, expected_coords, retries=5):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.35)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
    return False

# Currently at (6, 10) on 2F West
# Walk to Row 11 first
walk_step("Down", {"x": 6, "y": 11})

# Column 8 statues tests
tests = [
    # Stand at (7, 10), face RIGHT towards (8, 10)
    ({"x": 7, "y": 10}, "Right", "Statue (8, 10) from West"),
    # Stand at (7, 12), face RIGHT towards (8, 12)
    ({"x": 7, "y": 12}, "Right", "Statue (8, 12) from West"),
    # Stand at (7, 14), face RIGHT towards (8, 14)
    ({"x": 7, "y": 14}, "Right", "Statue (8, 14) from West"),
    
    # Stand at (8, 11), face UP towards (8, 10)
    ({"x": 8, "y": 11}, "Up", "Statue (8, 10) from South"),
    # Stand at (8, 11), face DOWN towards (8, 12)
    ({"x": 8, "y": 11}, "Down", "Statue (8, 12) from North"),
    # Stand at (8, 13), face UP towards (8, 12)
    ({"x": 8, "y": 13}, "Up", "Statue (8, 12) from South"),
    # Stand at (8, 13), face DOWN towards (8, 14)
    ({"x": 8, "y": 13}, "Down", "Statue (8, 14) from North"),
]

for coords, face_dir, desc in tests:
    curr = mgba.get_coordinates()
    # Horizontal move
    while curr['x'] != coords['x']:
        d = "Right" if curr['x'] < coords['x'] else "Left"
        if not walk_step(d, {"x": curr['x'] + (1 if d == "Right" else -1), "y": curr['y']}):
            break
        curr = mgba.get_coordinates()
    # Vertical move
    while curr['y'] != coords['y']:
        d = "Down" if curr['y'] < coords['y'] else "Up"
        if not walk_step(d, {"x": curr['x'], "y": curr['y'] + (1 if d == "Down" else -1)}):
            break
        curr = mgba.get_coordinates()
        
    # Face direction
    mgba.press_buttons([face_dir, "sleep 150"])
    
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Check if dialogue is open
    if handle_any_menu_or_battle():
        print(f"SUCCESS! {desc} IS THE INTERACTIVE SWITCH!")
        # Toggle it!
        mgba.press_buttons(["A", "sleep 2000", "A", "sleep 1000"])
        break
    else:
        print(f"Failed: {desc}")
