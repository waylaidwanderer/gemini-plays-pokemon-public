import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.1)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.1)
        p2 = mgba.get_coordinates()
    return p1

# We are currently at (11, 20) stopper
start_pos = mgba.get_coordinates()
print("Start Position:", start_pos)

# Let's test walking Right from (11, 20)
print("Testing Right from (11, 20)...")
mgba.press_buttons(["Right"])
p = wait_for_movement()
print("Position after 1 Right:", p)

if p != start_pos:
    # Walk Right as much as possible
    for i in range(10):
        mgba.press_buttons(["Right"])
        p_new = wait_for_movement()
        if p_new == p:
            print(f"Blocked going Right at: {p}")
            break
        p = p_new
        print(f"Right step {i+2}: {p}")

# Walk back to start or try other directions from wherever we end up
# Let's take a screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
