import mgba
import time
import os
from PIL import Image

def take_and_save_screenshot(label):
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    # Save to sandbox
    img.save(f"{label}.png")
    print(f"Saved screenshot: {label}.png")

# 1. Dismiss any active textboxes
mgba.press_buttons(["B"])
time.sleep(0.5)

# 2. Get current coordinates
pos = mgba.get_coordinates()
print(f"Current position: {pos}")

# If we are not at (2, 12), walk to it
if pos == {"x": 1, "y": 10}:
    print("Walking back to (2, 12)...")
    mgba.press_buttons(["Down", "sleep 500", "Down", "sleep 500", "Right", "sleep 500", "Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print(f"Position: {pos}")

# Ensure we are facing UP at (2, 12)
if pos == {"x": 2, "y": 12}:
    print("Facing UP at (2, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Let's interact with the switch step-by-step and take screenshots!
    print("Step 1: Pressing A to open dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    take_and_save_screenshot("mansion_switch_dialogue_open")
    
    print("Step 2: Pressing A to advance to YES/NO...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    take_and_save_screenshot("mansion_switch_dialogue_step2")
    
    print("Step 3: Pressing A to select YES...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    take_and_save_screenshot("mansion_switch_dialogue_step3")
    
    print("Step 4: Pressing A to dismiss...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    take_and_save_screenshot("mansion_switch_dialogue_final")
    
    # Now check if Column 1 Row 9 is open
    print("Testing Column 1 Row 9...")
    mgba.press_buttons(["Left", "sleep 500", "Up", "sleep 500", "Up", "sleep 500", "Up"])
    time.sleep(2.0)
    pos2 = mgba.get_coordinates()
    print(f"Position after trying to cross Row 9: {pos2}")
else:
    print("Not at (2, 12). Cannot proceed.")
