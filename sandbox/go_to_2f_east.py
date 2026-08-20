import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Initial position:", get_pos())

# Step Left onto the stairs at (15, 11)
print("Stepping Left onto stairs...")
mgba.press_buttons(["Left"])
time.sleep(2.0) # wait for screen warp animation

print("Post-warp position:", get_pos())
mgba.take_screenshot()
