import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting platform probe from current position:", get_pos())

# Steps from (6, 1):
# 1. Down to (6, 2)
# 2. Down to (6, 3)
# 3. Down to (6, 4) (platform!)
steps = [
    ("Down", (6, 2)),
    ("Down", (6, 3)),
    ("Down", (6, 4))
]

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
