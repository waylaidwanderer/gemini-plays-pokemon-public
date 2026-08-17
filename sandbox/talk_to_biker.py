import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start at (19, 3).
curr = get_pos()
print(f"Walking to (15, 5) to talk to the Biker at (16, 5) from {curr}...")

# 1. Walk Left 4 steps to (15, 3)
while curr[0] > 15:
    pos = press_and_wait("Left")
    if pos == curr:
        print(f"Blocked Left at {curr}")
        break
    curr = pos

# 2. Walk Down 2 steps to (15, 5)
while curr[1] < 5:
    pos = press_and_wait("Down")
    if pos == curr:
        print(f"Blocked Down at {curr}")
        break
    curr = pos

print(f"Reached {curr}. Turning Right and talking to Biker...")
# Face Right
press_and_wait("Right")
# Press A
mgba.press_buttons(["A"])
time.sleep(0.5)

print("Talk initiated. Let's see dialogue!")
