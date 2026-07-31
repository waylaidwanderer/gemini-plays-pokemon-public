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

# We are currently at (11, 20)
start_pos = mgba.get_coordinates()
print("Start Position:", start_pos)

# We want to perform a systematic DFS/BFS in the actual game to find all walkable coordinates reachable from (11, 20).
# We will only walk on normal tiles (we want to avoid stepping on any spinners that warp us away, 
# but if we do step on a spinner, we'll slide, and the script will track where we land and try to walk back).
# Wait, to make it super safe, let's just do a localized empirical test:
# Can we go from (11, 20) to (14, 20), then down to (14, 23)?
# Yes, we did that.
# Let's test if we can walk Right from (14, 21), (14, 22), (14, 23).
# Let's write a function to try to move Right from a position and then move back if it succeeded.

def test_direction(path_to_tile, move):
    # Walk to the tile
    for step in path_to_tile:
        mgba.press_buttons([step])
        wait_for_movement()
    
    pos_before = mgba.get_coordinates()
    # Try the move
    mgba.press_buttons([move])
    pos_after = wait_for_movement()
    
    success = (pos_after != pos_before)
    
    # Walk back to start
    # To do this safely, we can just press the opposite buttons in reverse order
    # (assuming no spinner was stepped on)
    opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
    if success:
        # Check if we stepped on a spinner (which would have moved us more than 1 tile)
        dx = abs(pos_after['x'] - pos_before['x'])
        dy = abs(pos_after['y'] - pos_before['y'])
        if dx > 1 or dy > 1:
            print(f"Stepped on spinner with move {move} from {pos_before} -> landed at {pos_after}!")
            # We stepped on a spinner, so we can't easily walk back the same way.
            # Let's just print this and not try to walk back (the script will finish or we'll reset to start).
            return pos_after
        else:
            # Succeeded 1 step, walk back 1 step
            mgba.press_buttons([opposite[move]])
            wait_for_movement()
            
    for step in reversed(path_to_tile):
        mgba.press_buttons([opposite[step]])
        wait_for_movement()
        
    return success

# Let's test if column 15 is walkable on any of the rows 20, 21, 22, 23!
# We can reach:
# (14, 20) via ["Right", "Right", "Right"]
# (14, 21) via ["Right", "Right", "Right", "Down"]
# (14, 22) via ["Right", "Right", "Right", "Down", "Down"]
# (14, 23) via ["Right", "Right", "Right", "Down", "Down", "Down"]

print("Testing (15, 20) (Right from row 20):")
print("Result:", test_direction(["Right", "Right", "Right"], "Right"))

print("Testing (15, 21) (Right from row 21):")
print("Result:", test_direction(["Right", "Right", "Right", "Down"], "Right"))

print("Testing (15, 22) (Right from row 22):")
print("Result:", test_direction(["Right", "Right", "Right", "Down", "Down"], "Right"))

print("Testing (15, 23) (Right from row 23):")
print("Result:", test_direction(["Right", "Right", "Right", "Down", "Down", "Down"], "Right"))

print("Finished testing. Current Position:", mgba.get_coordinates())
