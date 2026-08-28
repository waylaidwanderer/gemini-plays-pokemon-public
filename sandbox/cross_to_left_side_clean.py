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

print(f"Executing clean crossing from: {get_pos()}")

# Walk (6, 11) -> (6, 10) -> (5, 10) -> (4, 10) -> (4, 11) -> (4, 12) -> (4, 13) -> (1, 13)
step("Up")
step("Left")
step("Left")
step("Down")
step("Down")
step("Down")
step("Left")
step("Left")
step("Left")

print(f"Reached left side! Current position: {get_pos()}")
mgba.take_screenshot()
