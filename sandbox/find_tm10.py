# Refined simulation of B3F Spinner Maze to find a path from (1, 24) to (3, 21)
# Using current position (1, 24) as start.

walls = set()
spinners = {} # (x, y) -> 'L', 'R', 'U', 'D'
stoppers = set()

# Wall coordinates (green desks, solid walls, etc.)
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
for x in [2, 3, 5, 7]:
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
for y in range(15, 28):
    walls.add((0, y))
    walls.add((-1, y))
    walls.add((9, y)) # right border of the room

# Bottom border
for x in range(-1, 10):
    walls.add((x, 27)) # row 27 is the bottom wall line/black boundary

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

# Stoppers
stoppers.add((2, 19))
stoppers.add((6, 20))

def get_next_state(pos, move):
    dx, dy = 0, 0
    if move == 'Up': dy = -1
    elif move == 'Down': dy = 1
    elif move == 'Left': dx = -1
    elif move == 'Right': dx = 1
    
    nx, ny = pos[0] + dx, pos[1] + dy
    if (nx, ny) in walls:
        return pos # blocked, stay in place
        
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

start = (1, 24)
queue = deque([(start, [])])
visited = {start}

found = False
while queue:
    curr, path = queue.popleft()
    if curr == (3, 21):
        print("FOUND IT! Path from (1, 24):", path)
        found = True
        break
        
    for move in ['Up', 'Down', 'Left', 'Right']:
        nxt = get_next_state(curr, move)
        if nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, path + [move]))

if not found:
    print("No path found.")
