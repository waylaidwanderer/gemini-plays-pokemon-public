import time
import bridge

print("Starting test_gate.py...")

# Try walking UP to (8, 23)
bridge.press_buttons(["Up"])
time.sleep(0.7)
pos1 = bridge.get_coordinates()
print(f"Coordinates after Up: {pos1}")

# Try walking LEFT to (7, 23)
bridge.press_buttons(["Left"])
time.sleep(0.7)
pos2 = bridge.get_coordinates()
print(f"Coordinates after Left: {pos2}")

# Try walking DOWN to (7, 24)
bridge.press_buttons(["Down"])
time.sleep(0.7)
pos3 = bridge.get_coordinates()
print(f"Coordinates after Down from (7, 23): {pos3}")

# Try walking LEFT to (6, 23)
bridge.press_buttons(["Left"])
time.sleep(0.7)
pos4 = bridge.get_coordinates()
print(f"Coordinates after Left to col 6: {pos4}")

# Try walking DOWN to (6, 24)
bridge.press_buttons(["Down"])
time.sleep(0.7)
pos5 = bridge.get_coordinates()
print(f"Coordinates after Down on col 6: {pos5}")
