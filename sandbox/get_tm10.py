import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

print("Start Position:", mgba.get_coordinates())

# Complete, bulletproof path to TM10!
path_to_stopper = [
    "Left",               # to (1, 19)
    "Down", "Down", "Down", "Down", "Down", "Down", # to (1, 25)
    "Right", "Right", "Right", "Right", "Right", # to (6, 25)
    "Up"                  # onto (6, 24) UP spinner -> spins to (6, 20) stopper
]

for idx, move in enumerate(path_to_stopper):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"Step {idx+1} ({move}):", pos)

print("Should be at (6, 20) stopper:", mgba.get_coordinates())
time.sleep(0.5)

# Take screenshot to verify we are at (6, 20)
screenshot_stopper = mgba.take_screenshot()
print("Screenshot at Stopper:", screenshot_stopper)

# Walk to the Poké Ball
walk_to_ball = [
    "Down", # to (6, 21)
    "Left", # to (5, 21)
    "Left", # to (4, 21)
    "Left"  # to (3, 21) (Poké Ball!)
]

for idx, move in enumerate(walk_to_ball):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"Walk to Ball Step {idx+1} ({move}):", pos)

# Press 'A' to interact and get the item (if we haven't already by stepping on it)
# Wait, stepping on an item automatically triggers the textbox in Gen 1, so we should see dialog.
# Let's press 'A' to clear dialog and print coordinate
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(0.5)

print("Final Position after picking up item:", mgba.get_coordinates())
screenshot_final = mgba.take_screenshot()
print("Final Screenshot:", screenshot_final)
