import mgba
import time

print("Current Pos:", mgba.get_coordinates())

# 1. Walk to (2, 12) from (1, 10)
mgba.press_buttons(["Down", "sleep 450"]) # (1, 11)
mgba.press_buttons(["Down", "sleep 450"]) # (1, 12)
mgba.press_buttons(["Right", "sleep 450"]) # (2, 12)
mgba.press_buttons(["Up", "sleep 450"]) # Turn Up

# Press A once
print("Pressing A (1st time)...")
mgba.press_buttons(["A", "sleep 1200"])
sc1 = mgba.take_screenshot()
print("Screenshot 1:", sc1)

# Press A twice
print("Pressing A (2nd time)...")
mgba.press_buttons(["A", "sleep 1200"])
sc2 = mgba.take_screenshot()
print("Screenshot 2:", sc2)

# Press A 3rd time
print("Pressing A (3rd time)...")
mgba.press_buttons(["A", "sleep 1200"])
sc3 = mgba.take_screenshot()
print("Screenshot 3:", sc3)

# Press B to make sure it is closed
mgba.press_buttons(["B", "sleep 500"])
sc_final = mgba.take_screenshot()
print("Screenshot final:", sc_final)
