import time
import bridge

print("Running go_safari.py - Descending plateau and walking to Gold Teeth")

# Current position: (19, 16) on the plateau facing UP.
# Step 1: Walk Right to Column 21
print("Walking Right to Column 21...")
for i in range(2):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 2: Walk Down to (21, 18) (descend stairs)
print("Walking Down to (21, 18)...")
for i in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 3: Walk Left to (19, 18)
print("Walking Left to (19, 18)...")
for i in range(2):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 4: Walk Down to (19, 25) (Gold Teeth)
print("Walking Down to (19, 25) for Gold Teeth...")
for i in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords at Gold Teeth spot: {bridge.get_coordinates()}")

# Step 5: Press A to pick up Gold Teeth
print("Picking up Gold Teeth...")
bridge.press_buttons(["A"])
time.sleep(1.0)
print("A button pressed.")
