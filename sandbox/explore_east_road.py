import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def handle_battle():
    print("  Battle/Dialogue detected! Handling...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    # Run option: Down, Right, A
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_dir(d):
    before = get_pos()
    mgba.press_buttons([d])
    time.sleep(0.4)
    after = get_pos()
    if before == after:
        handle_battle()
        after = get_pos()
    return after != before, after

# Dismiss "Got away safely!"
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Starting 1F East exploration from:", get_pos())

# We want to go East and South towards the bottom-right (21, 23) or similar.
# Let's try walking:
# 1. Walk Right along row 12 as far as possible (up to col 21)
# 2. Walk Down col 21 as far as possible (up to row 23)
# If blocked, try to bypass.
for i in range(15):
    c = get_pos()
    print(f"Step {i+1}: position is {c}")
    # Try to move Right first
    success, pos = step_dir("Right")
    if not success:
        # If blocked moving Right, try moving Down
        print("  Blocked Right! Trying Down...")
        success2, pos2 = step_dir("Down")
        if not success2:
            # If blocked moving Down, try Up
            print("  Blocked Down! Trying Up...")
            success3, pos3 = step_dir("Up")
            if not success3:
                print("  Completely stuck! Exiting.")
                break

print("Exploration finished. Final position:", get_pos())
mgba.take_screenshot()
