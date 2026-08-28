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

print("Start position:", get_pos())

# Step Down to (10, 10)
for _ in range(4):
    step("Down")

# Step Left to (7, 10)
step("Left")
step("Left")
print("About to step Left onto stairs at (7, 10)...")
step("Left")

time.sleep(1.5)
print("Position after warping DOWN:", get_pos())
mgba.take_screenshot()
