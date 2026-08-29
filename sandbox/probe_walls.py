import mgba
import time

def probe_row_9_gates():
    print(f"Starting probe from: {mgba.get_coordinates()}")
    
    # We will test columns 1, 3, 4, 6, 7
    columns_to_test = [1, 3, 4, 6, 7]
    results = {}
    
    for col in columns_to_test:
        # Move to (col, 11)
        # First go down to Row 11
        pos = mgba.get_coordinates()
        if pos['y'] != 11:
            # Move to Row 11
            dy = 11 - pos['y']
            step = "Down" if dy > 0 else "Up"
            for _ in range(abs(dy)):
                mgba.press_buttons([step])
                time.sleep(0.3)
                
        # Now move horizontally to col
        pos = mgba.get_coordinates()
        dx = col - pos['x']
        step = "Right" if dx > 0 else "Left"
        for _ in range(abs(dx)):
            mgba.press_buttons([step])
            time.sleep(0.3)
            
        # Now move UP to Row 10
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
        # Verify we are at (col, 10)
        pos = mgba.get_coordinates()
        if pos['x'] != col or pos['y'] != 10:
            print(f"Error: Could not reach ({col}, 10), current pos: {pos}")
            continue
            
        # Attempt to step UP to Row 9
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
        pos_after = mgba.get_coordinates()
        if pos_after['y'] == 9:
            results[col] = "OPEN"
            # Step back down to Row 10
            mgba.press_buttons(["Down"])
            time.sleep(0.3)
        else:
            results[col] = "CLOSED"
            
    print("PROBE RESULTS:")
    for col, status in results.items():
        print(f"Column {col} Row 9: {status}")

probe_row_9_gates()
