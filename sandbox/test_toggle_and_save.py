import mgba
import time
from PIL import Image

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# Start from current position (3, 10)
# Walk DOWN twice to Row 12, then LEFT to Column 2, then UP to face the statue!
mgba.press_buttons(["Down"])
time.sleep(0.5)
mgba.press_buttons(["Down"])
time.sleep(0.5)
mgba.press_buttons(["Left"])
time.sleep(0.5)
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Standing at:", mgba.get_coordinates())

# Step 1: Open dialogue
mgba.press_buttons(["A"])
time.sleep(1.2)
scr1 = mgba.take_screenshot()
Image.open(scr1).save("cropped_test/switch_dialogue_step1_full.png")

# Step 2: Advance to Yes/No prompt
mgba.press_buttons(["A"])
time.sleep(1.2)
scr2 = mgba.take_screenshot()
Image.open(scr2).save("cropped_test/switch_dialogue_step2_full.png")

# Step 3: Select YES
mgba.press_buttons(["A"])
time.sleep(1.2)
scr3 = mgba.take_screenshot()
Image.open(scr3).save("cropped_test/switch_dialogue_step3_full.png")

# Step 4: Dismiss
mgba.press_buttons(["A"])
time.sleep(1.2)
scr4 = mgba.take_screenshot()
Image.open(scr4).save("cropped_test/switch_dialogue_final_full.png")

print("Toggled switch! Final position:", mgba.get_coordinates())
