import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    return pos_after

# We are at (2, 3) inside the Cinnabar Lab room.
# Let's walk to Row 7 and test if (2, 8) or (3, 8) is the exit warp!

print("Walking Down to Row 7...")
for i in range(4):
    curr = walk_step("Down")
    print("At:", curr)

time.sleep(0.5)
pos_7 = mgba.get_coordinates()
print("Arrived at Row 7:", pos_7)

# Check if we are at (2, 7). If we got blocked, we will know.
if pos_7['y'] == 7:
    # Test stepping Down to (2, 8)
    print("Testing (2, 8) exit...")
    pos_after = walk_step("Down")
    print("Position after Down:", pos_after)
    if abs(pos_after['x'] - pos_7['x']) > 2 or abs(pos_after['y'] - pos_7['y']) > 2:
        print("WARPED via (2, 8)!")
    else:
        # Walk back to (2, 7) if we didn't warp
        if pos_after['y'] == 8:
            walk_step("Up")
            
        # Test (3, 8) exit
        print("\nTesting (3, 8) exit...")
        walk_step("Right") # to (3, 7)
        pos_after_3 = walk_step("Down")
        print("Position after Down:", pos_after_3)
        if abs(pos_after_3['x'] - pos_7['x']) > 2 or abs(pos_after_3['y'] - pos_7['y']) > 2:
            print("WARPED via (3, 8)!")

time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
