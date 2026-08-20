import mgba
import time

def step_to_test(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Attempting to move {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Pressing direction again...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        
    print(f"Result position: {new_pos}")
    return new_pos['x'] == tx and new_pos['y'] == ty

def main():
    print("Testing south-west balcony access at Columns 4-7, Row 27...")
    pos = mgba.get_coordinates()
    print("Starting position:", pos)
    
    # 1. Walk from (2, 26) to (5, 27)
    path = [
        ("Right", 3, 26),
        ("Right", 4, 26),
        ("Right", 5, 26),
        ("Down", 5, 27),
    ]
    for d, tx, ty in path:
        if not step_to_test(d, tx, ty):
            print("Failed to reach (5, 27).")
            mgba.take_screenshot()
            return
            
    # 2. Try walking Down to Row 28
    print("Trying to walk Down from (5, 27) to Row 28...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    print("Position after Down:", pos_after)
    
    if pos_after == pos_before:
        print("Blocked! (5, 27) Down is blocked.")
        mgba.take_screenshot()
    else:
        print("SUCCESS! Position changed to:", pos_after)
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
