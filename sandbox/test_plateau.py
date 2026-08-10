import time
import bridge

print("Starting test_plateau.py")

# Current position: (22, 18) inside Safari Zone Center.
# Step 1: Left to (21, 18)
print("Moving Left to (21, 18)...")
bridge.press_buttons(["Left"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 2: Up to (21, 17) (climb stairs)
print("Moving Up to (21, 17)...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 3: Up again to see if we can walk onto/along the plateau
print("Moving Up again...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")
