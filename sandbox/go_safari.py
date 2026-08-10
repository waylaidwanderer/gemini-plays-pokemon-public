import time
import bridge

print("Running go_safari.py - Walking plateau to jump-down ledge")

# Current position: (21, 14) on the plateau facing UP.
# Step 1: Walk Left to Column 19
print("Walking Left to Column 19...")
for i in range(2):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 2: Walk Down to (19, 17)
print("Walking Down to (19, 17)...")
for i in range(3):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 3: Walk Down 1 more to jump down the ledge to (19, 18)
print("Jumping down the ledge to (19, 18)...")
bridge.press_buttons(["Down"])
time.sleep(1.0)
print(f"Coords after jump: {bridge.get_coordinates()}")
