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

print(f"Starting escape from B1F at: {get_pos()}")

# Walk to stairs at (5, 10)
step("Right")
step("Right")
step("Right")
step("Up")
step("Up")

# Step onto stairs to warp
print("Stepping onto stairs...")
step("Up")
time.sleep(1.5)
print(f"Warped! Current position: {get_pos()}")
mgba.take_screenshot()
