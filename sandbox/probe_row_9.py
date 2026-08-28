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

# Let's write a robust function to walk from any position to (col, 10) using Row 12 as the transit highway.
def go_to_row_10_col(target_col):
    # 1. Get to Row 12 first
    pos = get_pos()
    while pos[1] < 12:
        pos = step("Down")
    while pos[1] > 12:
        pos = step("Up")
        
    # 2. Walk horizontally on Row 12 to target_col
    pos = get_pos()
    while pos[0] < target_col:
        pos = step("Right")
    while pos[0] > target_col:
        pos = step("Left")
        
    # 3. Walk Up to Row 10
    pos = get_pos()
    while pos[1] > 10:
        pos = step("Up")
        
    return get_pos() == (target_col, 10)

print("Starting robust Row 9 probe...")
open_columns = []

# Probe columns 1, 3, 4, 5, 6, 7, 8 (Column 2 is blocked by Mewtwo statue)
columns_to_test = [1, 3, 4, 5, 6, 7, 8]

for col in columns_to_test:
    print(f"Moving to Column {col}...")
    if not go_to_row_10_col(col):
        print(f"Failed to reach Column {col} Row 10!")
        continue
        
    # Try to step UP to (col, 9)
    print(f"Testing Column {col} Row 9...")
    old_pos = get_pos()
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
