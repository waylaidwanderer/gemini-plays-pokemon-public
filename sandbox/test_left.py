import mgba
import time

def get_pos():
    for _ in range(5):
        pos = mgba.get_coordinates()
        if pos != {'x': 0, 'y': 0}:
            return pos['x'], pos['y']
        time.sleep(0.1)
    return 0, 0

start_x, start_y = get_pos()
print(f"Starting at: ({start_x}, {start_y})")

x, y = start_x, start_y
for i in range(40):
    mgba.press_buttons(["Left"])
    time.sleep(0.1)
    nx, ny = get_pos()
    if (nx, ny) == (x, y):
        print(f"Blocked at: ({x}, {y}) after {i} steps")
        break
    x, y = nx, ny
    print(f"Step {i+1}: ({x}, {y})")
