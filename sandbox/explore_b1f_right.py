import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Current pos: {pos}")

# We are at (24, 15). Let's explore Columns 25, 26, 27, 28 to see if we can go Down from any of them.
# Move Right to Column 25
pos = move(['Right'])

# Try to go Right and then Down for each column
for col in range(25, 29):
    print(f"At {pos}, checking if we can go Down...")
    next_pos = move(['Down'])
    if next_pos['y'] > 15:
        print(f"SUCCESS! Walked Down at Column {col} to {next_pos}!")
        # Go back Up to resume testing other columns
        pos = move(['Up'])
    else:
        print(f"Blocked going Down at Column {col}")
    
    # Move Right to next column if we are not at Column 28
    if col < 28:
        pos = move(['Right'])

# Move back to (24, 15) to be safe
pos = mgba.get_coordinates()
if pos['x'] > 24:
    for _ in range(pos['x'] - 24):
        pos = move(['Left'])

mgba.take_screenshot()
