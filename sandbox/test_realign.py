import time
import bridge

print("Walking step-by-step to diagnose Gatehouse path...")

coords = bridge.get_coordinates()
print(f"Starting Coords: {coords}")

# 1. Down to row 9
print("Pressing DOWN...")
bridge.press_buttons(["Down"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

# 2. Right to column 22
for i in range(3):
    print(f"Pressing RIGHT {i+1}...")
    bridge.press_buttons(["Right"])
    time.sleep(1.0)
    coords = bridge.get_coordinates()
    print(f"Coords: {coords}")

# 3. Up to row 4
for i in range(6):
    print(f"Pressing UP {i+1}...")
    bridge.press_buttons(["Up"])
    time.sleep(1.0)
    coords = bridge.get_coordinates()
    print(f"Coords: {coords}")

