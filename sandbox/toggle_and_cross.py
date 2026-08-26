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

if p == {"x": 5, "y": 8}:
    # Walk to (7, 11)
    print("Walking to (7, 11)...")
    steps = [
        ("Down", {"x": 5, "y": 9}),
        ("Down", {"x": 5, "y": 10}),
        ("Down", {"x": 5, "y": 11}),
        ("Right", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
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
            print("Battle detected during walking! Stopping script.")
            exit(1)
            
        p = check_pos()
        if p != expected:
            print(f"Failed to reach {expected}, actual: {p}")
            exit(1)
            
    # Try walking UP onto stairs at (7, 10)
    print("At (7, 11). Walking UP onto stairs...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Allow warp animation
    p = check_pos()
    print("Position after warp attempt:", p)
    
else:
    print("Not starting at (5, 8)")
