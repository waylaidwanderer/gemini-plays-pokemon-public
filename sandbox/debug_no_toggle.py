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

# We are at (2, 12) showing "A secret switch!".
# Let's advance using B instead of A to see if we can close it without toggling.
print("Pressing B to advance 'A secret switch!' to 'Press it? YES/NO'...")
mgba.press_buttons(["B"])
time.sleep(1.2)

# Now we should be at "Press it? YES/NO". Let's press B to select NO and close.
print("Pressing B to select NO and close dialogue...")
mgba.press_buttons(["B"])
time.sleep(1.2)

# Now we should be in the overworld. Let's test walking to Column 1 and UP.
print("Stepping Left...")
step("Left") # to (1, 12)
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - gate!
step("Up") # to (1, 8)

print("Final Position:", get_pos())
mgba.take_screenshot()
