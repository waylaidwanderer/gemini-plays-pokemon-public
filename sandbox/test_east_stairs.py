import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Testing path to (19, 12) staircase on B3F...")
# We are at (20, 11)
move(["Left"]) # Go to (19, 11)
time.sleep(0.5)

# Attempt to walk Down to (19, 12)
pos = mgba.get_coordinates()
move(["Down"])
time.sleep(1.0)

new_pos = mgba.get_coordinates()
print("Final coordinates after walking Down:", new_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
