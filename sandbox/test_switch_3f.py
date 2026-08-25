import mgba
import time

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Starting at (1, 12) on 3F West
# 1. Walk to (2, 13)
walk_step("Down", {"x": 1, "y": 13})
walk_step("Right", {"x": 2, "y": 13})

# 2. Try interacting with (2, 12) from (2, 13)
print("Standing at (2, 13). Facing UP and pressing A to test if switch can be toggled from here...")
mgba.press_buttons(["Up"])
time.sleep(0.3)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Check if text box opened (player coordinate shouldn't change, but we can try to press A/B)
# Let's take a screenshot to see if a dialog is open!
img_path = mgba.take_screenshot()
print(f"Screenshot taken: {img_path}")

# If we didn't toggle, try walking UP to (2, 12)
pos = mgba.get_coordinates()
if pos == {"x": 2, "y": 13}:
    print("Testing if we can walk UP to (2, 12)...")
    if walk_step("Up", {"x": 2, "y": 12}):
        print("Walked UP to (2, 12)! Toggling switch facing UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])   # Select YES
        time.sleep(1.0)
        mgba.press_buttons(["B"])   # Dismiss dialog
        time.sleep(0.5)
        print("Switch toggled from (2, 12)!")
    else:
        # If we couldn't walk up, maybe the previous A press actually toggled the switch?
        # Let's assume it did and walk left to check the gate at (1, 9)!
        print("Could not walk UP to (2, 12). Let's see if the previous A press toggled the switch...")
        # Press A again on YES in case the menu was open, and B to dismiss
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["B"])
        time.sleep(0.5)

# Walk back to (1, 13)
mgba.get_coordinates()
