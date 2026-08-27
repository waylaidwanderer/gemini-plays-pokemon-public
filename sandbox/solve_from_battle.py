import mgba
import time
from PIL import Image

def is_in_battle_or_menu():
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
    return percentage > 0.85

def escape_battle_safely():
    # If "appeared!" is on screen, press B to advance
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    if not is_in_battle_or_menu():
        print("No battle or menu detected.")
        return False
        
    print("Battle or menu detected! Attempting escape...")
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    if is_in_battle_or_menu():
        print("Still in battle menu. Pressing RUN...")
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(5):
            mgba.press_buttons(["B"])
            time.sleep(0.2)
    return True

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
            
        # Check if we are stuck in a battle first
        if escape_battle_safely():
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
                
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction} to {pos}")
            return True
            
        print(f"Move {direction} failed. Current: {pos}, Expected: {expected_coords}. Retrying...")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Escape from initial wild Ponyta battle
print("Escaping from wild Ponyta...")
escape_battle_safely()
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Starting from:", pos)

if pos == {"x": 22, "y": 3}:
    print("Walking to B1F West NORTH at (1, 5)...")
    steps = [
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
        ("Left", {"x": 18, "y": 5}),
        ("Left", {"x": 17, "y": 5}),
        ("Left", {"x": 16, "y": 5}),
        ("Left", {"x": 15, "y": 5}),
        ("Left", {"x": 14, "y": 5}),
        ("Left", {"x": 13, "y": 5}),
        ("Left", {"x": 12, "y": 5}),
        ("Left", {"x": 11, "y": 5}),
        ("Left", {"x": 10, "y": 5}),
        ("Left", {"x": 9, "y": 5}), # cross open gate at (9, 5)
        ("Left", {"x": 8, "y": 5}),
        ("Left", {"x": 7, "y": 5}),
        ("Left", {"x": 6, "y": 5}),
        ("Left", {"x": 5, "y": 5}),
        ("Left", {"x": 4, "y": 5}),
        ("Left", {"x": 3, "y": 5}),
        ("Left", {"x": 2, "y": 5}),
        ("Left", {"x": 1, "y": 5}),
    ]
    if run_steps(steps):
        print("Reached Secret Key standing tile at (1, 5)!")
    else:
        print("Failed to reach Secret Key")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 5}:
    print("Facing UP and interacting to retrieve the Secret Key...")
    mgba.press_buttons(["Up"]) # Face UP
    time.sleep(0.5)
    mgba.press_buttons(["A"]) # Interact with Key
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["A"]) # Advance through key acquisition text
        time.sleep(0.5)
    pos = mgba.get_coordinates()
    print("Position after retrieving Secret Key:", pos)

print("Finished script! Current position:", pos)
