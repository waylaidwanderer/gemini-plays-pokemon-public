import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

p = check_pos()

if p == {"x": 7, "y": 10}:
    # Walk Left on Row 10
    steps = [
        ("Left", {"x": 6, "y": 10}),
        ("Left", {"x": 5, "y": 10}),
    ]
    for d, expected in steps:
        mgba.press_buttons([d])
        time.sleep(0.55)
        p = check_pos()
        if p != expected:
            print(f"Failed to reach {expected}, actual: {p}")
            exit(1)
            
    # From (5, 10), walk UP Column 5
    steps_up = [
        ("Up", {"x": 5, "y": 9}),
        ("Up", {"x": 5, "y": 8}),
        ("Up", {"x": 5, "y": 7}),
        ("Up", {"x": 5, "y": 6}),
        ("Up", {"x": 5, "y": 5}),
    ]
    for d, expected in steps_up:
        mgba.press_buttons([d])
        time.sleep(0.55)
        
        # Handle battle if any
        scr = mgba.take_screenshot()
        from PIL import Image
        img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
        black_or_white = 0
        total_pixels = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img.getpixel((x, y))
                total_pixels += 1
                if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                    black_or_white += 1
        if black_or_white / total_pixels > 0.90:
            print("Battle detected! Stopping script.")
            exit(1)
            
        p = check_pos()
        if p != expected:
            print(f"BLOCKED at {p} trying to go to {expected}")
            break
else:
    print("Not starting at (7, 10)")
