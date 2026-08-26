import mgba
import time
from PIL import Image

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

pos = mgba.get_coordinates()
print("Starting position:", pos)

# Walk to (2, 12)
if pos == {"x": 1, "y": 10}:
    run_steps([
        ("Down", {"x": 1, "y": 11}),
        ("Right", {"x": 2, "y": 11}),
        ("Down", {"x": 2, "y": 12}),
    ])
    pos = mgba.get_coordinates()

# Now we are at (2, 12).
if pos == {"x": 2, "y": 12}:
    print("Facing UP at (2, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Capture before A press
    scr_before = mgba.take_screenshot()
    img_before = Image.open(scr_before)
    
    # Press A
    print("Pressing A...")
    mgba.press_buttons(["A", "sleep 1000"])
    
    scr_after = mgba.take_screenshot()
    img_after = Image.open(scr_after)
    
    # Check if identical
    is_identical = list(img_before.getdata()) == list(img_after.getdata())
    print("Screenshot before vs after A is identical:", is_identical)
    
    if not is_identical:
        print("Dialogue opened! Saving screenshots.")
        img_after.save("mansion_switch_dialogue_open.png")
    else:
        print("No dialogue opened. Let's try pressing A facing RIGHT or LEFT or DOWN to see if we can trigger anything.")

