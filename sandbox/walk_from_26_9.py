import mgba
import time

# We are at (26, 9) inside Mansion 1F (east wing).
# Walk to B1F stairs at (21, 24):
# Up 6 to (26, 3)
# Left 7 to (19, 3)
# Down 21 to (19, 24)
# Right 2 to (21, 24) (warp)

buttons = []
buttons += ["Up"] * 6
buttons += ["Left"] * 7
buttons += ["Down"] * 21
buttons += ["Right"] * 2

print("Walking to B1F stairs step-by-step from (26, 9)...")
for i, btn in enumerate(buttons):
    mgba.press_buttons([btn])
    time.sleep(0.4) # Wait for animation to complete
    pos = mgba.get_coordinates()
    print(f"Step {i+1}: pressed {btn}, pos is {pos}")
