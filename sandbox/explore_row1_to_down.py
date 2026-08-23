import mgba
import time
from collections import deque

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 100"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 500"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 100"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        attempts = 0
        while pos_before == pos_after and attempts < 3:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Let's map out the walkable area on 3F West starting from (7, 11) in State A
# We will do a safe, non-destructive BFS exploration to see if we can reach y=6
start = mgba.get_coordinates()
print("Starting BFS search from:", start)

queue = deque([start])
visited = { (start['x'], start['y']) }
path_to_y6 = None

# Let's write a quick simulator based on our visual knowledge
# Since we are standing at (17, 7) on 1F West, wait!
# WE ARE AT (17, 7) ON 1F WEST!
# Oh, we are NOT on 3F West! We are on 1F West!
print("Wait, we are currently at:", start)
