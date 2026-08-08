import mgba
import time

def move_and_log(buttons, description):
    print(f"Executing: {description}")
    mgba.press_buttons(buttons)
    # Give some sleep time if needed, but press_buttons is blocking or executes immediately
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    # Capture screenshot
    scr = mgba.take_screenshot()
    print(f"Screenshot captured: {scr}")
    return pos

print("Starting route test from (15, 25)")
# Step 1: Walk Down 1 step to (15, 26)
pos = move_and_log(["Down"], "Step Down to (15, 26)")

# Step 2: Walk Left 2 steps to (13, 26)
pos = move_and_log(["Left", "Left"], "Step Left to (13, 26)")

# Step 3: Try to walk Up 1 step to (13, 25)
pos = move_and_log(["Up"], "Step Up to (13, 25)")

# Let's do another Up to see if we can continue or if we are blocked
pos = move_and_log(["Up"], "Step Up to (13, 24)")
