# BFS on B3F to find a path from current (4, 21) to B4F stairs (18, 19)

walls = set()
spinners = {} # (x, y) -> 'L', 'R', 'U', 'D'
stoppers = set()

# Let's map everything we know on B3F!
# Left Room and Maze
# Row 16:
for x in [2, 3, 5, 6, 7]:
    walls.add((x, 16))
# Row 17:
for x in [5, 6, 7, 8]:
    walls.add((x, 17))
# Row 18:
for x in [2, 3, 4, 8]:
    walls.add((x, 18))
# Row 20:
for x in [2, 3, 5, 7, 15]: # (15, 20) is wall blocking row 20
    walls.add((x, 20))
# Row 21:
for x in [2, 7]:
    walls.add((x, 21))
# Row 22:
for x in [3, 5, 7]:
    walls.add((x, 22))
# Row 23:
for x in [3, 5, 7]:
    walls.add((x, 23))
# Row 24:
for x in [3, 5, 7]:
    walls.add((x, 24))
# Row 26:
for x in [4, 5, 6]:
    walls.add((x, 26))

# Left/right borders
for y in range(0, 30):
    walls.add((0, y))
    walls.add((-1, y))
    walls.add((29, y)) # right border of the whole floor (usually 28 or 29)

# Top/bottom boundaries of the floor
for x in range(-1, 30):
    walls.add((x, 5))  # row 5 is top wall
    walls.add((x, 27)) # row 27 is bottom wall

# Let's add known walls on the right side from our previous mapping:
# Column 18: Solid wall from Row 6 to 19, except gaps at (18, 10) and (18, 11).
for y in range(6, 20):
    if y not in [10, 11]:
        walls.add((18, y))

# Row 16: Solid wall from Column 18 to 28
for x in range(18, 29):
    walls.add((x, 16))

# Decorative columns at (24, 11) and (24, 13)
walls.add((24, 11))
walls.add((24, 13))

# Spinners
spinners[(4, 15)] = 'R'
spinners[(8, 15)] = 'U'
spinners[(4, 16)] = 'U'
spinners[(4, 19)] = 'L'
spinners[(8, 19)] = 'L'
spinners[(4, 22)] = 'U'
spinners[(6, 22)] = 'U'
spinners[(8, 23)] = 'U'
spinners[(6, 24)] = 'U'

# Let's add spinners from the upper maze (Rows 7-14, Columns 1-15)
spinners[(12, 13)] = 'U'
spinners[(12, 9)] = 'L'
spinners[(4, 9)] = 'L'
spinners[(9, 14)] = 'D'
spinners[(11, 16)] = 'R'
spinners[(14, 17)] = 'U'
spinners[(16, 14)] = 'U'
# from warp_to_b4f_row20.py:
spinners[(13, 18)] = 'L'
spinners[(11, 14)] = 'D'

# Stoppers
stoppers.add((2, 9))
stoppers.add((2, 19))
stoppers.add((6, 20))
stoppers.add((9, 16))
stoppers.add((15, 17))
stoppers.add((14, 15))
stoppers.add((16, 13))
stoppers.add((15, 18))
stoppers.add((11, 20))

# We can also add other known floor structures.
# Let's see if we can find a path using our standard movement physics.

def get_next_state(pos, move):
    dx, dy = 0, 0
    if move == 'Up': dy = -1
    elif move == 'Down': dy = 1
    elif move == 'Left': dx = -1
    elif move == 'Right': dx = 1
    
    nx, ny = pos[0] + dx, pos[1] + dy
    if (nx, ny) in walls:
        return pos
        
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
            break
        curr = next_step
        if curr in stoppers:
            break
            
    return curr

from collections import deque

start = (4, 21)
goal = (18, 19) # Stairs to B4F (warp triggers when walking Up from (18, 20) to (18, 19))
# So the path can end when we are at (18, 20) and go 'Up'

queue = deque([(start, [])])
visited = {start}

found = False
while queue:
    curr, path = queue.popleft()
    if curr == (18, 20):
        print("FOUND PATH TO STAIRS APPROACH TILE! Path:", path + ["Up"])
        found = True
        break
        
    for move in ['Up', 'Down', 'Left', 'Right']:
        nxt = get_next_state(curr, move)
        if nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, path + [move]))

if not found:
    print("No path found.")
