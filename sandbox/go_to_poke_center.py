import time
import bridge

print("Running go_to_poke_center.py...")

# Start: (22, 6)
print("1. Walking UP to row 2...")
for _ in range(4):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("2. Walking RIGHT to col 37...")
for _ in range(15):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("3. Walking DOWN to row 8...")
for _ in range(6):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("4. Walking LEFT to col 19...")
for _ in range(18):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("5. Walking DOWN to row 9...")
bridge.press_buttons(["Down"])
time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("6. Walking RIGHT to col 26...")
for _ in range(7):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("7. Walking DOWN to row 14...")
for _ in range(5):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("8. Walking LEFT to col 22...")
for _ in range(4):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("9. Walking DOWN to row 21...")
for _ in range(7):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("10. Walking RIGHT to col 24...")
for _ in range(2):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("11. Walking DOWN to row 27...")
for _ in range(6):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("12. Walking LEFT to col 19 (in front of PC)...")
for _ in range(5):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
print(f"Coords: {bridge.get_coordinates()}")

print("13. Entering Pokémon Center...")
bridge.press_buttons(["Up"])
time.sleep(2.0)
print(f"Coords inside Pokémon Center: {bridge.get_coordinates()}")

