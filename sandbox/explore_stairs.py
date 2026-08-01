import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# We are at (3, 15)
print("Testing surrounding areas from (3, 15)...")

# Let's try to walk Left and Down to explore the bottom-left area
move(["Left"]) # (2, 15)
move(["Left"]) # (1, 15)
move(["Down"]) # (1, 16)
move(["Down"]) # (1, 17)
move(["Down"]) # (1, 18)
move(["Down"]) # (1, 19)
move(["Right"]) # (2, 19)
move(["Right"]) # (3, 19)

# Let's see where we are!
pos = mgba.get_coordinates()
print("Current position:", pos)
