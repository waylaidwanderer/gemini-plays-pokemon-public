import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def find_left_exit():
    print("Starting left-side brute force of 1F exit from:", get_pos())
    # We are currently at (9, 7)
    
    test_columns = [7, 6, 5, 4, 3, 2]
    
    for col in test_columns:
        cx, cy = get_pos()
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
                
        # Try to walk DOWN to trigger exit
        press_and_wait("Down", 1.0)
        
        # Check if we transitioned
        nx, ny = get_pos()
        if ny > 7 or nx != col:
            print(f"SUCCESS! Transitioned outside at Column {col}! Final position: ({nx}, {ny})")
            mgba.take_screenshot()
            return True
            
    print("Failed to find exit warp on left-side columns.")
    return False

find_left_exit()
