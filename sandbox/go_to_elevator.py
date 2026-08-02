import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at B3F (19, 12)
# Step 1: Walk Up to Row 7 (5 steps Up)
print("Walking up Column 19...")
for _ in range(5):
    pos = move(["Up"])

# Step 2: Walk Right to Column 25 (6 steps Right)
print("Walking right to Column 25...")
for _ in range(6):
    pos = move(["Right"])

# Step 3: Walk Up 1 step to (25, 6) stairs to B2F
print("Stepping onto B2F stairs...")
pos = move(["Up"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Position on B2F: {pos}")

# Step 4: On B2F, walk Down to Row 14 (6 steps Down)
if pos['x'] == 21 and pos['y'] == 8:
    print("Walking down Column 21 on B2F...")
    for _ in range(6):
        pos = move(["Down"])
    
    # Step 5: Walk Right to Column 24 (3 steps Right)
    print("Walking right to Column 24 through the gap...")
    for _ in range(3):
        pos = move(["Right"])
    
    # Step 6: Walk Up 1 step into the LEFT elevator door at (24, 13)
    print("Stepping into LEFT elevator door at (24, 13)...")
    pos = move(["Up"])
    time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final position inside Elevator: {pos}")
mgba.take_screenshot()
