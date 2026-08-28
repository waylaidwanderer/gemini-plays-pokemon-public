import mgba
import time

print("Pressing Start...")
mgba.press_buttons(["Start"])
time.sleep(1.0)

img = mgba.take_screenshot()
print("Menu open screenshot:", img)
