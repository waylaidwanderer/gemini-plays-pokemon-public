import mgba
import time

print("Highlighting TRUFFLE (slot 6)...")
mgba.press_buttons(["Down", "Down", "Down", "Down", "Down"])
time.sleep(0.5)

print("Opening TRUFFLE's submenu...")
mgba.press_buttons(["A"])
time.sleep(1.0) # wait for submenu to appear

print("Selecting DIG...")
mgba.press_buttons(["A"])
time.sleep(2.5) # wait for DIG animation and warp to overworld

print("Warp complete! Checking final overworld position:")
pos = mgba.get_coordinates()
print("Position on Cinnabar Island:", pos)
mgba.take_screenshot()
