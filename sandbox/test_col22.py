import time
import bridge

print("Starting test_col22.py")

# Walk Left to (22, 15)
print("Moving Left to (22, 15)...")
bridge.press_buttons(["Left"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Walk Up to (22, 14)
print("Moving Up to (22, 14)...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Walk Up to (22, 13)
print("Moving Up to (22, 13)...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")
