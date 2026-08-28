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
step("Down")
step("Down")
step("Right")

# 2. Stand at (2, 12) and toggle the switch
print("At (2, 12). Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.8)

print("Toggling switch with exactly 5 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(9.0)
print("Synchronized switch toggle completed.")

# 3. Walk to (1, 12)
step("Left")

# 4. Walk UP Column 1 to Row 6 (which should be OPEN in State B!)
print("Testing walking UP past Row 9 Column 1 gate...")
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - This is the gate!
step("Up") # to (1, 8)
step("Up") # to (1, 7)
step("Up") # to (1, 6)

print("Final Position:", get_pos())
mgba.take_screenshot()
