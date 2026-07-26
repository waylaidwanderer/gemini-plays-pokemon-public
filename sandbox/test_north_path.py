import mgba
import time

def move(buttons):
    for b in buttons:
        mgba.press_buttons([b])
        time.sleep(0.3)

# Start at (33, 20)
# Walk to (20, 22)
print("Moving down and left...")
move(["Down", "Down", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"])

# Print coordinates
print("Current Position:", mgba.get_coordinates())

# Take a screenshot to visualize
mgba.take_screenshot()
