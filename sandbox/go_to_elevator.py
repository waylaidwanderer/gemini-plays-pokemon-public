import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting position: {pos}")

# We are on B3F at (25, 10)
# Step 1: Walk Right to (26, 10)
pos = move(["Right"])

# Step 2: Walk Up to (26, 7) (3 steps Up)
for _ in range(3):
    pos = move(["Up"])

# Step 3: Walk Left to (25, 7) (1 step Left)
pos = move(["Left"])

# Step 4: Walk Up 1 step to (25, 6) stairs
print("Stepping onto B2F stairs...")
pos = move(["Up"])

# Wait a moment for map transition
time.sleep(1)
pos = mgba.get_coordinates()
print(f"Position after B2F transition: {pos}")

# Step 5: Walk from B2F (21, 8) to the Elevator
if pos['x'] == 21 and pos['y'] == 8:
    # Walk Right to Column 25 (4 steps Right)
    print("Walking right to Column 25 on B2F...")
    for _ in range(4):
        pos = move(["Right"])
    
    # Walk Down to Row 14 (6 steps Down)
    print("Walking down to Row 14 on B2F...")
    for _ in range(6):
        pos = move(["Down"])
    
    # Walk Up to (25, 13) to warp into the elevator (1 step Up)
    print("Stepping into B2F Elevator at (25, 13)...")
    pos = move(["Up"])
    
    # Wait for elevator transition
    time.sleep(1)
    pos = mgba.get_coordinates()
    print(f"Final position inside Elevator: {pos}")
    mgba.take_screenshot()
else:
    print("Failed to reach B2F (21, 8) as expected. Take screenshot.")
    mgba.take_screenshot()
