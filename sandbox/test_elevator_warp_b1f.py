import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (24, 14)
# Let's walk Down along Column 24 as far as possible (up to Row 20)
for i in range(14, 21):
    pos = move(["Down"])
    # If our coordinates change to something else (e.g. inside the elevator, which has a different map/coordinates), we warped!
    # Or if we got blocked, we stop.
    if pos['y'] != i + 1:
        print(f"Blocked at {pos}")
        break

print("Final position after script:", mgba.get_coordinates())
mgba.take_screenshot()
