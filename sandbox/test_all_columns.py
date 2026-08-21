import mgba
import time

def test_columns():
    print("Systematically testing all columns (1-8) for vertical traversal across row 9...")
    
    # 1. Walk from current position (10, 6) down to (10, 11)
    for _ in range(5):
        mgba.press_buttons(["Down"])
        time.sleep(0.05)
    print(f"Starting at: {mgba.get_coordinates()}")
    
    results = {}
    
    # Test each column from 8 down to 1
    for col in range(8, 0, -1):
        # Move horizontally along row 11 to 'col'
        curr_x = mgba.get_coordinates()['x']
        steps = col - curr_x
        if steps > 0:
            for _ in range(steps):
                mgba.press_buttons(["Right"])
                time.sleep(0.05)
        elif steps < 0:
            for _ in range(-steps):
                mgba.press_buttons(["Left"])
                time.sleep(0.05)
                
        # Now we are at (col, 11). Try to walk UP as far as possible (up to row 7)
        reached_y = 11
        for _ in range(4): # Try to walk up 4 steps (from 11 to 7)
            mgba.press_buttons(["Up"])
            time.sleep(0.05)
            pos = mgba.get_coordinates()
            if pos['y'] < reached_y:
                reached_y = pos['y']
            else:
                break # Blocked!
                
        results[col] = reached_y
        print(f"Column {col}: reached y={reached_y}")
        
        # Walk back down to row 11 if we moved up
        if reached_y < 11:
            for _ in range(11 - reached_y):
                mgba.press_buttons(["Down"])
                time.sleep(0.05)
                
    print("\n--- Summary of Columns (1-8) Traversal ---")
    for col, y in results.items():
        print(f"Column {col}: reached y={y}")

test_columns()
