import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (23, 13) on B1F
# 1. Walk Up Column 23 as far as possible (up to Row 5)
for i in range(13, 5, -1):
    pos = move(["Up"])
    if pos['y'] != i - 1:
        print(f"Blocked at {pos} during Up movement along Column 23")
        break

# 2. If we successfully reached Row 5, continue to the western corridor!
if pos['y'] == 5:
    # Walk Left to Column 11 (12 steps Left from 23)
    for _ in range(12):
        pos = move(["Left"])
    
    # Walk Down Column 11 to Row 10 (5 steps Down)
    for _ in range(5):
        pos = move(["Down"])
    
    # Walk Right to Column 14 (3 steps Right)
    for _ in range(3):
        pos = move(["Right"])
    
    # Walk Down Column 14 to Row 14 (4 steps Down)
    for _ in range(4):
        pos = move(["Down"])
    
    # Try walking Down to see if we can reach the bottom area of B1F
    print("Testing walking Down from (14, 14) in the west...")
    for i in range(14, 26):
        pos = move(["Down"])
        if pos['y'] != i + 1:
            print(f"Blocked at {pos} during Down movement in the west")
            break

print("Final position after exploration:", mgba.get_coordinates())
mgba.take_screenshot()
