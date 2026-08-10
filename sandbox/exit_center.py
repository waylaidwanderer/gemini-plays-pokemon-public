import time
import bridge

print("Running exit_center.py inside Pokémon Center...")

# Start: (13, 4)
print("1. Walking DOWN to row 7...")
for _ in range(3):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

print("2. Walking LEFT to column 3...")
for _ in range(10):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords: {coords}")

print("3. Exiting Pokémon Center (DOWN)...")
bridge.press_buttons(["Down"])
time.sleep(2.0) # Wait for transition loading

coords = bridge.get_coordinates()
print(f"Coords inside Fuchsia City overworld: {coords}")
