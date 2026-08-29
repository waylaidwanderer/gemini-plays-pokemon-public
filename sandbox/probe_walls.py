import mgba
import time

def test_wall(y):
    current_pos = mgba.get_coordinates()
    print(f"Moving to (1, {y}) facing Left...")
    
    # Walk to (1, y)
    if y > current_pos['y']:
        for _ in range(y - current_pos['y']):
            mgba.press_buttons(["Down"])
            time.sleep(0.2)
    elif y < current_pos['y']:
        for _ in range(current_pos['y'] - y):
            mgba.press_buttons(["Up"])
            time.sleep(0.2)
            
    # Face Left
    mgba.press_buttons(["Left"])
    time.sleep(0.2)
    
    # Press A
    print(f"Pressing A at {mgba.get_coordinates()} facing Left...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Dismiss any text box
    mgba.press_buttons(["B"])
    time.sleep(0.2)

# Test left wall interactions on Rows 10, 11, 12, 13
test_wall(10)
test_wall(11)
test_wall(12)
test_wall(13)
