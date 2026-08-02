import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting position: {pos}")

# We are on B3F at (23, 18)
# Step 1: Walk UP Column 23 on B3F to Row 7 (11 steps Up)
print("Walking up Column 23...")
for _ in range(11):
    pos = move(["Up"])

# Step 2: Walk Right along Row 7 to Column 25 (2 steps Right)
print("Walking right to Column 25...")
for _ in range(2):
    pos = move(["Right"])

# Step 3: Walk Up 1 step into the B2F stairs at (25, 6)
print("Stepping onto B2F stairs...")
pos = move(["Up"])

# Wait a moment for emulator map transition
time.sleep(1)
pos = mgba.get_coordinates()
print(f"Position after B2F transition: {pos}")

if pos['x'] == 21 and pos['y'] == 8:
    # Step 4: Walk Right to Column 25 (4 steps Right)
    print("Walking right to Column 25 on B2F...")
    for _ in range(4):
        pos = move(["Right"])
    
    # Step 5: Walk Down to Row 14 (6 steps Down)
    print("Walking down to Row 14 on B2F...")
    for _ in range(6):
        pos = move(["Down"])
    
    # Step 6: Walk Up to (25, 13) to warp into the elevator (1 step Up)
    print("Stepping into B2F Elevator at (25, 13)...")
    pos = move(["Up"])
    
    # Let's wait and see where we are
    time.sleep(1)
    pos = mgba.get_coordinates()
    print(f"Final position inside Elevator: {pos}")
    mgba.take_screenshot()
else:
    print("Failed to reach B2F (21, 8) as expected. Screenshot taken.")
    mgba.take_screenshot()
