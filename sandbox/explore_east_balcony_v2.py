import mgba
import time

def handle_battle():
    print("Likely in battle! Attempting to flee...")
    # Gen 1 Battle Menu: FIGHT is top-left. RUN is bottom-right.
    # To run: Down, Right, A (or Right, Down, A)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_to_adjacent(dir_str):
    pos = mgba.get_coordinates()
    mgba.press_buttons([dir_str])
    time.sleep(0.55)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # Check if battle triggered
        handle_battle()
        new_pos = mgba.get_coordinates()
    return new_pos

# Let's perform a BFS from the current position.
# We will track coordinates we have visited.
# Since we are on foot and can move, we'll build a map.
# But wait, BFS on-foot is tricky because we have to physically move the character.
# We can do a DFS (Depth First Search) with backtracking, which is much easier to implement on-foot!
# Let's write a DFS recursive explorer.

visited = set()
walls = set()

def explore():
    curr = mgba.get_coordinates()
    curr_tup = (curr['x'], curr['y'])
    visited.add(curr_tup)
    print(f"Visited: {curr_tup}")
    
    # Directions to try: Up, Down, Left, Right
    directions = {
        'Up': (0, -1),
        'Down': (0, 1),
        'Left': (-1, 0),
        'Right': (1, 0)
    }
    
    for d, (dx, dy) in directions.items():
        target = (curr_tup[0] + dx, curr_tup[1] + dy)
        if target in visited or target in walls:
            continue
            
        # Try to step in direction d
        new_pos = walk_to_adjacent(d)
        new_tup = (new_pos['x'], new_pos['y'])
        
        if new_tup == curr_tup:
            # We bumped, so target is a wall
            walls.add(target)
            print(f"Wall at: {target}")
        else:
            # Successfully moved to target!
            explore()
            # Backtrack
            opposite = {
                'Up': 'Down',
                'Down': 'Up',
                'Left': 'Right',
                'Right': 'Left'
            }[d]
            back_pos = walk_to_adjacent(opposite)
            print(f"Backtracked to: {back_pos}")

# Start exploration!
explore()
print("Exploration finished!")
print("Visited tiles:", sorted(list(visited)))
print("Wall tiles:", sorted(list(walls)))
