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

print(f"Starting warp attempt via (7, 10) from: {get_pos()}")

# Walk Right to (7, 11)
step("Right")
step("Right")

# Step UP onto stairs at (7, 10)
print("Stepping UP onto the stairs at (7, 10)...")
mgba.press_buttons(["Up"])
time.sleep(2.5)

print(f"Warp check complete! Current position: {get_pos()}")
mgba.take_screenshot()
