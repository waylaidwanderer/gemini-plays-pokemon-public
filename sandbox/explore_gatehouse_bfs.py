import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press(btn):
    mgba.press_buttons([btn])
    time.sleep(0.1)

# A simple script to explore walkable tiles around the current position
visited = set()
queue = []
path_to = {}

start_pos = get_pos()
queue.append(start_pos)
visited.add(start_pos)
path_to[start_pos] = []

print(f"Starting BFS from {start_pos}")

# We will just do a small coordinate verification by trying to move in 4 directions
# from our current position and seeing where we end up.
# Let's try to move Left and see if we can walk back to Fuchsia City or find the exit.

directions = {
    "Left": (-1, 0),
    "Right": (1, 0),
    "Up": (0, -1),
    "Down": (0, 1)
}

# Let's probe neighbors from the current position
x, y = start_pos
for dir_name, (dx, dy) in directions.items():
    press(dir_name)
    nx, ny = get_pos()
    if (nx, ny) != (x, y):
        print(f"Walked {dir_name} to {(nx, ny)}")
        # Go back
        back_dir = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}[dir_name]
        press(back_dir)
    else:
        print(f"Blocked {dir_name} from {start_pos}")

print("Probing complete.")
