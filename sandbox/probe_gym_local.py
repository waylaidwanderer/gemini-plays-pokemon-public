import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting Row 1 Leftward search from:", get_pos())

# Steps from (16, 1):
# 1. Left to (15, 1)
# ...
# 10. Left to (6, 1)
steps = []
for x in range(15, 5, -1):
    steps.append(("Left", (x, 1)))
    
for d, c in steps:
    mgba.press_buttons(["B"])
    time.sleep(0.1)
    
    old_pos = get_pos()
    mgba.press_buttons([d])
    time.sleep(0.55)
    new_pos = get_pos()
    print(f"Tried {d} from {old_pos}. Landed at: {new_pos}")
    
    if new_pos != c:
        print(f"Offset/block detected! Expected {c}, got {new_pos}. Aborting.")
        break
