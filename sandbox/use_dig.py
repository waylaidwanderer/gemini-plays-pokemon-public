import mgba
import time

print("Opening Start Menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

print("Moving to POKéMON...")
mgba.press_buttons(["Down"])
time.sleep(0.3)

print("Selecting POKéMON...")
mgba.press_buttons(["A"])
time.sleep(0.8)

print("Selecting TRUFFLE...")
mgba.press_buttons(["A"])
time.sleep(0.8)

print("Using DIG...")
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Coordinates after DIG: ({pos['x']}, {pos['y']})")
