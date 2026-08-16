import mgba
import time

print("--- WALK EAST GAP AND RETRIEVE GOLD TEETH ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (19, 23) facing LEFT.
# 1. Walk to (21, 23): Right 3 times (1 turn + 2 steps).
print("Step 1: Walking to (21, 23)")
mgba.press_buttons(["Right"])
time.sleep(0.4)
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
print("Position after Step 1:", get_pos())

# 2. Walk Down to (21, 26): Down 4 times (1 turn + 3 steps).
print("Step 2: Walking Down Column 21 to Row 26")
mgba.press_buttons(["Down"])
time.sleep(0.4)
for _ in range(3):
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
print("Position after Step 2:", get_pos())

# 3. Walk Left to (19, 26): Left 3 times (1 turn + 2 steps).
print("Step 3: Walking Left along Row 26 to Column 19")
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(2):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after Step 3:", get_pos())

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

# Select TRUFFLE (first slot, cursor is already on him!)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Select DIG (Option 1 in submenu)
mgba.press_buttons(["A"])
time.sleep(3.0) # wait for DIG warp animation

mgba.take_screenshot()
print("Final Position after DIG:", get_pos())
