import mgba

print("Start pos:", mgba.get_coordinates())

# Move Down to row 20 (2 steps Down)
mgba.press_buttons(["Down", "Down"])
print("At row 20:", mgba.get_coordinates())
mgba.take_screenshot()

# Walk Right 12 steps to see east of Gym
mgba.press_buttons(["Right"] * 12)
print("After 12 Right:", mgba.get_coordinates())
mgba.take_screenshot()

# Try walking Up 5 steps
mgba.press_buttons(["Up"] * 5)
print("After 5 Up:", mgba.get_coordinates())
mgba.take_screenshot()
