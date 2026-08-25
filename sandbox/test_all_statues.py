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
        # We don't expect battles in this test, but run if they occur
        mgba.press_buttons([direction])
        time.sleep(0.35)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
    return False

# Start at (5, 10) on 2F West
# Let's walk to Row 11 first
walk_step("Down", {"x": 5, "y": 11})

# We will test various locations:
# Format: (test_x, test_y), face_dir, description
tests = [
    # Column 3 statues (from Column 2)
    ({"x": 2, "y": 10}, "Right", "Statue (3, 10) from West"),
    ({"x": 2, "y": 12}, "Right", "Statue (3, 12) from West"),
    ({"x": 2, "y": 14}, "Right", "Statue (3, 14) from West"),
    
    # Column 3 statues (from Column 4)
    ({"x": 4, "y": 10}, "Left", "Statue (3, 10) from East"),
    ({"x": 4, "y": 12}, "Left", "Statue (3, 12) from East"),
    ({"x": 4, "y": 14}, "Left", "Statue (3, 14) from East"),
    
    # Column 3 statues (from Row 11, 13)
    ({"x": 3, "y": 11}, "Up", "Statue (3, 10) from South"),
    ({"x": 3, "y": 11}, "Down", "Statue (3, 12) from North"),
    ({"x": 3, "y": 13}, "Up", "Statue (3, 12) from South"),
    ({"x": 3, "y": 13}, "Down", "Statue (3, 14) from North"),
]

# Walk to a coordinate, face direction, press A, and check if dialogue opens
for coords, face_dir, desc in tests:
    # Walk to coords
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
        mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000"])
        break
    else:
        print(f"Failed: {desc}")
