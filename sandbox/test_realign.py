import time
import bridge

print("Testing UP path at Column 8...")

# Start: (9, 32)
print("1. Walking LEFT to (8, 32)...")
bridge.press_buttons(["Left"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

print("2. Probing UP to row 31...")
bridge.press_buttons(["Up"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords after UP: {coords}")

if coords[1] < 32:
    print("SUCCESS! Column 8 is walkable going UP!")
    # Walk further UP to row 30
    bridge.press_buttons(["Up"])
    time.sleep(1.0)
    print(f"Final coords: {bridge.get_coordinates()}")
else:
    print("Column 8 is blocked. Returning to (9, 32)...")
    bridge.press_buttons(["Right"])
    time.sleep(1.0)

