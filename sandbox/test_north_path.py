import mgba
import time

def move(buttons):
    for b in buttons:
        mgba.press_buttons([b])
        time.sleep(0.3)

print("Moving to row 20, then left to column 20...")
# From (28, 22), go Up 2, then Left 8
move(["Up", "Up", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"])

print("Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
