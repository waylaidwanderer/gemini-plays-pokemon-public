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

print(f"Walking from current B1F position {get_pos()} to B1F East stairs at (22, 2)...")

# 1. Walk up Column 12 from Row 11 to Row 7: (12, 11) -> (12, 7)
step("Up")
step("Up")
step("Up")
step("Up")

# 2. Walk Right along Row 7 from Column 12 to Column 22: (22, 7)
for _ in range(10):
    step("Right")

# 3. Walk Up Column 22 to the stairs at (22, 2)
step("Up")
step("Up")
step("Up")
step("Up")
step("Up")

# Step Up onto the stairs to warp UP to 1F East
print("Stepping UP onto B1F East stairs...")
mgba.press_buttons(["Up"])
time.sleep(2.5)

print(f"Warp complete! Current position on 1F East: {get_pos()}")
mgba.take_screenshot()
