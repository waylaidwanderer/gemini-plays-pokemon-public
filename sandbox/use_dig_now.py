import mgba
import time

print("Using DIG to escape...")
# 1. Open Menu
mgba.press_buttons(["Start", "sleep 400"])

# 2. Go Down to POKéMON and press A
mgba.press_buttons(["Down", "sleep 200", "A", "sleep 800"])

# 3. Go Down 4 times to select TRUFFLE (5th Pokémon in list) and press A
for _ in range(4):
    mgba.press_buttons(["Down", "sleep 200"])
mgba.press_buttons(["A", "sleep 800"])

# 4. Press A to select DIG (Option 1)
mgba.press_buttons(["A", "sleep 1500"])

print("DIG executed. Current position:", mgba.get_coordinates())
# Save screenshot to confirm landing
mgba.take_screenshot()
