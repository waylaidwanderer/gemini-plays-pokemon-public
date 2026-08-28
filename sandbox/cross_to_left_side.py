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

print(f"Starting crossing to the left side of Viridian Gym from: {get_pos()}")

# Walk Left to (6, 11)
step("Left")
step("Left")

# Step Down onto the LEFT spinner at (6, 12) to spin to (5, 12)
print("Stepping Down onto the LEFT spinner at (6, 12)...")
mgba.press_buttons(["Down"])
time.sleep(2.5) # Wait for spin animation
print(f"Spin complete! Current position: {get_pos()}")

# Walk down Column 5 to Row 13
step("Down")

# Walk Left along Row 13 to Column 1
step("Left")
step("Left")
step("Left")
step("Left")

print(f"Reached left side! Final position: {get_pos()}")
mgba.take_screenshot()
