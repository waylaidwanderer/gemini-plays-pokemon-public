import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.3)
    return get_pos()

start = get_pos()
print(f"Walking Left from {start} to Column 1...")

# Walk left to Column 1
curr = start
while curr[0] > 1:
    pos = press_and_wait("Left")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

# Walk up to the stairs at (1, 1)
print(f"Reached {curr}. Walking Up to the stairs...")
while curr[1] > 1:
    pos = press_and_wait("Up")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

print("Final position before stairs:", get_pos())
