import mgba
import time

print("Opening Start menu...")
mgba.press_buttons(["Start", "sleep 400"])

print("Selecting POKéMON...")
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 800"])

print("Selecting TRUFFLE (Slot 6)...")
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 180"])
mgba.press_buttons(["A", "sleep 800"])

print("Selecting DIG...")
mgba.press_buttons(["A", "sleep 1500"]) # DIG is option 1 in the menu
time.sleep(3.0)

print("Should be outside on Cinnabar Island! Position:", mgba.get_coordinates())
