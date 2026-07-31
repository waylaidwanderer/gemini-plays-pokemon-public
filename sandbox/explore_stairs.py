import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

# Start at (3, 13)
print("Start Position:", mgba.get_coordinates())

# 1. Walk Up to (3, 9)
mgba.press_buttons(["Up", "Up", "Up", "Up"])
wait_for_movement()
print("At (3, 9):", mgba.get_coordinates())

# 2. Right onto (4, 9) (LEFT spinner) -> spins to (2, 9) stopper
mgba.press_buttons(["Right"])
time.sleep(1.5)
wait_for_movement()
print("At (2, 9) stopper:", mgba.get_coordinates())

# 3. Walk to (4, 14) via (3, 9) -> (3, 13) -> (4, 13) -> (4, 14)
mgba.press_buttons(["Right"])
wait_for_movement()
mgba.press_buttons(["Down", "Down", "Down", "Down"])
wait_for_movement()
mgba.press_buttons(["Right"])
wait_for_movement()
mgba.press_buttons(["Down"])
wait_for_movement()
print("At (4, 14):", mgba.get_coordinates())

# 4. Right onto (5, 14) (RIGHT spinner) -> spins to (9, 16) stopper
mgba.press_buttons(["Right"])
time.sleep(2.0)
wait_for_movement()
print("At (9, 16) stopper:", mgba.get_coordinates())

# 5. Right to (10, 16)
mgba.press_buttons(["Right"])
wait_for_movement()
print("At (10, 16):", mgba.get_coordinates())

# 6. Down onto (10, 17) (RIGHT spinner) -> spins to (14, 15) stopper
mgba.press_buttons(["Down"])
time.sleep(2.0)
wait_for_movement()
print("At (14, 15) stopper:", mgba.get_coordinates())

# 7. Right to (15, 15) -> Down onto (15, 16) (DOWN spinner) -> spins to (15, 18) stopper
mgba.press_buttons(["Right", "Down"])
time.sleep(2.0)
wait_for_movement()
print("At (15, 18) stopper:", mgba.get_coordinates())

# 8. Right onto (16, 18) (UP spinner) -> spins to (16, 13) stopper
mgba.press_buttons(["Right"])
time.sleep(2.0)
wait_for_movement()
print("At (16, 13) stopper:", mgba.get_coordinates())

# 9. Walk to the Right Room past the Rocket Grunt:
# To (19, 13)
mgba.press_buttons(["Right", "Right", "Right"])
wait_for_movement()
print("At (19, 13):", mgba.get_coordinates())

# Walk down and right around the Grunt to reach (23, 14)
mgba.press_buttons(["Right", "Right", "Down", "Right"])
wait_for_movement()
print("At (23, 14):", mgba.get_coordinates())

# Walk to Row 15
mgba.press_buttons(["Down"])
wait_for_movement()
print("At (23, 15):", mgba.get_coordinates())

# Let's explore the far right area comprehensively (Columns 24-28, Rows 10-15)
# We will do a local DFS to find any staircases!
walkable_far_right = set()
visited_far_right = set()

def dfs_far_right(pos):
    walkable_far_right.add(pos)
    visited_far_right.add(pos)
    
    # Try all 4 directions
    directions = ['Up', 'Down', 'Left', 'Right']
    opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
    
    for move in directions:
        dx, dy = 0, 0
        if move == 'Up': dy = -1
        elif move == 'Down': dy = 1
        elif move == 'Left': dx = -1
        elif move == 'Right': dx = 1
        
        nxt = (pos[0] + dx, pos[1] + dy)
        
        # We only explore the far-right area (X between 23 and 28, Y between 10 and 15)
        if 23 <= nxt[0] <= 28 and 10 <= nxt[1] <= 15:
            if nxt not in visited_far_right:
                mgba.press_buttons([move])
                p_new_coords = wait_for_movement()
                p_new = (p_new_coords['x'], p_new_coords['y'])
                
                if p_new == nxt:
                    dfs_far_right(p_new)
                    mgba.press_buttons([opposite[move]])
                    wait_for_movement()
                else:
                    visited_far_right.add(nxt)

dfs_far_right((23, 15))

print("ALL WALKABLE TILES IN FAR RIGHT AREA:")
print(sorted(list(walkable_far_right)))

screenshot_path = mgba.take_screenshot()
print("Exploration Screenshot:", screenshot_path)
