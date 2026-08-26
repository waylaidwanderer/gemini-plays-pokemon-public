import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = check_pos()

# Define the bypass steps to (12, 10)
steps = [
    ("Down", {"x": 9, "y": 11}),
    ("Left", {"x": 8, "y": 11}),
    ("Left", {"x": 7, "y": 11}),
    ("Left", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
    ("Up", {"x": 5, "y": 10}),
    ("Up", {"x": 5, "y": 9}),
    ("Up", {"x": 5, "y": 8}),
    ("Up", {"x": 5, "y": 7}),
    ("Right", {"x": 6, "y": 7}),
    ("Right", {"x": 7, "y": 7}),
    ("Right", {"x": 8, "y": 7}),
    ("Right", {"x": 9, "y": 7}),
    ("Right", {"x": 10, "y": 7}),
    ("Right", {"x": 11, "y": 7}),
    ("Right", {"x": 12, "y": 7}),
    ("Right", {"x": 13, "y": 7}),
    ("Down", {"x": 13, "y": 8}),
    ("Down", {"x": 13, "y": 9}),
    ("Down", {"x": 13, "y": 10}),
    ("Left", {"x": 12, "y": 10}),
]

for d, expected in steps:
    # Try moving
    mgba.press_buttons([d])
    time.sleep(0.55)
    
    # Handle wild battles if any
    # (Checking for white/black text box color)
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
        print("Battle or dialogue detected! Stopping script to let player escape.")
        break
        
    pos = mgba.get_coordinates()
    if pos == expected:
        print(f"Successfully moved {d} to {pos}")
    else:
        print(f"FAILED to move {d} to {expected}. Actual position: {pos}")
        break

print("Testing done!")
