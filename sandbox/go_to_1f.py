import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("Position:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# Walk Left twice to (5, 10)
print("Moving to staircase at (5, 10)...")
mgba.press_buttons(["Left", "sleep 300", "Left", "sleep 300"])
time.sleep(1.0)
check_pos()

# Let's take a screenshot to see if we warped
mgba.take_screenshot()
