import mgba
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

# Currently at (2, 12). Let's turn UP and do the interaction step-by-step
print("Current position:", get_pos())

print("Turning UP...")
mgba.press_buttons(["Up", "sleep 400"])

# Step 1: Press A to open dialogue
print("Pressing A (1)...")
mgba.press_buttons(["A", "sleep 1200"])
img1 = mgba.take_screenshot()
import os
if os.path.exists("switch_step_1.png"): os.remove("switch_step_1.png")
os.rename(img1, "switch_step_1.png")

# Step 2: Press A to advance to YES/NO
print("Pressing A (2)...")
mgba.press_buttons(["A", "sleep 1200"])
img2 = mgba.take_screenshot()
if os.path.exists("switch_step_2.png"): os.remove("switch_step_2.png")
os.rename(img2, "switch_step_2.png")

# Step 3: Press A to select YES
print("Pressing A (3)...")
mgba.press_buttons(["A", "sleep 1200"])
img3 = mgba.take_screenshot()
if os.path.exists("switch_step_3.png"): os.remove("switch_step_3.png")
os.rename(img3, "switch_step_3.png")

# Step 4: Press A to advance past "Who wouldn't?"
print("Pressing A (4)...")
mgba.press_buttons(["A", "sleep 1200"])
img4 = mgba.take_screenshot()
if os.path.exists("switch_step_4.png"): os.remove("switch_step_4.png")
os.rename(img4, "switch_step_4.png")

# Step 5: Press B to close
print("Pressing B...")
mgba.press_buttons(["B", "sleep 600"])

# Check final position
print("Final position:", get_pos())
