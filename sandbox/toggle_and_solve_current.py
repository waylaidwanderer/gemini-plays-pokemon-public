import mgba
import time

def walk_and_check(buttons):
    for btn in buttons:
        print(f"Pressing {btn}...")
        mgba.press_buttons([btn])
        time.sleep(0.3)
        print(f"Position: {mgba.get_coordinates()}")

# Current position is (6, 10)
# We want to walk:
# Down -> (6, 11)
# Left -> (5, 11)
# Left -> (4, 11)
# Left -> (3, 11)
# Down -> (3, 12)
# Left -> (2, 12)
# Up -> (2, 12) facing (2, 11)

path = ["Down", "Left", "Left", "Left", "Down", "Left", "Up"]
walk_and_check(path)

# Now we should be at (2, 12) facing Up.
# Let's interact with the switch:
# 1. Press A to open dialogue ("A secret switch!")
# 2. Press A to advance ("Press it?")
# 3. Press A to select YES ("Who wouldn't?")
# 4. Press A to dismiss dialogue
print("Interacting with switch...")
mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "A", "sleep 500", "A"])
time.sleep(2.0)

screenshot = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot}")
