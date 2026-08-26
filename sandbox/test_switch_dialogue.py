import mgba
import time
from PIL import Image

# Walk to (1, 11) and try interacting with (2, 11)
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Walk to (1, 11) if needed
if pos != {"x": 1, "y": 11}:
    steps = []
    if pos["y"] < 13:
        for y in range(pos["y"] + 1, 14):
            steps.append(("Down", {"x": pos["x"], "y": y}))
    if pos["x"] > 1:
        for x in range(pos["x"] - 1, 0, -1):
            steps.append(("Left", {"x": x, "y": 13}))
    if pos["y"] > 13:
        for y in range(pos["y"] - 1, 12, -1):
            steps.append(("Up", {"x": pos["x"], "y": y}))
    if pos["x"] < 1:
        for x in range(pos["x"] + 1, 2):
            steps.append(("Right", {"x": x, "y": 13}))
            
    # From (1, 13) walk up to (1, 11)
    steps.append(("Up", {"x": 1, "y": 12}))
    steps.append(("Up", {"x": 1, "y": 11}))
    
    for d, c in steps:
        mgba.press_buttons([d])
        time.sleep(0.4)

pos = mgba.get_coordinates()
print("Reached position:", pos)

# Turn RIGHT
mgba.press_buttons(["Right"])
time.sleep(0.5)

# Press A
mgba.press_buttons(["A"])
time.sleep(1.2)

# Screenshot
scr = mgba.take_screenshot()
img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
cropped = img.crop((0, 104, 160, 144))

colors = cropped.getcolors()
print("Unique colors in dialogue:", len(colors) if colors else "Many")
img.save("mansion_switch_dialogue_open.png")
print("Saved full screenshot to mansion_switch_dialogue_open.png")
