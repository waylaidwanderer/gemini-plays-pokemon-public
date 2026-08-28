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

# We are at (2, 12) facing UP.
print("Toggling switch to State B with exactly 4 A-presses...")
mgba.press_buttons([
    "A", "sleep 1200",
    "A", "sleep 1200",
    "A", "sleep 1200",
    "A", "sleep 1200"
])
time.sleep(6.5)
print("Switch toggle complete!")

# Walk to Column 1 and walk UP Column 1 past the open gate to Row 6!
step("Left")
step("Up")
step("Up")
step("Up") # (1, 9) - Should be OPEN in State B!
step("Up")
step("Up")
step("Up")

print("Final Position:", get_pos())
mgba.take_screenshot()
