import mgba
import time

print("--- USING DIG TO WARP TO PC ---")

# 1. Open the menu
mgba.press_buttons(["Start", "sleep 500"])

# 2. Go to POKEMON
# Move Up multiple times to ensure we are at the top (POKEDEX)
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
time.sleep(0.3)

# Move Down once to POKEMON and press A
mgba.press_buttons(["Down", "sleep 100", "A", "sleep 500"])

# 3. Select TRUFFLE (first slot)
mgba.press_buttons(["A", "sleep 500"])

# 4. Select DIG (Option 1)
mgba.press_buttons(["A", "sleep 3000"])

print("DIG executed. Current Position:", mgba.get_coordinates())
mgba.take_screenshot()
