import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting main Gym entry probe from current position:", get_pos())

# We are at (1, 14)
# Steps:
# 1. Right to (2, 14)
# 2. Up to (2, 13)
# 3. Right to (3, 13)
# 4. Right to (4, 13)
steps = [
    ("Right", (2, 14)),
    ("Up", (2, 13)),
    ("Right", (3, 13)),
    ("Right", (4, 13))
]

for d, c in steps:
    # Ensure no battle/dialogue
    # Press B to be safe
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
