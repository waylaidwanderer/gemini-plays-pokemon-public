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

if pos['x'] == 23 and pos['y'] == 9:
    # Walk Down to (23, 11)
    pos = move(['Down'])
    pos = move(['Down'])
    
    # Walk Right to (25, 11)
    pos = move(['Right'])
    pos = move(['Right'])
    
    # Walk Up to (25, 7)
    for _ in range(4):
        pos = move(['Up'])
        
    # Walk Left to (23, 7)
    pos = move(['Left'])
    pos = move(['Left'])
    
    # Walk Up to (23, 3)
    for _ in range(4):
        pos = move(['Up'])

# Now we are at (23, 3). Let's explore Row 3 and Row 2!
print("Reached top area. Current position:", mgba.get_coordinates())

# Let's explore Left on Row 3
for col in range(22, 18, -1):
    pos = move(['Left'])
    print(f"At Row 3 Column {col}: {pos}")
    # Try to walk Up to Row 2
    print("Testing if Up is walkable...")
    test_pos = move(['Up'])
    if test_pos['y'] < 3:
        print(f"SUCCESS! Walked UP to Row 2: {test_pos}")
        # Return to Row 3
        pos = move(['Down'])
    else:
        print("Blocked going UP")

# Walk back Right to (23, 3)
pos = mgba.get_coordinates()
if pos['x'] < 23:
    for _ in range(23 - pos['x']):
        pos = move(['Right'])

# Let's explore Right on Row 3
for col in range(24, 29):
    pos = move(['Right'])
    print(f"At Row 3 Column {col}: {pos}")
    # Try to walk Up to Row 2
    print("Testing if Up is walkable...")
    test_pos = move(['Up'])
    if test_pos['y'] < 3:
        print(f"SUCCESS! Walked UP to Row 2: {test_pos}")
        # Return to Row 3
        pos = move(['Down'])
    else:
        print("Blocked going UP")

mgba.take_screenshot()
