import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

# Test walking Right from (21, 2) onto (22, 2)
print("Testing step Right onto (22, 2) from (21, 2)...")
new_pos = step("Right")
mgba.take_screenshot()

# If we didn't warp and successfully moved to (22, 2):
if new_pos == (22, 2):
    print("SUCCESS: Walked onto (22, 2)! Let's try to step Right to (23, 2)...")
    new_pos2 = step("Right")
    mgba.take_screenshot()
    if new_pos2 == (23, 2):
         print("SUCCESS: Walked onto (23, 2)!")
    else:
         print("BLOCKED going Right to (23, 2)")
         step("Left") # Go back to (21, 2)
else:
    print("Blocked or warped!")
