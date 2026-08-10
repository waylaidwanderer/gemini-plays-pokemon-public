import time
import bridge

print("Starting test_col22_north.py")

# Walk Left to (22, 32)
print("Moving Left to (22, 32)...")
bridge.press_buttons(["Left"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Walk Up to (22, 31)
print("Moving Up to (22, 31)...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Walk Up to (22, 30)
print("Moving Up to (22, 30)...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")
