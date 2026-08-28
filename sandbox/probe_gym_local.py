import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting right-upper channel probe from current position:", get_pos())

# Steps:
# 1. Up to (12, 8)
# 2. Up to (12, 7)
# 3. Up to (12, 6)
# 4. Right to (13, 6)
# 5. Right to (14, 6)
# 6. Right to (15, 6)
# 7. Right to (16, 6)
# 8. Right to (17, 6)
steps = [
    ("Up", (12, 8)),
    ("Up", (12, 7)),
    ("Up", (12, 6)),
    ("Right", (13, 6)),
    ("Right", (14, 6)),
    ("Right", (15, 6)),
    ("Right", (16, 6)),
    ("Right", (17, 6))
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
