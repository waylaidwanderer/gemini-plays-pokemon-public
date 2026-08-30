import mgba
import time

pos = mgba.get_coordinates()
print(f"Starting gate check from {pos}")

# Steps:
# Up to Row 3 (6 -> 3 is 3 steps)
# Left to Col 22 (26 -> 22 is 4 steps)
# Up to Row 2 (3 -> 2 is 1 step)
# Left to Col 21 (22 -> 21 is 1 step)

path = ["Up", "Up", "Up", "Left", "Left", "Left", "Left", "Up"]
for btn in path:
    mgba.press_buttons([btn])
    time.sleep(0.4)

pos_mid = mgba.get_coordinates()
print(f"Position before trying gate: {pos_mid}")

# Try to step left to Col 21
mgba.press_buttons(["Left"])
time.sleep(0.4)

pos_after = mgba.get_coordinates()
print(f"Position after trying gate: {pos_after}")
if pos_after['x'] == 21 and pos_after['y'] == 2:
    print("GATE IS OPEN! WE ARE IN STATE A.")
else:
    print("GATE IS CLOSED! WE ARE IN STATE B.")
