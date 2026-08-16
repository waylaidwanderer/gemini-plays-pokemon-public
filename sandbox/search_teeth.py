import mgba
import time

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(6):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def walk_to(tx, ty):
    print(f"Walking to ({tx}, {ty})...")
    while True:
        curr = mgba.get_coordinates()
        x, y = curr['x'], curr['y']
        if x == tx and y == ty:
            return True
        if x < tx: btn = "Right"
        elif x > tx: btn = "Left"
        elif y < ty: btn = "Down"
        else: btn = "Up"
        mgba.press_buttons([btn])
        time.sleep(0.42)
        new = mgba.get_coordinates()
        if new['x'] == x and new['y'] == y:
            escape_battle()
            time.sleep(0.5)

# We are at (19, 24).
# Walk LEFT to Column 16
walk_to(16, 24)
# Walk DOWN to Row 26 (Highway)
walk_to(16, 26)

# Now walk Row 26 from Column 10 to 25 and check coordinates and screenshots
print("Scanning Row 26 for the Gold Teeth item ball...")
for target_x in range(10, 26):
    walk_to(target_x, 26)
    screenshot_path = mgba.take_screenshot()
    print(f"Scanned ({target_x}, 26): Screenshot saved to {screenshot_path}")

print("Scan complete!")
