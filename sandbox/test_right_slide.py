import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Testing Right exploration from (18, 15)...")
# We are at (18, 15)
move(["Right"]) # to (19, 15)
move(["Right"]) # to (20, 15)

# Try walking Down
pos = mgba.get_coordinates()
move(["Down"])
new_pos = mgba.get_coordinates()
if new_pos == pos:
    print("Blocked going Down from (20, 15)")

# Try walking Right
pos = mgba.get_coordinates()
move(["Right"])
new_pos = mgba.get_coordinates()
if new_pos == pos:
    print("Blocked going Right from (20, 15)")

screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
