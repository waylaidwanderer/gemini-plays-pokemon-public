import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def find_exit_brute_force():
    print("Starting brute force of 1F exit from:", get_pos())
    # We are currently at (8, 7)
    
    # We will test columns: 8, 9, 7, 6, 5, 4, 14, 15
    # For each column, we walk to that column on Row 7, and try to walk DOWN.
    # If the map transition happens, the position will warp to Celadon City (around 10, 14).
    # Since Celadon City map is different, we check if get_pos() returns x around 10 or similar,
    # or if get_pos() y coordinate changes to 14 or similar.
    # Actually, if we warp, the coordinates will change, so we can detect it easily!
    
    test_columns = [8, 9, 7, 6, 5, 4, 14, 15]
    
    for col in test_columns:
        cx, cy = get_pos()
        # If we already transitioned, we will notice coordinates changed drastically
        if cy > 7 or cx < 0 or cx > 20:
            print("Successfully transitioned outside!")
            return True
            
        print(f"Testing Column {col} on Row 7...")
        # Walk horizontally on Row 7 to 'col'
        steps = col - cx
        if steps != 0:
            btn = "Right" if steps > 0 else "Left"
            for _ in range(abs(steps)):
                press_and_wait(btn)
                
        # Now we are at (col, 7). Let's try to walk DOWN
        press_and_wait("Down", 1.0)
        
        # Check if we transitioned
        nx, ny = get_pos()
        if ny > 7 or nx != col:
            print(f"SUCCESS! Transitioned outside at Column {col}! Final position: ({nx}, {ny})")
            mgba.take_screenshot()
            return True
            
    print("Failed to find exit warp on tested columns.")
    return False

find_exit_brute_force()
