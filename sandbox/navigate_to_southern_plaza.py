import mgba
import time

# Current position is (9, 7).
# Let's walk the path to (3, 7) and then exit.

path = [
    ("Left", 4), # (9,7) -> (5,7)
    ("Up", 3),   # (5,7) -> (5,4)
    ("Left", 1), # (5,4) -> (4,4)
    ("Up", 3),   # (4,4) -> (4,1)
    ("Left", 1), # (4,1) -> (3,1)
    ("Down", 6), # (3,1) -> (3,7)
]

print("Starting walk to the exit (3, 7)...")
for direction, steps in path:
    for i in range(steps):
        pos = mgba.get_coordinates()
        print(f"At {pos}, pressing {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.35)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # retry once
            time.sleep(0.5)
            mgba.press_buttons([direction])
            time.sleep(0.35)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"FAILED to move {direction} at {pos}")
                break

pos = mgba.get_coordinates()
print(f"Final position before exit: {pos}")

if pos['x'] == 3 and pos['y'] == 7:
    print("Pressing Down to exit...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    print(f"New position after exit: {mgba.get_coordinates()}")
else:
    print("Not at exit position, not exiting.")
