import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

print(f"Starting escape from B1F (State A) at: {get_pos()}")

# Walk Left to Column 5 Row 11
step("Left")
step("Left")
step("Left")

# Step UP onto stairs at (5, 10) to warp
print("Stepping UP onto stairs...")
mgba.press_buttons(["Up"])
time.sleep(2.0)

print(f"Warp complete! Current position: {get_pos()}")
mgba.take_screenshot()
