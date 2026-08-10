import time
import bridge

print("Running go_safari.py (Fuchsia Pokémon Center -> Safari Gatehouse)...")

# Start: (19, 28)
print("1. Walking LEFT to Column 1 on Row 28...")
for _ in range(18):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 1: {coords}")

# Step 2: Walk UP to row 21
print("2. Walking UP Column 1 to Row 21...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 21: {coords}")

# Step 3: Walk RIGHT along Row 21 to Column 22
print("3. Walking RIGHT to Column 22...")
for _ in range(21):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 22: {coords}")

# Step 4: Walk UP Column 22 to Row 14
print("4. Walking UP Column 22 to Row 14...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 14: {coords}")

# Step 5: Walk RIGHT along Row 14 to Column 26
print("5. Walking RIGHT along Row 14 to Column 26...")
for _ in range(4):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 26: {coords}")

# Step 6: Use CUT on the bush at (26, 13)
# We are currently at (26, 14) facing RIGHT or UP? Let's turn UP first to face the bush at (26, 13)
print("6. Turning UP to face the bush at (26, 13)...")
bridge.press_buttons(["Up"])
time.sleep(0.6)

print("Opening menu to use CUT...")
bridge.press_buttons(["Start", "sleep 500"])
bridge.press_buttons(["Down", "sleep 200", "A", "sleep 500"]) # Select POKEMON
bridge.press_buttons(["Down", "sleep 200", "A", "sleep 500"]) # Select TRUFFLE (Paras)
bridge.press_buttons(["Down", "sleep 200", "A", "sleep 1500"]) # Select CUT move and wait for text
bridge.press_buttons(["B", "sleep 1000"]) # Dismiss dialogue

coords = bridge.get_coordinates()
print(f"Coords after CUT (should be 26, 14): {coords}")

# Step 7: Walk UP column 26 to Row 9 (5 steps UP)
print("7. Walking UP Column 26 to Row 9...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 9: {coords}")

# Step 8: Walk LEFT along Row 9 to Column 19
print("8. Walking LEFT along Row 9 to Column 19...")
for _ in range(7):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 19: {coords}")

# Step 9: Walk UP Column 19 to Row 8
print("9. Walking UP Column 19 to Row 8...")
bridge.press_buttons(["Up"])
time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 8: {coords}")

# Step 10: Walk RIGHT along Row 8/9 to Column 37
print("10. Walking RIGHT along Row 8/9 to Column 37...")
for _ in range(18):
    bridge.press_buttons(["Right"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 37: {coords}")

# Step 11: Walk UP Column 37 to Row 2
print("11. Walking UP Column 37 to Row 2...")
for _ in range(6):
    bridge.press_buttons(["Up"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 2: {coords}")

# Step 12: Walk LEFT along Row 2 to Column 22
print("12. Walking LEFT along Row 2 to Column 22...")
for _ in range(15):
    bridge.press_buttons(["Left"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Column 22: {coords}")

# Step 13: Walk DOWN Column 22 to Row 4
print("13. Walking DOWN Column 22 to Row 4...")
for _ in range(2):
    bridge.press_buttons(["Down"])
    time.sleep(0.6)
coords = bridge.get_coordinates()
print(f"Coords at Row 4: {coords}")

# Step 14: Walk UP to enter Gatehouse
print("14. Entering Gatehouse...")
bridge.press_buttons(["Up"])
time.sleep(2.0)
coords = bridge.get_coordinates()
print(f"Coords inside Gatehouse: {coords}")

