import mgba
import sys
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

def check_dialogue(label):
    img = mgba.take_screenshot()
    pil_img = Image.open(img)
    cropped = pil_img.crop((0, 112, 160, 144))
    pixels = list(cropped.getdata())
    white_pixels = sum(1 for p in pixels if p[0] > 200 and p[1] > 200 and p[2] > 200)
    ratio = white_pixels / len(pixels)
    has_dlg = ratio > 0.5
    print(f"[{label}] Position: {get_pos()}, Has dialogue: {has_dlg} (ratio: {ratio:.4f})")
    cropped.save(f"crop_{label}.png")
    if has_dlg:
        # Close dialogue
        mgba.press_buttons(["B", "sleep 500"])
    return has_dlg

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
                # Flee from battle if blocked
                mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
                for _ in range(5):
                    mgba.press_buttons(["B", "sleep 150"])
        steps += 1
    return False

# Starting at (3, 11) facing LEFT
print("Current pos:", get_pos())

# 1. Stand at (3, 11) facing LEFT (towards 2, 11)
print("Testing (3, 11) facing LEFT...")
mgba.press_buttons(["Left", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
check_dialogue("step1")

# 2. Stand at (3, 10) facing LEFT (towards 2, 10)
print("Testing (3, 10) facing LEFT...")
walk_to(3, 10)
mgba.press_buttons(["Left", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
check_dialogue("step2")

# 3. Stand at (1, 10) facing RIGHT (towards 2, 10)
print("Testing (1, 10) facing RIGHT...")
walk_to(3, 12)
walk_to(1, 12)
walk_to(1, 10)
mgba.press_buttons(["Right", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
check_dialogue("step3")

# 4. Stand at (1, 11) facing RIGHT (towards 2, 11)
print("Testing (1, 11) facing RIGHT...")
walk_to(1, 11)
mgba.press_buttons(["Right", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
check_dialogue("step4")

# 5. Stand at (2, 12) facing UP (towards 2, 11)
print("Testing (2, 12) facing UP...")
walk_to(1, 12)
walk_to(2, 12)
mgba.press_buttons(["Up", "sleep 300"])
mgba.press_buttons(["A", "sleep 1000"])
check_dialogue("step5")

print("Probing complete.")
