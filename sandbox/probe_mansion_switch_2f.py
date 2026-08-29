import mgba
import time

def test_statue_2f(y):
    current_pos = mgba.get_coordinates()
    print(f"Moving to (12, {y}) facing Right...")
    
    # Walk to (12, y)
    if y > current_pos['y']:
        for _ in range(y - current_pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.2)
    elif y < current_pos['y']:
        for _ in range(current_pos['y'] - y):
            mgba.press_buttons(["Up"])
            time.sleep(0.2)
            
    # Face Right
    mgba.press_buttons(["Right"])
    time.sleep(0.2)
    
    # Press A
    print(f"Pressing A at {mgba.get_coordinates()} facing Right...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Dismiss any text box
    mgba.press_buttons(["B"])
    time.sleep(0.2)

# We are at (12, 8). Let's test the statue at (13, 9) by standing at (12, 9)
test_statue_2f(9)

# Let's test the statue at (13, 11) by standing at (12, 11)
test_statue_2f(11)
