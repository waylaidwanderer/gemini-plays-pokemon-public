import mgba
import time

visited = set()
to_visit = [mgba.get_coordinates()]
print("Starting systematic area mapping...")

# Since we want to find all reachable coordinates, we can do a DFS or BFS.
# But because we are physically moving the player, we have to backtrack.
# Instead of a full graph search which requires complex backtracking code,
# we can use a simpler approach: walk in a direction, if position changes, record it,
# then walk back.
# Even simpler: let's write a script that attempts to move in a grid pattern
# or just lets us manually explore some paths, or does a simple backtracking search.

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def run_from_battle():
    # If we get into a battle, we run away
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 1000"])
    mgba.press_buttons(["B", "sleep 200", "B", "sleep 200"])

# Let's do a simple recursive DFS with backtracking
path = []
reachable = set()

def dfs(current_pos):
    reachable.add(current_pos)
    # Try the 4 directions: Up, Down, Left, Right
    directions = [('Up', 0, -1), ('Down', 0, 1), ('Left', -1, 0), ('Right', 1, 0)]
    for move, dx, dy in directions:
        next_pos = (current_pos[0] + dx, current_pos[1] + dy)
        if next_pos not in reachable:
            # Attempt to move
            mgba.press_buttons([move])
            time.sleep(0.3)
            pos = get_pos()
            if pos == current_pos:
                # We hit a wall, next_pos is not reachable
                # Wait, what if we entered a battle? Let's check if we had a battle.
                # If we did, let's run away.
                # To be simple, let's just assume it's a wall or handle battle
                pass
            elif pos == next_pos:
                # Successfully moved!
                dfs(next_pos)
                # Now backtrack to current_pos
                opposite = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}[move]
                mgba.press_buttons([opposite])
                time.sleep(0.3)
                # Verify we backtracked successfully
                b_pos = get_pos()
                if b_pos != current_pos:
                    print(f"Backtrack failed! Expected {current_pos}, got {b_pos}")
                    # If we got into a battle, run away and try again
                    run_from_battle()
                    time.sleep(0.5)
                    mgba.press_buttons([opposite])
                    time.sleep(0.3)

start = get_pos()
print("Starting position:", start)
dfs(start)
print("Reachable tiles:", sorted(list(reachable)))
mgba.take_screenshot()
