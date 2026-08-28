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

# 1. Walk from (4, 10) to (2, 12)
step("Left")
step("Down")
step("Down")
step("Left")

# 2. Turn UP to face the statue at (2, 11)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Verify position and orientation
print("Position before interaction:", get_pos())
mgba.take_screenshot()

# 3. Press A to interact
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

# 4. Press A to see Yes/No prompt
print("Pressing A (dialogue 2)...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

# 5. Press A to select YES
print("Pressing A (dialogue 3)...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

# 6. Press A to clear "Click!"
print("Pressing A (dialogue 4)...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

print("Interactions complete! Final position:", get_pos())
