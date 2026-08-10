import time
import bridge

print("Running go_safari.py (Center -> Area 1 East)...")

# Current position: (18, 8) facing DOWN in Safari Zone Center
# Step 1: Walk DOWN to row 23
print("Walking DOWN to row 23...")
for _ in range(15):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 23: {coords}")

# Step 2: Walk RIGHT to Column 29 and transition to Area 1 East
print("Walking RIGHT to transition to Area 1 East...")
for _ in range(12):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords inside Area 1 (East): {coords}")

