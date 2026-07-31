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

# We are currently at (14, 20)
print("Start Position:", mgba.get_coordinates())

# Let's explore Down
print("Moving Down to (14, 21)...")
mgba.press_buttons(["Down"])
p1 = wait_for_movement()
print("Position:", p1)

print("Moving Down to (14, 22)...")
mgba.press_buttons(["Down"])
p2 = wait_for_movement()
print("Position:", p2)

print("Moving Down to (14, 23)...")
mgba.press_buttons(["Down"])
p3 = wait_for_movement()
print("Position:", p3)

# Let's see if we can move in other directions from (14, 23)
# Let's try Right
print("Testing Right from (14, 23)...")
mgba.press_buttons(["Right"])
p_right = wait_for_movement()
print("Position after Right:", p_right)

if p_right == p3:
    print("Right is blocked from (14, 23). Trying Left onto (13, 23) spinner...")
    mgba.press_buttons(["Left"])
    time.sleep(2.0) # Let the slide finish
    p_left = wait_for_movement()
    print("Position after Left/Slide:", p_left)

screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
