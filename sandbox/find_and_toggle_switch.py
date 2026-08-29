import mgba
import time
from PIL import Image

def wait_and_screen(label):
    time.sleep(0.5)
    img_path = mgba.take_screenshot()
    img = Image.open(img_path)
    img.save(f"sandbox/screenshots/cropped/{label}.png")
    print(f"Captured: {label}")

# We are on "A secret switch!" dialogue.
# Let's press A to advance
print("Pressing A (1)...")
mgba.press_buttons(["A"])
wait_and_screen("switch_step_1")

# Let's press A again (to select Yes if it's "Press it?", or advance if it's something else)
print("Pressing A (2)...")
mgba.press_buttons(["A"])
wait_and_screen("switch_step_2")

# Let's press A again
print("Pressing A (3)...")
mgba.press_buttons(["A"])
wait_and_screen("switch_step_3")

# Let's press A again
print("Pressing A (4)...")
mgba.press_buttons(["A"])
wait_and_screen("switch_step_4")
