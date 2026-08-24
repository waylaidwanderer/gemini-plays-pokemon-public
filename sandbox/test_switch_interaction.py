import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Stand at (1, 11) facing Right
print("Current Position:", get_pos())

# Interact with (2, 11)
print("Facing Right...")
mgba.press_buttons(["Right", "sleep 300"])

print("Pressing A (1st time)...")
mgba.press_buttons(["A", "sleep 800"])
sc1 = mgba.take_screenshot()
print("Screenshot after 1st A:", sc1)

print("Pressing A (2nd time)...")
mgba.press_buttons(["A", "sleep 800"])
sc2 = mgba.take_screenshot()
print("Screenshot after 2nd A:", sc2)

print("Pressing A (3rd time)...")
mgba.press_buttons(["A", "sleep 800"])
sc3 = mgba.take_screenshot()
print("Screenshot after 3rd A:", sc3)

mgba.press_buttons(["B", "sleep 300"])
