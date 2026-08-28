import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

print("Starting platform south-side probe from current position:", get_pos())

# Steps from (6, 3):
# 1. Left to (5, 3)
# 2. Down to (5, 4)
# 3. Down to (5, 5)
# 4. Down to (5, 6)
# 5. Right to (6, 6)
# 6. Right to (7, 6)
steps = [
    ("Left", (5, 3)),
    ("Down", (5, 4)),
    ("Down", (5, 5)),
    ("Down", (5, 6)),
    ("Right", (6, 6)),
    ("Right", (7, 6))
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

# If successfully reached (7, 6), stand facing UP and try to step UP to (7, 5)
pos = get_pos()
if pos == (7, 6):
    print("At (7, 6), facing UP towards (7, 5)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Try step UP
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    pos2 = get_pos()
    print("Tried Up from (7, 6). Landed at:", pos2)
    if pos2 == (7, 5):
        print("SUCCESS: Stepped onto the platform from the south side!")
        # Step back Down
        mgba.press_buttons(["Down"])
        time.sleep(0.55)
    else:
        print("FAILED: Platform is blocked from the south side.")
