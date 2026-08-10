import time
import bridge

print("Testing left-ward path from (19, 20)...")

# Current position: (19, 20) facing UP
print("1. Walking DOWN to (19, 21)...")
bridge.press_buttons(["Down"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

print("2. Walking LEFT to (18, 21)...")
bridge.press_buttons(["Left"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

print("3. Walking LEFT to (17, 21)...")
bridge.press_buttons(["Left"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

print("4. Walking LEFT to (16, 21)...")
bridge.press_buttons(["Left"])
time.sleep(1.0)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

