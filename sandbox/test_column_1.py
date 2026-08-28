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

# 1. Walk from (4, 10) to (1, 11) via (1, 12)
step("Left")
step("Down")
step("Down")
step("Left") # to (2, 12)
step("Left") # to (1, 12)
step("Up")   # to (1, 11)

# 2. Try to walk UP Column 1
print("Testing walking UP Column 1...")
p1 = step("Up")   # to (1, 10)
p2 = step("Up")   # to (1, 9)
p3 = step("Up")   # to (1, 8)
p4 = step("Up")   # to (1, 7)
p5 = step("Up")   # to (1, 6)

time.sleep(1.0)
print("Final position:", get_pos())
mgba.take_screenshot()
