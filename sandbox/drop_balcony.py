import mgba
import time

def step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    print(f"Pressed {direction}: {pos_before} -> {pos_after}")
    return pos_after

pos = mgba.get_coordinates()
print(f"Starting at {pos}")

# 1. Right to (20, 16)
pos = step("Right")

# 2. Down to (20, 17)
pos = step("Down")

# 3. Down to (20, 18)
pos = step("Down")

# 4. Left to (19, 18) (drop!)
pos = step("Left")
time.sleep(1.0)
print(f"End position: {mgba.get_coordinates()}")
