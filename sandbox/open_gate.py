import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (20, 8)
# Step 1: Walk Left to Column 19 (1 step Left)
pos = move(["Left"])

# Step 2: Walk Down to Row 14 (6 steps Down)
print("Walking down Column 19...")
for _ in range(6):
    pos = move(["Down"])

# Step 3: Walk Right to Column 25 (6 steps Right)
print("Walking right to Column 25 through the gap at (23, 14)...")
for _ in range(6):
    pos = move(["Right"])

# Step 4: Walk Up to Row 7 (7 steps Up)
print("Walking up Column 25...")
for _ in range(7):
    pos = move(["Up"])

# Step 5: Walk Up 1 step into the gate at (25, 6)
print("Attempting to walk into Row 6 to trigger the Lift Key gate...")
pos = move(["Up"])

# Wait for potential script/animation/textbox
time.sleep(2.0)
pos = mgba.get_coordinates()
print(f"Coordinates after attempting to open gate: {pos}")
mgba.take_screenshot()
