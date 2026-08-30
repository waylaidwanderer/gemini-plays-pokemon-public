import mgba
import time

def check_warp():
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}")
    
    # Try pressing Up
    print("Pressing Up...")
    mgba.press_buttons(["Up"])
    time.sleep(0.6)
    new_pos = mgba.get_coordinates()
    print(f"Position after Up: {new_pos}")
    if new_pos['x'] != pos['x'] or new_pos['y'] != pos['y']:
        print("Warp triggered by Up!")
        mgba.take_screenshot()
        return True
        
    # If we didn't warp, we might have walked to (22, 0) or remained at (22, 1)
    # Let's walk back to (22, 1) if we moved to (22, 0)
    pos = mgba.get_coordinates()
    if pos['y'] == 0:
        print("Moving back to (22, 1)...")
        mgba.press_buttons(["Down"])
        time.sleep(0.6)
    
    pos = mgba.get_coordinates()
    # Try pressing Down
    print("Pressing Down...")
    mgba.press_buttons(["Down"])
    time.sleep(0.6)
    new_pos = mgba.get_coordinates()
    print(f"Position after Down: {new_pos}")
    if new_pos['x'] != pos['x'] or new_pos['y'] != pos['y']:
        print("Warp triggered by Down!")
        mgba.take_screenshot()
        return True
        
    mgba.take_screenshot()
    return False

check_warp()
