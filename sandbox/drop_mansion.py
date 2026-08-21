import mgba
import time

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print(f"BUMPED at {pos_before} going {direction}")
    else:
        print(f"Moved to {pos_after}")
    return pos_after

# Starting from (20, 15) on 3F East (State B)
pos = mgba.get_coordinates()
print("Starting position on 3F East:", pos)

# We want to find the exact drop tile by trying Column 19, 18, 17, 20, 21 on Row 15
cols_to_test = [19, 18, 20, 21]

for col in cols_to_test:
    print(f"\n--- Testing Column {col} on Row 15 ---")
    pos = mgba.get_coordinates()
    
    # 1. Walk to Column `col` on Row 15
    while pos['x'] > col:
        pos = walk_step("Left")
    while pos['x'] < col:
        pos = walk_step("Right")
        
    pos = mgba.get_coordinates()
    if pos['x'] == col and pos['y'] == 15:
        # 2. Try walking DOWN to Row 16 (the drop/ledge)
        print(f"Attempting to walk Down from ({col}, 15)...")
        pos_before = pos
        pos = walk_step("Down")
        
        # Check if we successfully walked down or dropped (warped)
        if pos != pos_before:
            print(f"Successfully moved/dropped! New position: {pos}")
            # If we warped/dropped, the script will exit
            if abs(pos['y'] - pos_before['y']) > 2 or pos['y'] >= 16:
                print("DROP DETECTED! We have dropped to B1F!")
                break
        else:
            print(f"Column {col} Row 15 is blocked going Down.")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
