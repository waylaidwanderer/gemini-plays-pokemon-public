# Simulation of B3F Spinner Maze to find a path from (3, 19) to (3, 21)

# Grid layout defined by (X, Y) coordinates.
# X is column (0 to 8 on screen, but can extend).
# Y is row (15 to 23 on screen).

# Define boundaries or known tiles on B3F.
# Let's map everything we see on the screen.

walls = set()
spinners = {} # (x, y) -> 'L', 'R', 'U', 'D'
stoppers = set()

# Wall coordinates (green desks, solid walls, etc.)
# Row 15:
# - (-1, 15) is wall, (0, 15) is vertical wall line
# Row 16:
# - (2, 16), (3, 16), (5, 16), (6, 16), (7, 16) are green desks
for x in [2, 3, 5, 6, 7]:
    walls.add((x, 16))
# Row 17:
# - (5, 17), (6, 17), (7, 17), (8, 17) are green desks
for x in [5, 6, 7, 8]:
    walls.add((x, 17))
# Row 18:
# - (2, 18), (3, 18), (4, 18), (8, 18) are green desks
for x in [2, 3, 4, 8]:
    walls.add((x, 18))
# Row 20:
# - (2, 20), (3, 20), (5, 20), (7, 20) are green desks
for x in [2, 3, 5, 7]:
    walls.add((x, 20))
# Row 21:
# - (2, 21), (7, 21) are green desks.
# - (3, 21) has the Poké Ball. We can treat (3, 21) as the goal or walkable once we reach (4, 21).
for x in [2, 7]:
    walls.add((x, 21))
# Row 22:
# - (3, 22), (5, 22), (7, 22) are green desks
for x in [3, 5, 7]:
    walls.add((x, 22))
# Row 23:
# - (3, 23), (5, 23), (7, 23) are green desks
for x in [3, 5, 7]:
    walls.add((x, 23))

# Left/right borders
for y in range(15, 24):
    walls.add((0, y)) # (0, y) is solid black vertical line/wall
    walls.add((-1, y))

# Spinners
# Row 15:
spinners[(4, 15)] = 'R'
spinners[(8, 15)] = 'U'
# Row 16:
spinners[(4, 16)] = 'U'
# Row 19:
spinners[(4, 19)] = 'L'
spinners[(8, 19)] = 'L'
# Row 22:
spinners[(4, 22)] = 'U'
spinners[(6, 22)] = 'U'
# Row 23:
spinners[(8, 23)] = 'U'

# Stoppers
stoppers.add((2, 19))
stoppers.add((6, 20))

# Other elements on screen:
# Y can go outside 15..23?
# Let's assume standard boundaries for this corner.

def get_next_state(pos, move):
    # pos is (x, y)
    # move is 'Up', 'Down', 'Left', 'Right'
    dx, dy = 0, 0
    if move == 'Up': dy = -1
    elif move == 'Down': dy = 1
    elif move == 'Left': dx = -1
    elif move == 'Right': dx = 1
    
    nx, ny = pos[0] + dx, pos[1] + dy
    if (nx, ny) in walls:
        return pos # blocked, stay in place
        
    # We moved to (nx, ny). Now, if it's a spinner, we slide!
    curr = (nx, ny)
    while curr in spinners:
        sd = spinners[curr]
        sdx, sdy = 0, 0
        if sd == 'U': sdy = -1
        elif sd == 'D': sdy = 1
        elif sd == 'L': sdx = -1
        elif sd == 'R': sdx = 1
        
        next_step = (curr[0] + sdx, curr[1] + sdy)
        if next_step in walls:
            # Hit a wall, stop on curr
            break
        # Move to next tile
        curr = next_step
        if curr in stoppers:
            # Hit a stopper, stop sliding
            break
            
    return curr

# BFS to find the shortest path from (3, 19) to (3, 21)
# Goal is reached if we can move onto (3, 21) from its neighbor (4, 21) (since (4, 21) is the only open neighbor of (3, 21)).
# Let's check BFS!
from collections import deque

start = (3, 19)
queue = deque([(start, [])])
visited = {start}

found = False
while queue:
    curr, path = queue.popleft()
    if curr == (3, 21):
        print("FOUND IT! Path:", path)
        found = True
        break
        
    # Explore 4 directions
    for move in ['Up', 'Down', 'Left', 'Right']:
        nxt = get_next_state(curr, move)
        if nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, path + [move]))

if not found:
    print("No path found within the on-screen boundaries.")
