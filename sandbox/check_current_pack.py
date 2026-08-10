import time
import mgba

print("Opening menu to check inventory...")
mgba.press_buttons(["Start", "sleep 500"])
# Take screenshot after Start
img_path1 = mgba.take_screenshot()
print(f"Screenshot after Start: {img_path1}")

print("Moving to PACK...")
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
# Take screenshot of PACK
img_path2 = mgba.take_screenshot()
print(f"Screenshot after entering PACK: {img_path2}")

# Let's scroll down to see more items
print("Scrolling down in PACK...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100"])
img_path3 = mgba.take_screenshot()
print(f"Screenshot after scrolling down: {img_path3}")

# Press B to close PACK and menu
print("Closing PACK...")
mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])
coords = mgba.get_coordinates()
print(f"Coordinates after closing menu: {coords}")
