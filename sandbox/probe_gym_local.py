import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting local probe from (10, 9)...")

# Steps:
# 1. Right to (11, 9)
# 2. Right to (12, 9)
# 3. Right to (13, 9)
# 4. Right to (14, 9)
# 5. Right to (15, 9)
steps = [
    ("Right", (11, 9)),
    ("Right", (12, 9)),
    ("Right", (13, 9)),
    ("Right", (14, 9)),
    ("Right", (15, 9))
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
