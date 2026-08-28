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

# 1. Walk from current position to (2, 12)
pos = get_pos()
if pos == (3, 10):
    step("Down")
    step("Down")
    step("Left")
elif pos == (3, 11):
    step("Down")
    step("Left")
elif pos == (3, 12):
    step("Left")

print("At switch position. Starting synchronized 4 A-press switch toggle...")

# 2. Toggle the switch using EXACTLY 4 slow A-presses in a single synchronized call
mgba.press_buttons([
    "Up", "sleep 600",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
# Wait for the emulator to finish the entire sequence
time.sleep(7.0)
print("Synchronized switch toggle completed.")

# 3. Walk back to Column 3
step("Right")

# 4. Walk UP Column 3 past the Row 9 gate to Row 6!
print("Attempting to walk UP Column 3 to Row 6...")
step("Up") # to (3, 11)
step("Up") # to (3, 10)
step("Up") # to (3, 9) - Row 9 gate
step("Up") # to (3, 8)
step("Up") # to (3, 7)
step("Up") # to (3, 6)

print("Final Position:", get_pos())
mgba.take_screenshot()
