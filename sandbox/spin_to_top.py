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

print(f"Starting spin-to-top sequence from: {get_pos()}")

# Walk to (5, 9)
step("Left")
step("Up")
step("Up")
step("Left")

# Step Left onto the UP spinner at (4, 9)
print("Stepping Left onto the UP spinner tile at (4, 9) to spin to the top!")
mgba.press_buttons(["Left"])
time.sleep(4.0)

print(f"Spin complete! Current position: {get_pos()}")
mgba.take_screenshot()
