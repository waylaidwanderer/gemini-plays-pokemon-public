import mgba
import time
from PIL import Image

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# Walk to (2, 12) and face UP
mgba.press_buttons(["Down"])
time.sleep(0.5)
mgba.press_buttons(["Right"])
time.sleep(0.5)
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Standing at:", mgba.get_coordinates())

# Step 1: Open dialogue
mgba.press_buttons(["A"])
time.sleep(1.2)
scr1 = mgba.take_screenshot()
img1 = Image.open(scr1).resize((160, 144), Image.Resampling.NEAREST)
img1.crop((0, 112, 160, 144)).save("cropped_test/switch_dialogue_step1.png")
print("Saved step1 dialogue screenshot")

# Step 2: Advance to prompt
mgba.press_buttons(["A"])
time.sleep(1.2)
scr2 = mgba.take_screenshot()
img2 = Image.open(scr2).resize((160, 144), Image.Resampling.NEAREST)
img2.crop((0, 112, 160, 144)).save("cropped_test/switch_dialogue_step2.png")
print("Saved step2 dialogue screenshot")

# Step 3: Select YES
mgba.press_buttons(["A"])
time.sleep(1.2)
scr3 = mgba.take_screenshot()
img3 = Image.open(scr3).resize((160, 144), Image.Resampling.NEAREST)
img3.crop((0, 112, 160, 144)).save("cropped_test/switch_dialogue_step3.png")
print("Saved step3 dialogue screenshot")

# Step 4: Dismiss
mgba.press_buttons(["A"])
time.sleep(1.2)
scr4 = mgba.take_screenshot()
img4 = Image.open(scr4).resize((160, 144), Image.Resampling.NEAREST)
img4.crop((0, 112, 160, 144)).save("cropped_test/switch_dialogue_final.png")
print("Saved step4 dialogue screenshot")

# Get final position
print("Final position:", mgba.get_coordinates())
