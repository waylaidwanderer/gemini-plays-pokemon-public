import mgba
import time

print("Opening START menu and going to POKéMON...")
mgba.press_buttons(["Start", "sleep 500", "Down", "sleep 200", "A", "sleep 800"])
print("Capturing party screenshot...")
mgba.take_screenshot()
print("Backing out of menu...")
mgba.press_buttons(["B", "sleep 400", "B", "sleep 400"])
