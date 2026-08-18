import mgba
import time

# We are surfing at (7, 16) in Pallet Town.
# Let's swim south along Route 21. Route 21 is about 90 rows tall.
# We will swim Down up to 95 steps.
# If we get blocked (e.g. wild battle), coordinates won't change. We will run from battle.

def run_from_battle():
    print("Coordinates didn't change. Attempting to escape battle...")
    # Press B to dismiss any dialogue or Fight menu
    mgba.press_buttons(["B", "sleep 300"])
    # Move to RUN and select (from main menu, Down then Right selects RUN)
    mgba.press_buttons(["Down", "Right", "A", "sleep 1200"])
    # Press B to clear "Got away safely!" or other battle text
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
