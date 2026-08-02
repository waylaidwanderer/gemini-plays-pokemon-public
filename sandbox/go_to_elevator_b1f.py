import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Walk Right 1 step to Column 25
if pos['x'] == 24 and pos['y'] == 7:
    pos = move(["Right"])

# Walk Down Column 25
if pos['x'] == 25:
    for i in range(pos['y'], 20):
        pos = move(["Down"])
        if pos['y'] != i + 1:
            print(f"Blocked at {pos}")
            break

print("Finished moving. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
