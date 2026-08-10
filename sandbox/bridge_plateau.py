import time
import bridge

print("Starting bridge_plateau.py")

# Step 1: Down to (23, 22)
print("Moving Down to (23, 22)...")
bridge.press_buttons(["Down"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 2: Left 7 times to (16, 22)
for i in range(7):
    print(f"Moving Left ({i+1}/7)...")
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    print(f"Coords: {bridge.get_coordinates()}")

# Step 3: Down 6 times to (16, 28)
for i in range(6):
    print(f"Moving Down ({i+1}/6)...")
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
    print(f"Coords: {bridge.get_coordinates()}")
