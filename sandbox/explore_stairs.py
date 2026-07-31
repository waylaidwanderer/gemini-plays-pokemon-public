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

# We are currently at (1, 15)
print("Start Position:", mgba.get_coordinates())

# 1. Walk Right onto (4, 15) spinner -> spins us to (8, 11) stopper
print("Walking to spinner...")
mgba.press_buttons(["Right", "Right", "Right"])
time.sleep(3.0) # Let the slide finish
p_stopper = wait_for_movement()
print("Landed at stopper:", p_stopper)

# 2. From (8, 11) stopper, let's explore going Up and Left to see how far we can go!
# We'll try walking Up as much as possible
mgba.press_buttons(["Up"])
p_up = wait_for_movement()
print("Position after Up:", p_up)

if p_up != p_stopper:
    # Try Left
    mgba.press_buttons(["Left"])
    p_left = wait_for_movement()
    print("Position after Left:", p_left)
    
    if p_left != p_up:
        # Walk Left as much as possible
        for i in range(10):
            mgba.press_buttons(["Left"])
            p_new = wait_for_movement()
            if p_new == p_left:
                print("Blocked going Left at:", p_left)
                break
            p_left = p_new
            print(f"Left step {i+2}:", p_left)

# Take screenshot to verify where we ended up
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
