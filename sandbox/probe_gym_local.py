import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting central-upper channel probe from current position:", get_pos())

# Steps:
# 1. Up to (16, 2)
# 2. Up to (16, 1)
steps = [
    ("Up", (16, 2)),
    ("Up", (16, 1))
]

for d, c in steps:
    # Ensure no battle/dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.1)
    
    old_pos = get_pos()
    mgba.press_buttons([d])
    time.sleep(0.55)
    new_pos = get_pos()
    print(f"Tried {d} from {old_pos}. Landed at: {new_pos}")
    
    if new_pos != c:
        print(f"Offset detected! Expected {c}, got {new_pos}. Aborting.")
        break
