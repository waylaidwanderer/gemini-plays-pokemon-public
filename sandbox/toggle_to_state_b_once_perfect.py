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

print("Start position:", get_pos())

# 1. Walk from current position (1, 10) to (2, 12)
pos = get_pos()
if pos == (1, 10):
    step("Down")
    step("Down")
    step("Right")
elif pos == (2, 12):
    print("Already at switch position!")

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.8)

# 2. Perfect Switch Toggle Sequence: A (inspect), A (select YES), B (dismiss text)
print("Sending perfect toggle sequence (A -> sleep -> A -> sleep -> B)...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "B", "sleep 1000"
])
time.sleep(4.5)
print("Sequence completed.")

# 3. Walk to (1, 12)
step("Left")

# 4. Walk UP Column 1 to Row 6 (should be OPEN in State B!)
print("Testing walking UP Column 1...")
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - The gate!
step("Up") # to (1, 8)
step("Up") # to (1, 7)
step("Up") # to (1, 6)

print("Final Position:", get_pos())
mgba.take_screenshot()
