import mgba
import time

print("--- EXECUTING PERFECT GOLD TEETH RETRIEVAL ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (19, 23) facing UP.
# 1. Walk LEFT to Column 15.
print("Step 1: Walking LEFT to Column 15")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 15:
        print("Arrived at Column 15!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 15!")

# 2. Walk DOWN to Row 26.
print("Step 2: Walking DOWN Column 15 to Row 26")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 26:
        print("Arrived at Row 26!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 26!")

# 3. Walk RIGHT to Column 19.
print("Step 3: Walking RIGHT to Column 19")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 19:
        print("Arrived at Column 19!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 19!")

# 4. Face UP and press A to retrieve Gold Teeth
print("Step 4: Retrieving Gold Teeth")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Clear any text boxes
mgba.press_buttons(["A"])
time.sleep(0.6)

# 5. Use DIG to warp back to Fuchsia City Pokémon Center!
print("Step 5: Using DIG to warp out...")
mgba.press_buttons(["Start"])
time.sleep(0.6)

# Force cursor to POKEDEX (top)
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)

# Press Down once to POKEMON, and A
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(1.0)

# Press Down once to highlight TRUFFLE, and A
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(1.0)

# Select DIG (Option 1 in submenu)
mgba.press_buttons(["A"])
time.sleep(3.0) # wait for DIG warp animation

mgba.take_screenshot()
print("Final Position after DIG:", get_pos())
