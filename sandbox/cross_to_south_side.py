import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    return pos

print("Starting reverse Route 4 alignment bypass script...")

# 1. We are at x=19, y=13. Let's walk Left towards x=0.
current_x = 19
current_y = 13
blocked = False

print("Walking Left along row 13...")
for i in range(19):
    pos = walk_step("Left")
    # Note: get_coordinates() might return {'x': 0, 'y': 0}, so we should check if it's non-zero
    if pos['x'] != 0 or pos['y'] != 0:
        print(f"Step {i+1}: Arrived at {pos}")
        current_x = pos['x']
        current_y = pos['y']
    else:
        # If get_coordinates returns 0, we can decrement current_x manually as a fallback
        current_x -= 1
        print(f"Step {i+1} (Fallback): x={current_x}, y={current_y}")

# 2. Walk Up 1 step to y=12
print("Walking Up to row 12...")
pos = walk_step("Up")
if pos['x'] != 0 or pos['y'] != 0:
    print(f"After Up: {pos}")
    current_x = pos['x']
    current_y = pos['y']
else:
    current_y = 12
    print(f"After Up (Fallback): x={current_x}, y={current_y}")

# 3. Walk Left to transition to Route 4
print("Transitioning to Route 4...")
pos = walk_step("Left")
time.sleep(1.0) # Wait for map load
pos = mgba.get_coordinates()
print(f"Coordinates after transition to Route 4: {pos}")

# 4. Now on Route 4, we want to go from y=4 to y=8. Let's walk Down 4 steps.
print("Walking Down 4 steps on Route 4...")
for i in range(4):
    pos = walk_step("Down")
    print(f"Route 4 Down Step {i+1}: {pos}")

# 5. Walk Right to transition back to Cerulean City (South side)
print("Transitioning back to Cerulean City (South side)...")
pos = walk_step("Right")
time.sleep(1.0) # Wait for map load
pos = mgba.get_coordinates()
print(f"Final coordinates in Cerulean City (South side): {pos}")
