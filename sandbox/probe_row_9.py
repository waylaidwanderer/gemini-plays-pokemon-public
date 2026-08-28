import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def test_up(col):
    # Walk to (col, 10)
    pos = get_pos()
    while pos[0] < col:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        pos = get_pos()
    while pos[0] > col:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos = get_pos()
    while pos[1] < 10:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        pos = get_pos()
    while pos[1] > 10:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = get_pos()
        
    print(f"Standing at {pos}. Trying to step UP to Row 9...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    new_pos = get_pos()
    if new_pos[1] == 9:
        print(f"SUCCESS: Column {col} Row 9 is OPEN! Reached {new_pos}")
        # Step back Down
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        return True
    else:
        print(f"FAILED: Column {col} Row 9 is CLOSED.")
        return False

# Ensure we are at (1, 10)
print("Starting Row 9 probe from current:", get_pos())

# Test Column 1, 2, 4, 5, 6 on Row 9
results = {}
for col in [1, 2, 4, 5, 6]:
    results[col] = test_up(col)
    
print("Probe complete. Results:", results)
