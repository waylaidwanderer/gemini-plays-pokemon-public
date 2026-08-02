import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (24, 11)
# Step 1: Walk Right to (25, 11)
pos = move(["Right"])

# Step 2: Walk Down to (25, 14)
for i in range(11, 14):
    pos = move(["Down"])

# Step 3: Try walking Up from (25, 14) into (25, 13)
print("Testing Up into (25, 13):")
pos = move(["Up"])
if pos['y'] == 13:
    print("Warped or walked into (25, 13)!")
else:
    print(f"Blocked at {pos}")
    # Step 4: Try Left to (24, 14) and Up into (24, 13)
    # First, step back down to (25, 14) if needed (though we should already be at (25, 14))
    pos = mgba.get_coordinates()
    pos = move(["Left"])
    print("Testing Up into (24, 13):")
    pos = move(["Up"])
    if pos['y'] == 13:
        print("Warped or walked into (24, 13)!")
    else:
        print(f"Blocked at {pos}")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
