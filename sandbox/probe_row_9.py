import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    return get_pos()

# We are currently at (1, 10). Let's probe all Columns from 1 to 8 on Row 10
# and try to step Up to Row 9 for each column!

print("Starting Row 9 probe...")
open_columns = []

for col in range(1, 9):
    # Walk to (col, 10)
    pos = get_pos()
    current_col = pos[0]
    
    if current_col < col:
        for _ in range(col - current_col):
            step("Right")
    elif current_col > col:
        for _ in range(current_col - col):
            step("Left")
            
    # Verify we are at (col, 10)
    pos = get_pos()
    if pos != (col, 10):
        print(f"Could not reach ({col}, 10), current pos: {pos}")
        continue
        
    # Try to step UP to (col, 9)
    print(f"Testing Column {col} Row 9...")
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    new_pos = get_pos()
    if new_pos[1] == 9:
        print(f"SUCCESS: Column {col} Row 9 is OPEN!")
        open_columns.append(col)
        # Step back down to Row 10
        step("Down")
    else:
        print(f"Column {col} Row 9 is CLOSED.")

print("Probe completed! Open columns on Row 9:", open_columns)
