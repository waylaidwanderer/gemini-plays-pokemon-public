import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    new_pos = get_pos()
    print(f"Stepped {direction}: {old_pos} -> {new_pos}")
    return new_pos

print("Current position:", get_pos())

# Walk to (2, 12)
step("Down")
step("Down")
step("Right")

# Face UP
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# Press A once to open dialogue
print("Pressing A once...")
mgba.press_buttons(["A"])
time.sleep(1.2)

print("Final Position:", get_pos())
mgba.take_screenshot()
