import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Walk Down Column 25 as far as possible
for i in range(7, 25):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos}")
        break

print("Finished. Final position:", mgba.get_coordinates())
mgba.take_screenshot()
