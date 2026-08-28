import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting Giovanni search to the right from current position:", get_pos())

# Steps from (14, 3):
# 1. Right to (15, 3)
# ...
# 7. Right to (21, 3)
steps = []
for x in range(15, 22):
    steps.append(("Right", (x, 3)))
    
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
