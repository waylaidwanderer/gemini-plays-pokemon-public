import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    return pos_after

# We are at (9, 12) on Cinnabar Island.
# Walk around the signpost to (9, 10) and test walking UP Column 9!
print("Walking around the signpost to (9, 10)...")
walk_step("Left")  # to (8, 12)
walk_step("Up")    # to (8, 11)
walk_step("Up")    # to (8, 10)
walk_step("Right") # to (9, 10)

print("Arrived at (9, 10):", mgba.get_coordinates())

print("\nTesting walking UP Column 9...")
for i in range(10):
    pos_before = mgba.get_coordinates()
    pos_after = walk_step("Up")
    print(f"Row {pos_after['y']}")
    if pos_before == pos_after:
        print(f"Column 9 blocked at Row {pos_after['y']}")
        break
    if pos_after['y'] <= 3:
        print("Column 9 is 100% OPEN to the North side!")
        break

time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
