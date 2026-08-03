import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

# Currently at B3F (28, 13) facing Up.
# Let's walk Down to (28, 15) to start Row 15 testing:
print("Moving to (28, 15)...")
move("Down", 2)

# We will test Column 28, 27, 26, 25, 24, 23
# For each column:
# 1. Try to walk Down 1 step.
# 2. If position changed, walk back Up 1 step and mark as WALKABLE.
# 3. Walk Left 1 step to the next column.

walkability = {}
for col in [28, 27, 26, 25, 24, 23]:
    pos = mgba.get_coordinates()
    print(f"Testing Column {col} at Row 15 (current: {pos}):")
    
    # Try moving Down
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down", "sleep 300"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_after != pos_before:
        # Walkable! Walk back Up
        print(f"  Column {col} Row 16 is WALKABLE (now at {pos_after})")
        walkability[col] = "WALKABLE"
        mgba.press_buttons(["Up", "sleep 300"])
        time.sleep(0.5)
    else:
        print(f"  Column {col} Row 16 is BLOCKED")
        walkability[col] = "BLOCKED"
        
    # Move Left to next column if not at 23
    if col > 23:
        mgba.press_buttons(["Left", "sleep 300"])
        time.sleep(0.5)

print("\nFinal B3F Row 16 Walkability:")
for col, state in walkability.items():
    print(f"  Column {col}: {state}")

screenshot = mgba.take_screenshot()
print("Screenshot:", screenshot)
