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

# Path found by BFS:
# ['Up', 'Up', 'Left', 'Left', 'Up', 'Up', 'Right', 'Right', 'Right', 'Up', 'Right', 'Right', 'Right', 'Right', 'Down', 'Right', 'Right', 'Down', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right', 'Down', 'Right', 'Right', 'Up']
path = [
    'Up', 'Up',               # to (4, 19) spinner -> (2, 19) stopper
    'Left', 'Left',           # to (1, 19) (bump)
    'Up', 'Up',               # to (1, 17)
    'Right', 'Right', 'Right',# to (4, 17)
    'Up',                     # to (4, 16) spinner -> (8, 11) stopper
    'Right', 'Right', 'Right', 'Right', # to (12, 11)
    'Down',                   # to (12, 12)
    'Right', 'Right',         # to (14, 12)
    'Down', 'Down', 'Down',   # to (14, 15)
    'Right', 'Right', 'Right', 'Right', # to (18, 15)
    'Down',                   # to (18, 16)
    'Right', 'Right',         # to (20, 16)
    'Up'                      # into warp stairs or toward the stairs area
]

# We will execute each move one-by-one and print our position to track progress.
for idx, move in enumerate(path):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"Step {idx+1} ({move}):", pos)
    # Check if we transitioned to B4F (Map transition)
    # If the map transition occurs, we will see a change or pos will change.
    
# Take screenshot to verify we reached B4F
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
