import mgba
import time

def move(d, steps=1):
    for i in range(steps):
        mgba.press_buttons([d, "sleep 300"])
        time.sleep(0.4)
    return mgba.get_coordinates()

# Stand at (9, 16).
# Walk Right twice to step onto the RIGHT spinner at (11, 16):
print("Walking Right from current position...")
pos1 = move("Right", 1)
print("Position 1:", pos1)

pos2 = move("Right", 1)
print("Position 2:", pos2)

# Wait a second for slide to complete
time.sleep(1.5)

final_pos = mgba.get_coordinates()
print("Final Position after sliding:", final_pos)

screenshot = mgba.take_screenshot()
print("Screenshot taken.")
