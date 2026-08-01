import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting exploration Left on Row 7 from B3F (25, 6)...")
# Current is (25, 6)
move(["Down"]) # (25, 7)

# Walk Left up to 8 steps to see if we reach Column 19 or 18
for i in range(8):
    pos = mgba.get_coordinates()
    move(["Left"])
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Hit wall going Left at: {pos}")
        break

# Let's take a screenshot to inspect
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
print("Final exploration position:", mgba.get_coordinates())
