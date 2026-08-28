import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting top-most area probe from current position:", get_pos())

# Steps from (17, 6):
# 1. Up to (17, 5)
# 2. Up to (17, 4)
# 3. Up to (17, 3)
# 4. Right to (18, 3)
# 5. Up to (18, 2)
# 6. Up to (18, 1)
steps = [
    ("Up", (17, 5)),
    ("Up", (17, 4)),
    ("Up", (17, 3)),
    ("Right", (18, 3)),
    ("Up", (18, 2)),
    ("Up", (18, 1))
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
