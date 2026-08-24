import mgba
import sys
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Fleeing...")
    time.sleep(2.0)
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 30
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            return True
        if x < target_x: direction = "Right"
        elif x > target_x: direction = "Left"
        elif y < target_y: direction = "Down"
        elif y > target_y: direction = "Up"
        pos_before, pos_after = walk_step(direction)
        if pos_before == pos_after:
            time.sleep(0.1)
            pos_now = get_pos()
            if pos_now == pos_before:
                run_from_battle()
        steps += 1
    return False

def check_dialogue():
    img = mgba.take_screenshot()
    pil_img = Image.open(img)
    cropped = pil_img.crop((0, 112, 160, 144))
    pixels = list(cropped.getdata())
    white_pixels = sum(1 for p in pixels if p[0] > 200 and p[1] > 200 and p[2] > 200)
    ratio = white_pixels / len(pixels)
    return ratio > 0.5, ratio

# We are currently at (1, 10). Let's test different spots!

# Spot 1: (1, 11) facing RIGHT
print("--- TESTING SPOT 1: (1, 11) facing RIGHT ---")
walk_to(1, 11)
mgba.press_buttons(["Right", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
has_dlg, r = check_dialogue()
print(f"Result at (1, 11) facing RIGHT: Has dialogue = {has_dlg} (ratio = {r:.4f})")
if has_dlg:
    print("SPOT 1 SUCCESS!")
    mgba.press_buttons(["B", "sleep 500"])

# Spot 2: (2, 12) facing UP
print("--- TESTING SPOT 2: (2, 12) facing UP ---")
walk_to(1, 12)
walk_to(2, 12)
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
has_dlg, r = check_dialogue()
print(f"Result at (2, 12) facing UP: Has dialogue = {has_dlg} (ratio = {r:.4f})")
if has_dlg:
    print("SPOT 2 SUCCESS!")
    mgba.press_buttons(["B", "sleep 500"])

# Spot 3: (3, 11) facing LEFT
print("--- TESTING SPOT 3: (3, 11) facing LEFT ---")
walk_to(3, 12)
walk_to(3, 11)
mgba.press_buttons(["Left", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
has_dlg, r = check_dialogue()
print(f"Result at (3, 11) facing LEFT: Has dialogue = {has_dlg} (ratio = {r:.4f})")
if has_dlg:
    print("SPOT 3 SUCCESS!")
    mgba.press_buttons(["B", "sleep 500"])

print("Testing complete.")
