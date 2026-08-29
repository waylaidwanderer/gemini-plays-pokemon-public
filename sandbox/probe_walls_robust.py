import mgba
import time

def handle_battle_if_present():
    print("Checking/handling battle...")
    # Standard battle escape sequence
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def move_safe(step):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([step])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        # We didn't move! We might be in a battle.
        print(f"We didn't move on step '{step}'. Attempting battle escape...")
        handle_battle_if_present()
        # Try moving again
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
    return pos_after

def probe_all_row_9():
    print(f"Starting robust probe from: {mgba.get_coordinates()}")
    
    columns_to_test = [1, 3, 4, 6, 7]
    results = {}
    
    for col in columns_to_test:
        pos = mgba.get_coordinates()
        print(f"Testing Column {col}. Current pos: {pos}")
        
        # 1. Move to Row 11 first
        while pos['y'] < 11:
            pos = move_safe("Down")
        while pos['y'] > 11:
            pos = move_safe("Up")
            
        # 2. Move horizontally to target column
        while pos['x'] < col:
            pos = move_safe("Right")
        while pos['x'] > col:
            pos = move_safe("Left")
            
        # 3. Move UP to Row 10
        pos = move_safe("Up")
        if pos['y'] != 10:
            print(f"Error: Failed to reach Row 10 on Column {col}. Current pos: {pos}")
            continue
            
        # 4. Attempt to step UP to Row 9
        pos_test = move_safe("Up")
        if pos_test['y'] == 9:
            results[col] = "OPEN"
            print(f"Column {col} Row 9 is OPEN!")
            # Step back down to Row 10
            move_safe("Down")
        else:
            results[col] = "CLOSED"
            print(f"Column {col} Row 9 is CLOSED.")
            
    print("\n--- FINAL PROBE RESULTS ---")
    for col, status in results.items():
        print(f"Column {col} Row 9: {status}")

probe_all_row_9()
