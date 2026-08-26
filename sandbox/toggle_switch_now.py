import mgba
import time
import os
from PIL import Image

# Ensure any active menus/dialogues are closed
mgba.press_buttons(["B"])
time.sleep(0.5)

pos = mgba.get_coordinates()
print(f"Starting toggle test from: {pos}")

# 1. Walk back to (2, 12)
if pos == {"x": 3, "y": 10}:
    print("Walking back to (2, 12)...")
    mgba.press_buttons(["Down", "sleep 500", "Down", "sleep 500", "Left", "sleep 500", "Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()

if pos == {"x": 2, "y": 12}:
    print("We are at (2, 12). Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle the switch step-by-step with screenshots
    print("Pressing A (1)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    print("Pressing A (2)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    print("Pressing A (3)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    print("Pressing A (4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Walk to (3, 10) and try walking UP to (3, 9)
    print("Walking to (3, 10) to test Column 3 Row 9...")
    mgba.press_buttons([
        "Down", "sleep 500",
        "Right", "sleep 500",
        "Up", "sleep 500",
        "Up", "sleep 500"
    ])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print(f"Position at (3, 10): {pos}")
    
    if pos == {"x": 3, "y": 10}:
        print("Attempting to walk UP to (3, 9)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        pos2 = mgba.get_coordinates()
        print(f"Final position after trying to cross Row 9: {pos2}")
        
        # Save a screenshot to verify
        scr_file = mgba.take_screenshot()
        img = Image.open(scr_file)
        img.save("mansion_switch_dialogue_final.png")
        print("Saved final screenshot.")
else:
    print("Failed to reach (2, 12)")
