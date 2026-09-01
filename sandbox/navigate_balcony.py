import mgba
import time

def press(button, count=1):
    for _ in range(count):
        mgba.press_buttons([button])
        time.sleep(0.35)
        pos = mgba.get_coordinates()
        print(f"Pressed {button}. Position is now {pos}")

print("Current coordinates:", mgba.get_coordinates())

# 1. Walk from (12, 11) to (3, 11)
print("Walking to (3, 11)...")
press("Left", 9)   # (12, 11) -> (3, 11)

# Verify we reached (3, 11)
pos = mgba.get_coordinates()
if pos != {'x': 3, 'y': 11}:
    print(f"Error: Expected to be at (3, 11), but actually at {pos}")
    exit(1)

# 2. Turn left and toggle switch
print("Toggling Mewtwo switch...")
press("Left", 1)  # Face Left towards (2, 11)

# 4 A-presses to complete dialogue
for i in range(1, 5):
    print(f"A-press {i}...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)

# 3. Walk from (3, 11) to the balcony and drop!
print("Walking to the balcony...")
press("Right", 9)  # (3, 11) -> (12, 11)
press("Down", 5)   # (12, 11) -> (12, 16)
press("Right", 9)  # (12, 16) -> (21, 16)
press("Down", 2)   # (21, 16) -> (21, 18)
press("Left", 2)   # (21, 18) -> (19, 18) (drop!)

print("Final position check:")
print(mgba.get_coordinates())
mgba.take_screenshot()
