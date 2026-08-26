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

if p == {"x": 6, "y": 10}:
    # Walk to (2, 12) on 3F West
    print("Walking to (2, 12) on 3F West...")
    steps = [
        ("Down", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
        ("Left", {"x": 2, "y": 11}),
        ("Down", {"x": 2, "y": 12}),
    ]
    for d, expected in steps:
        mgba.press_buttons([d])
        time.sleep(0.55)
        # Handle wild battle if any
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
            print("Battle detected during walking! Stopping script to let player run.")
            exit(1)
            
        p = check_pos()
        if p != expected:
            print(f"Failed to reach {expected}, actual: {p}")
            exit(1)
            
    # Face UP
    print("Facing UP towards 3F West switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Press A to open switch dialogue
    print("Pressing A on switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Toggle switch to State B
    print("Selecting YES...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Dismiss dialogue
    print("Dismissing dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    p = check_pos()
    print("Position after toggling switch:", p)
    
else:
    print("Not starting at (6, 10)")
