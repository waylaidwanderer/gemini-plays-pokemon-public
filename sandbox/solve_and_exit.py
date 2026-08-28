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
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))[:3]
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss run text
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

# 1. Complete Switch Dialogue
print("Pressing A to select YES...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Pressing B to dismiss any final switch dialogue...")
mgba.press_buttons(["B"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Position after dialogue:", pos)
mgba.take_screenshot()

# 2. Walk from current position (2, 12) on 3F West to stairs at (7, 10)
steps_3f = [
    ("Right", {"x": 3, "y": 12}),
    ("Up", {"x": 3, "y": 11}),
    ("Right", {"x": 4, "y": 11}),
    ("Right", {"x": 5, "y": 11}),
    ("Right", {"x": 6, "y": 11}),
    ("Right", {"x": 7, "y": 11}),
    ("Up", {"x": 7, "y": 10})
]

print("Executing 3F West walk to stairs...")
for d, c in steps_3f:
    walk_step(d, c)

pos = mgba.get_coordinates()
print("Position after 3F walk (should be 2F West landing):", pos)
mgba.take_screenshot()

# 3. Walk on 2F West from landing to stairs at (5, 10)
# Landing is (7, 11)
steps_2f = [
    ("Left", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
    ("Up", {"x": 5, "y": 10})
]

print("Executing 2F West walk to stairs...")
for d, c in steps_2f:
    walk_step(d, c)

pos = mgba.get_coordinates()
print("Position after 2F walk (should be 1F West landing):", pos)
mgba.take_screenshot()

# 4. Walk on 1F West from landing to exit at (5, 27)
# Landing on 1F is likely (5, 11) or adjacent. Let's trace from whatever current pos is.
# Let's dynamically generate the 1F walk steps to (5, 27) based on landing position.
pos = mgba.get_coordinates()
print("Dynamic 1F West walk start position:", pos)

steps_1f = []
if pos["x"] == 5:
    for y in range(pos["y"] + 1, 28):
        steps_1f.append(("Down", {"x": 5, "y": y}))

print(f"Executing 1F West walk steps: {steps_1f}")
for d, c in steps_1f:
    walk_step(d, c)

# 5. Exit the Mansion
pos = mgba.get_coordinates()
if pos == {"x": 5, "y": 27}:
    print("At exit tile (5, 27)! Exiting mansion...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    print("Final position after exiting:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print(f"Failed to reach (5, 27). Current position: {pos}")

