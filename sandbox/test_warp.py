import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! From {pos_before} to {pos_after}")
        return "WARPED"
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    return "BLOCKED"

print("Testing warps from (5, 10) on 3F West...")
print("Current position:", mgba.get_coordinates())

# Try UP
print("Trying UP...")
res = step_strict("Up", 5, 9)
print(f"Result: {res}. Position: {mgba.get_coordinates()}")

# Try DOWN (which is step to 5, 11)
print("Trying DOWN...")
res = step_strict("Down", 5, 11)
print(f"Result: {res}. Position: {mgba.get_coordinates()}")

# Walk back to (5, 10) if we are at (5, 11)
if mgba.get_coordinates() == {'x': 5, 'y': 11}:
    step_strict("Up", 5, 10)

# Try LEFT
print("Trying LEFT...")
res = step_strict("Left", 4, 10)
print(f"Result: {res}. Position: {mgba.get_coordinates()}")

# Walk back to (5, 10) if we are at (4, 10)
if mgba.get_coordinates() == {'x': 4, 'y': 10}:
    step_strict("Right", 5, 10)

# Try RIGHT
print("Trying RIGHT...")
res = step_strict("Right", 6, 10)
print(f"Result: {res}. Position: {mgba.get_coordinates()}")

