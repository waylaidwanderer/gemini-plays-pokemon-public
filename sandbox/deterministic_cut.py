import mgba
import time

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Navigating to POKéMON...")
buttons = ["Down"] * 10 + ["Up"] * 5 + ["A"]
mgba.press_buttons(buttons)
time.sleep(1.0)

print("Navigating to TRUFFLE...")
buttons = ["Down"] * 10 + ["Up"] * 4 + ["A"]
mgba.press_buttons(buttons)
time.sleep(1.0)

print("Selecting CUT...")
buttons = ["Down"] * 10 + ["Up"] * 3 + ["A"]
mgba.press_buttons(buttons)
time.sleep(2.0)

print("Done!")
