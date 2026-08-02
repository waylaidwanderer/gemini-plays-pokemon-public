import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

# We are at B3F (25, 7)
pos = mgba.get_coordinates()
print("Starting at:", pos)

if pos['x'] == 25 and pos['y'] == 7:
    print("Warping to B2F...")
    pos = move(["Up"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Coordinates after warp:", pos)

# Now we should be on B2F. Let's make sure we are around (21, 8) or (21, 9)
if pos['x'] == 21:
    print("Successfully on B2F!")
    # Step to (21, 13)
    steps_down = 13 - pos['y']
    print(f"Walking Down {steps_down} steps...")
    for _ in range(steps_down):
        pos = move(["Down"])
    
    # Walk Right 3 steps to (24, 13)
    print("Walking Right to Column 24...")
    for _ in range(3):
        pos = move(["Right"])
    
    # Step Up 1 step to warp at (24, 12) or walk into (24, 13)?
    # Wait, the warp is at (24, 13) or (24, 12)?
    # The disassembly says:
    # warp 24, 13, 0, ROCKET_HIDEOUT_ELEVATOR
    # Since the warp is at (24, 13), walking onto (24, 13) should warp us!
    # Let's see if we are already warped.
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Coordinates after elevator warp attempt:", pos)

# Let's see if we are inside the elevator
# The elevator map coordinates are (1, 4) or (2, 4) or (3, 4).
# Let's check if our x is small (like 1, 2, 3) and y is 4 or 5.
if pos['x'] in [1, 2, 3] and pos['y'] in [4, 5]:
    print("Successfully inside the elevator!")
    # Let's move to the control panel at (2, 1)
    # We are at (1, 4) or (2, 4).
    # Walk to (2, 4) first if we are at (1, 4)
    if pos['x'] == 1:
        pos = move(["Right"])
    elif pos['x'] == 3:
        pos = move(["Left"])
        
    # Walk Up to (2, 2)
    print("Walking Up to the control panel...")
    pos = move(["Up"])
    pos = move(["Up"])
    
    # Look Up at (2, 1) by pressing Up once more or just pressing A
    print("Looking at control panel...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    
    # Interact with control panel
    print("Interacting with control panel...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.take_screenshot()

print("Script finished. Current position:", mgba.get_coordinates())
