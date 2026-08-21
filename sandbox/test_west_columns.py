import mgba
import time

def test_west_columns():
    print("Testing West-side columns 1, 2, 3, 5 for vertical traversal across row 9...")
    
    # Current position is (10, 4)
    # Walk Down to (10, 11)
    for _ in range(7):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Reached bypass landing: {mgba.get_coordinates()}")
    
    # Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"Reached (3, 11): {mgba.get_coordinates()}")
    
    results = {}
    
    # 1. Test Column 3:
    print("Testing Column 3 UP...")
    reached_y = 11
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
        pos = mgba.get_coordinates()
        if pos['y'] < reached_y:
            reached_y = pos['y']
        else:
            break
    results[3] = reached_y
    print(f"Column 3: reached y={reached_y}")
    
    # Walk back down if needed
    if reached_y < 11:
        for _ in range(11 - reached_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
            
    # 2. Test Column 2:
    print("Testing Column 2 UP...")
    # Walk to (2, 11) (Wait, (2, 11) has the Mewtwo statue! But let's see if we can stand on (2, 12) or (2, 11))
    mgba.press_buttons(["Down"]) # to row 12
    time.sleep(0.05)
    mgba.press_buttons(["Left"]) # to col 2
    time.sleep(0.05)
    print(f"At (2, 12): {mgba.get_coordinates()}")
    
    reached_y = 12
    for _ in range(6):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
        pos = mgba.get_coordinates()
        if pos['y'] < reached_y:
            reached_y = pos['y']
        else:
            break
    results[2] = reached_y
    print(f"Column 2: reached y={reached_y}")
    
    # Walk back down if needed
    if reached_y < 11:
        for _ in range(11 - reached_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
            
    # 3. Test Column 1:
    # From (2, 12) or (2, 11): walk Left to Column 1 (Row 12 is open, or Row 11)
    print("Testing Column 1 UP...")
    pos = mgba.get_coordinates()
    if pos['y'] == 11:
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    else:
        # We are at (2, 12), walk Left to (1, 12)
        mgba.press_buttons(["Left"])
        time.sleep(0.05)
    print(f"At Column 1: {mgba.get_coordinates()}")
    
    reached_y = mgba.get_coordinates()['y']
    start_y = reached_y
    for _ in range(7):
        mgba.press_buttons(["Up"])
        time.sleep(0.05)
        pos = mgba.get_coordinates()
        if pos['y'] < reached_y:
            reached_y = pos['y']
        else:
            break
    results[1] = reached_y
    print(f"Column 1: reached y={reached_y}")
    
    # Walk back down if needed
    if reached_y < 11:
        for _ in range(11 - reached_y):
            mgba.press_buttons(["Down"])
            time.sleep(0.05)
            
    print("\n--- Summary of West Columns ---")
    for col, y in results.items():
        print(f"Column {col}: reached y={y}")

test_west_columns()
