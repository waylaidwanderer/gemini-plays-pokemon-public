import mgba
import time

def walk_path(buttons):
    for btn in buttons:
        mgba.press_buttons([btn])
        time.sleep(0.1)
        pos = mgba.get_coordinates()
        print(f"Pressed {btn}, current position: {pos}")

pos = mgba.get_coordinates()
print(f"Starting position: {pos}")

if pos == {'x': 24, 'y': 14}:
    # Path: Right 2 to (26, 14), Down 7 to (26, 21), Left 2 to (24, 21), Down 7 to (24, 28), Left 5 to (19, 28), Up 1 to (19, 27)
    buttons = (
        ["Right"] * 2 +
        ["Down"] * 7 +
        ["Left"] * 2 +
        ["Down"] * 7 +
        ["Left"] * 5 +
        ["Up"] * 1
    )
    walk_path(buttons)
else:
    print("Not at (24, 14), cannot use hardcoded path.")
