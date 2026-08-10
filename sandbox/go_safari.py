import time
import bridge

print("Running go_safari.py - Walking around Rhydon statues on Row 36")

# Current position: (6, 33) facing Left
# Step 1: Walk Right to Column 8
print("Walking Right to Column 8...")
for i in range(2):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 2: Walk Down to Row 36
print("Walking Down to Row 36...")
for i in range(3):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

# Step 3: Walk Left to transition to Area 3 (West)
print("Walking Left to transition...")
for i in range(12):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
    c = bridge.get_coordinates()
    print(f"Step {i+1} Coords: {c}")
