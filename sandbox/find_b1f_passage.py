import mgba
import time

def walk_to(target_x, target_y):
    # Walk to target_x, target_y from current position
    # Assumes simple clear column 24 or 25
    pos = mgba.get_coordinates()
    curr_x, curr_y = pos['x'], pos['y']
    
    # If coordinates are 0,0, wait and retry
    if curr_x == 0 and curr_y == 0:
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        curr_x, curr_y = pos['x'], pos['y']
        
    print(f"Walking from ({curr_x}, {curr_y}) to ({target_x}, {target_y})...")
    
    # First, align x to column 24 or 25
    while curr_x < target_x:
        mgba.press_buttons(["Right", "sleep 350"])
        curr_x += 1
    while curr_x > target_x:
        mgba.press_buttons(["Left", "sleep 350"])
        curr_x -= 1
        
    # Then, align y
    while curr_y < target_y:
        mgba.press_buttons(["Down", "sleep 350"])
        curr_y += 1
    while curr_y > target_y:
        mgba.press_buttons(["Up", "sleep 350"])
        curr_y -= 1

def main():
    print("Testing all rows from 14 to 27 on B1F for left passage...")
    # Currently at (24, 26)
    
    for test_row in range(14, 28):
        # 1. Walk to (24, test_row)
        walk_to(24, test_row)
        
        # 2. Try to step Left to column 23
        mgba.press_buttons(["Left", "sleep 350"])
        pos = mgba.get_coordinates()
        
        # If coordinates are 0,0, wait a bit
        if pos['x'] == 0 and pos['y'] == 0:
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            
        print(f"Tested Row {test_row}: step Left -> {pos}")
        
        # 3. If we succeeded (x is 23), print and exit!
        if pos['x'] == 23:
            print(f"SUCCESS! Row {test_row} is open to the Left!")
            mgba.take_screenshot()
            return
            
        # 4. If we didn't succeed, we might have stepped somewhere else (e.g. wild battle).
        # We need to make sure we are not in battle!
        # If we got a wild battle, the script will exit and we handle it in the next turn.
        # But let's assume no battle for now, and if we are at (23, test_row) we warp back.
        # Wait, if we are at 23, we already returned. If we are at 24, we continue.

if __name__ == "__main__":
    main()
