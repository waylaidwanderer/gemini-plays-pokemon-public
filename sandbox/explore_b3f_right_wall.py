import mgba
import time

pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

# Sequence of buttons to navigate to (16, 10)
buttons = [
    "Up", "Up", "Up", "Up", # to (3, 9)
    "Left",                 # to (2, 9)
    "Left",                 # to (1, 9)
    "Up", "Up",             # to (1, 7)
    "Right", "Right", "Right", "Right", # to (5, 7)
    "Down", "Down",         # to (5, 9)
    "Right", "Right",       # to (7, 9)
    "Up", "Up",             # to (7, 7)
    "Right", "Right", "Right", "Right", "Right", "Right", # to (13, 7)
    "Down", "Down", "Down", # to (13, 10) -> spins to (14, 12)
    "Up", "Up",             # to (14, 10)
    "Right", "Right"        # to (16, 10)
]

mgba.press_buttons(buttons)

pos = mgba.get_coordinates()
print(f"End Position: {pos}")

screenshot_path = mgba.take_screenshot()
print(f"Screenshot at End Position: {screenshot_path}")
