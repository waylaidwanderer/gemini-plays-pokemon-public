import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting warp down to 2F east wing from 3F. Current pos:", get_pos())

# Press B to clear the "Got away safely!" textbox
mgba.press_buttons(["B"])
time.sleep(0.3)

# Walk Left from (18, 11) to the stairs at (15, 11)
mgba.press_buttons(["Left"])
time.sleep(0.5)
print("Pos after first Left:", get_pos())

mgba.press_buttons(["Left"])
time.sleep(0.5)
print("Pos after second Left:", get_pos())

# Step Left onto the stairs at (15, 11) to warp down
print("Stepping onto stairs...")
mgba.press_buttons(["Left"])
time.sleep(1.5) # Allow warp transition to complete completely

print("Landed on 2F! Current pos:", get_pos())
mgba.take_screenshot()
