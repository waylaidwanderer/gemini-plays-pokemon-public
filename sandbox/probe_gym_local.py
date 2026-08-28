import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting Giovanni search from:", get_pos())

# Steps:
# 1. Down to (18, 2)
# 2. Down to (18, 3)
# 3. Left to (17, 3)
# 4. Left to (16, 3)
# 5. Left to (15, 3)
# 6. Left to (14, 3)
steps = [
    ("Down", (18, 2)),
    ("Down", (18, 3)),
    ("Left", (17, 3)),
    ("Left", (16, 3)),
    ("Left", (15, 3)),
    ("Left", (14, 3))
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
