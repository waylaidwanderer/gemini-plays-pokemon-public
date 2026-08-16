import mgba
import time
from collections import deque

print("--- BFS TO FIND GATEHOUSE EXIT ---")

# We start at the current position.
# We want to find a tile that warps us out of the gatehouse.
# When we warp, our 'x' coordinate will become 18 (or similar Fuchsia City coordinate),
# or the map will change.
# Let's write a robust script to search for the exit.

def get_pos():
    return mgba.get_coordinates()

start_pos = get_pos()
print("Start position:", start_pos)

# Since we want to find the exit, we can try to walk towards y=15 or similar bottom coordinates.
# Let's explore the walkable area.
# In Gen 1, we can walk by pressing buttons.
# Let's trace a path to the bottom-left area where the doormat seems to be.
# Looking at the screen, column 6 or 7 at y=15 seems to have a doormat.
# Let's try to walk to (6, 15) or (7, 15).
# From (8, 12):
# We can go Left to (7, 12), then Down to (7, 13), (7, 14), (7, 15) or similar.
# Let's try a direct path of moves first to see if it works:

path_moves = [
    "Left",   # to (7, 12)
    "Left",   # to (6, 12)
    "Down",   # to (6, 13)
    "Down",   # to (6, 14)
    "Down",   # to (6, 15)
    "Down",   # to (6, 16) - exit?
]

for move in path_moves:
    pos = get_pos()
    print(f"Before move '{move}': {pos}")
    mgba.press_buttons([move])
    time.sleep(0.5)
    
    new_pos = get_pos()
    print(f"After move '{move}': {new_pos}")
    if new_pos and new_pos['x'] > 12:
        print("Successfully warped out of the gatehouse!")
        break

mgba.take_screenshot()
print("Final position:", get_pos())
