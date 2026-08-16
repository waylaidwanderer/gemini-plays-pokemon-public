import mgba
import time

print("--- TESTING COLUMN 22 WALKABILITY ---")

def get_pos():
    return mgba.get_coordinates()

# Start at (19, 22) facing UP.
# Walk to Column 22 Row 22.
print("Walking to (22, 22)...")
mgba.press_buttons(["Right"])
time.sleep(0.4)
for _ in range(3):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
print("Position:", get_pos())

# Now walk DOWN Column 22 to Row 26 step-by-step
print("Walking DOWN Column 22...")
for step in range(5):
    pos = get_pos()
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    new_pos = get_pos()
    print(f"Step {step+1}: from {pos} to {new_pos}")
    if new_pos == pos:
        print(f"BLOCKED at {pos} going Down!")
        break

mgba.take_screenshot()
print("Final Position:", get_pos())
