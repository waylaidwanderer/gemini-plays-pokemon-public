import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Currently at (7, 11) on 3F West facing LEFT
print("Currently at:", get_pos())

# Walk detour around partition and rubble to switch at (2, 11)
mgba.press_buttons(["Left", "sleep 250"]) # (6, 11)
mgba.press_buttons(["Up", "sleep 250"]) # (6, 10)
mgba.press_buttons(["Left", "sleep 250", "Left", "sleep 250"]) # (4, 10)
mgba.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "Down", "sleep 250"]) # (4, 13)
mgba.press_buttons(["Left", "sleep 250", "Left", "sleep 250", "Left", "sleep 250"]) # (1, 13)
mgba.press_buttons(["Up", "sleep 250", "Up", "sleep 250"]) # (1, 11)

print("Arrived at (1, 11)! Toggling switch to State B...")
mgba.press_buttons(["Right", "sleep 250", "A", "sleep 500", "B", "sleep 250"])
print("State B active! Position:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot:", sc)
