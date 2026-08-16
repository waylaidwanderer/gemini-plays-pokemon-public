import bridge
import time

# ==========================================================
# PHASE 0: Fuchsia City - CUT Bush and Walk to (26, 9)
# ==========================================================
print("Opening Start menu...")
bridge.press_buttons(["Start"])
time.sleep(1.0)

print("Resetting Start menu cursor to POKEDEX...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting POKEMON...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.0)

print("Resetting POKEMON cursor to first Pokémon...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting TRUFFLE...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.0)

# The cursor defaults to DIG (Option 1). We press Down once to go to CUT (Option 2).
print("Moving cursor to CUT...")
bridge.press_buttons(["Down"])
time.sleep(1.0) # Generous sleep to ensure the cursor moves!

print("Selecting CUT...")
bridge.press_buttons(["A"])
time.sleep(3.0) # Wait for animation and text

print("Clearing dialogue...")
bridge.press_buttons(["A"])
time.sleep(1.5) # Wait for overworld transition

# Walk UP 5 steps to (26, 9)
print("Walking UP to (26, 9)...")
for i in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.5)

print("Position after walk:", bridge.get_coordinates())
