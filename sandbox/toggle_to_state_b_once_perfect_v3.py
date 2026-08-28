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

# Since we are currently at (2, 12) showing "A secret switch!"
# We must perform exactly 3 slow A-presses to toggle to State B and close dialogue.
print("Toggling switch to State B with exactly 3 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(5.0)
print("Switch toggle complete!")

# Walk to Column 1 and UP past gate
step("Left") # to (1, 12)
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - gate should be open now!
step("Up") # to (1, 8)

print("Final Position:", get_pos())
mgba.take_screenshot()
