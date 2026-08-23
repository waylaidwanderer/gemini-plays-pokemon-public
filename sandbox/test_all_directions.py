import mgba
import time

def get_pos():
    return mgba.get_coordinates()

print("Testing all directions from current position...")
print("Initial pos:", get_pos())

# Try walking Down
mgba.press_buttons(["Down", "sleep 250"])
pos_down = get_pos()
print("After Down:", pos_down)

if pos_down != {'x': 1, 'y': 10}:
    # Go back to (1, 10)
    mgba.press_buttons(["Up", "sleep 250"])
    print("Returned to:", get_pos())

# Try walking Right
mgba.press_buttons(["Right", "sleep 250"])
pos_right = get_pos()
print("After Right:", pos_right)

if pos_right != {'x': 1, 'y': 10}:
    # Go back to (1, 10)
    mgba.press_buttons(["Left", "sleep 250"])
    print("Returned to:", get_pos())

# Try walking Up
mgba.press_buttons(["Up", "sleep 250"])
pos_up = get_pos()
print("After Up:", pos_up)

if pos_up != {'x': 1, 'y': 10}:
    # Go back to (1, 10)
    mgba.press_buttons(["Down", "sleep 250"])
    print("Returned to:", get_pos())

sc = mgba.take_screenshot()
print("Screenshot:", sc)
