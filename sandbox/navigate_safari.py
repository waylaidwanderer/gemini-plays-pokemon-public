import mgba
import time

print("--- EXECUTING OPTIMIZED GOLD TEETH RETRIEVAL ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (19, 23) facing UP.
# 1. Walk UP Column 19 to Row 19: (19, 19)
print("Step 1: Walking UP Column 19 to Row 19")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 19:
        print("Arrived at Row 19!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 19!")

# 2. Walk LEFT along Row 19 to Column 15: (15, 19)
print("Step 2: Walking LEFT along Row 19 to Column 15")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 15:
        print("Arrived at Column 15!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 15!")

# 3. Walk DOWN Column 15 to Row 26: (15, 26)
print("Step 3: Walking DOWN Column 15 to Row 26")
for _ in range(15):
    pos = get_pos()
    if pos and pos['y'] == 26:
        print("Arrived at Row 26!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 26!")

# 4. Walk RIGHT along Row 26 to Column 19: (19, 26) (directly below the teeth!)
print("Step 4: Walking RIGHT along Row 26 to Column 19")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 19:
        print("Arrived at Column 19!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 19!")

# 5. Face UP and press A to retrieve Gold Teeth
print("Step 5: Retrieving Gold Teeth")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Clear any text boxes
mgba.press_buttons(["A"])
time.sleep(0.6)

# 6. Use DIG to warp back to Fuchsia City Pokémon Center!
print("Step 6: Using DIG to warp out...")
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
