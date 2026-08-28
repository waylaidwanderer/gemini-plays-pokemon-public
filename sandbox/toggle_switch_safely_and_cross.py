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

# 1. Walk from (1, 10) to (2, 12)
step("Down")
step("Down")
step("Right")

# 2. Turn UP to face switch at (2, 11)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# 3. Press A exactly 4 times with 1.0s delay (no 5th A press, to avoid reopening dialogue!)
print("Toggling Mewtwo switch...")
for i in range(4):
    print(f"Pressing A {i+1}/4...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggled!")

# 4. Step Left to (1, 12)
step("Left")

# 5. Walk UP Column 1 to Row 6
print("Walking UP Column 1...")
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) (Should be open now!)
step("Up") # to (1, 8)
step("Up") # to (1, 7)
step("Up") # to (1, 6)

print("Final position:", get_pos())
mgba.take_screenshot()
