import mgba
import time

def move(direction, steps=1):
    for i in range(steps):
        print(f"Moving {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.18)
        pos = mgba.get_coordinates()
        # Note: coordinates might be (0, 0) due to emulator/harness warning,
        # but the actual game character will move.

# We start at (9, 8)
print("Stepping Up 4 times to row 4...")
move("Up", 4)

print("Stepping Right 5 times to column 14...")
move("Right", 5)

time.sleep(0.5)
screenshot = mgba.take_screenshot()
print(f"Pathing completed. Screenshot: {screenshot}")
