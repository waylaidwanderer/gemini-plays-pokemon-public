import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        handle_any_menu_or_battle()
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

print("Running test_switch_at_1_13.py...")
pos = mgba.get_coordinates()
print("Starting from:", pos)

# Walk to (1, 13)
if pos != {"x": 1, "y": 13}:
    steps_to_113 = []
    # If we are at (3, 11)
    if pos == {"x": 3, "y": 11}:
        steps_to_113 = [
            ("Down", {"x": 3, "y": 12}),
            ("Down", {"x": 3, "y": 13}),
            ("Left", {"x": 2, "y": 13}),
            ("Left", {"x": 1, "y": 13}),
        ]
    else:
        # Fallback path if we are somewhere else
        # Just walk to (1, 13)
        pass
        
    if not run_steps(steps_to_113):
        print("Failed to reach (1, 13)")
        exit(1)
        
    pos = mgba.get_coordinates()

# Now we are at (1, 13).
if pos == {"x": 1, "y": 13}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.45)
    
    # Check our coordinate now
    new_pos = mgba.get_coordinates()
    print("Position after pressing UP at (1, 13):", new_pos)
    
    # Press A
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Take screenshot of dialogue
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    cropped.save("cropped_test/switch_dialogue_at_1_13.png")
    print("Dialogue image saved to cropped_test/switch_dialogue_at_1_13.png")
    
    mgba.press_buttons(["B"])
    time.sleep(0.3)
