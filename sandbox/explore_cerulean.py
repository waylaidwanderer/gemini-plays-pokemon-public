import mgba
import time

print("Current pos:", mgba.get_coordinates())

# Let's explore East along row 18 from (10,18)
# Walk 15 steps Right to (25,18)
mgba.press_buttons(["Right"] * 15)
pos1 = mgba.get_coordinates()
print("After 15 Right:", pos1)
mgba.take_screenshot()

# Walk 5 steps Right to (30,18) or as far as possible
mgba.press_buttons(["Right"] * 5)
pos2 = mgba.get_coordinates()
print("After 5 more Right:", pos2)
mgba.take_screenshot()

# Try going Up from here
mgba.press_buttons(["Up"] * 5)
pos3 = mgba.get_coordinates()
print("After 5 Up:", pos3)
mgba.take_screenshot()
