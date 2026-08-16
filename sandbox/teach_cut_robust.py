import mgba
import time

print("Ensuring we face UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(1.0)

print("Resetting Start menu cursor to POKEDEX...")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting POKEMON...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.0)

print("Resetting POKEMON cursor to first Pokémon...")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting TRUFFLE...")
mgba.press_buttons(["Down", "A"])
time.sleep(1.0)

# Since TRUFFLE has DIG and CUT:
# Submenu has DIG first, then CUT second.
# The cursor defaults to DIG (the 1st option).
# We press Down once to highlight CUT, and A to use it!
print("Selecting CUT...")
mgba.press_buttons(["Down", "A"])
time.sleep(2.0) # Wait for text/animation

# Now we are on the text box "TRUFFLE used CUT!".
# Let's press A to clear it!
print("Pressing A to clear 'used CUT' dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Press B twice to safely close any remaining menus
print("Closing menus...")
mgba.press_buttons(["B", "B"])
time.sleep(1.0)

# Walk UP 5 steps to (26, 9)
print("Walking UP to (26, 9)...")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.44)

print("Position after walk:", mgba.get_coordinates())
