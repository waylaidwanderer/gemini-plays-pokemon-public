import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = get_pos()
    print(f"Stepped {direction}: {old_pos} -> {new_pos}")
    return new_pos

print("Start position:", get_pos())

# 1. Walk from (3, 10) to (2, 12)
step("Down")
step("Down")
step("Left")

# 2. Turn UP
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.6)

# 3. Toggle switch with 6 slow A-presses
print("Toggling Mewtwo switch...")
for i in range(6):
    print(f"Pressing A {i+1}/6...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)

# 4. Walk to (3, 12)
step("Right")

# 5. Try to walk UP Column 3 to Row 6 (which should be OPEN in State B!)
print("Testing walking UP past Row 9 gate...")
p1 = step("Up") # to (3, 11)
p2 = step("Up") # to (3, 10)
p3 = step("Up") # to (3, 9) - This is the gate!
p4 = step("Up") # to (3, 8)
p5 = step("Up") # to (3, 7)
p6 = step("Up") # to (3, 6)

print("Final Position:", get_pos())
mgba.take_screenshot()
