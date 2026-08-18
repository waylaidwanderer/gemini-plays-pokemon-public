import mgba
import time

# We are at (11, 0) in Pallet Town
# Walk Left 3 steps to Column 8
mgba.press_buttons(["Left", "Left", "Left"])
print(f"Pacing start position: {mgba.get_coordinates()}")

# Walk Down 16 steps to Row 16
for i in range(16):
    mgba.press_buttons(["Down"])

pos_water = mgba.get_coordinates()
print(f"Position at water edge: {pos_water}")

# Open Start Menu, select POKéMON, select SHELLBY, select SURF
surf_actions = [
    "Start", "sleep 400",
    "Down", "sleep 150", "A", "sleep 500", # Open PKMN menu
    "A", "sleep 500", # Select SHELLBY (1st in list)
    "A", "sleep 500", # Select SURF (1st option when facing water)
    "A", "sleep 1000" # Dismiss "SHELLBY used SURF!" text and enter water
]
mgba.press_buttons(surf_actions)
print(f"Position after starting Surf: {mgba.get_coordinates()}")

# We are now in the water at (8, 16) in Pallet Town (or (8, 17)).
# Now swim south on Route 21. Route 21 is about 90 rows tall.
# We will swim Down up to 95 steps.
# If we get blocked (e.g. wild battle), coordinates won't change. We will run from battle.

def run_from_battle():
    print("Coordinates didn't change. Attempting to escape battle...")
    # Press B to dismiss any dialogue or Fight menu
    mgba.press_buttons(["B", "sleep 300"])
    # Move to RUN and select
    mgba.press_buttons(["Down", "Right", "A", "sleep 1200"])
    # Press B to clear "Got away safely!"
    mgba.press_buttons(["B", "sleep 300"])

consecutive_failures = 0
for i in range(95):
    prev_pos = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    curr_pos = mgba.get_coordinates()
    
    if curr_pos == prev_pos:
        consecutive_failures += 1
        print(f"Move failed at {prev_pos}. Failure count: {consecutive_failures}")
        if consecutive_failures >= 4:
            print("Stuck or blocked. Stopping.")
            break
        # Escape battle
        run_from_battle()
    else:
        consecutive_failures = 0
        if i % 10 == 0:
            print(f"Successfully swimming south. Current position: {curr_pos}")

print(f"Swim finished. Final position: {mgba.get_coordinates()}")
screenshot = mgba.take_screenshot()
print(f"Screenshot saved to: {screenshot}")
