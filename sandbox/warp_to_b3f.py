import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Current position is (5, 15) on B2F
# Let's walk Left into (4, 15) stairs
pos = move(["Left"])

print("Final position after warp attempt:", mgba.get_coordinates())
mgba.take_screenshot()
