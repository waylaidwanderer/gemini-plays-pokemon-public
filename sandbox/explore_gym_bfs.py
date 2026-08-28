import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def walk_to(target_pos):
    pos = get_pos()
    # Very simple deterministic routing for bottom-left room (columns 4-7, rows 11-13)
    # Target is (tx, ty)
    tx, ty = target_pos
    
    # 1. First align horizontally on Row 13 to tx
    while pos[0] < tx:
        mgba.press_buttons(["Right"])
        time.sleep(0.55)
        pos = get_pos()
    while pos[0] > tx:
        mgba.press_buttons(["Left"])
        time.sleep(0.55)
        pos = get_pos()
        
    # 2. Then align vertically to ty
    while pos[1] < ty:
        mgba.press_buttons(["Down"])
        time.sleep(0.55)
        pos = get_pos()
    while pos[1] > ty:
        mgba.press_buttons(["Up"])
        time.sleep(0.55)
        pos = get_pos()
        
    return pos == target_pos

def test_up_from(col):
    # Walk to (col, 11)
    if not walk_to((col, 11)):
        print(f"Failed to walk to ({col}, 11)")
        return False
        
    print(f"At ({col}, 11), testing UP to Row 10...")
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    pos = get_pos()
    print(f"Tried Up from ({col}, 11). Landed at: {pos}")
    
    # If we successfully walked, step back Down
    if pos == (col, 10):
        mgba.press_buttons(["Down"])
        time.sleep(0.55)
        return "walk"
    elif pos != (col, 11):
        print(f"SPUN from ({col}, 11) Up to {pos}!")
        return f"spin_to_{pos}"
    return "blocked"

# Starting at (4, 13)
print("Starting Row 10 probe from:", get_pos())

# Test Up from Columns 4, 5, 6, 7 on Row 11
results = {}
for col in [4, 5, 6, 7]:
    results[col] = test_up_from(col)
    
print("Row 10 probe results:", results)

# Walk back to (4, 13)
walk_to((4, 13))
print("Finished. Final position:", get_pos())
