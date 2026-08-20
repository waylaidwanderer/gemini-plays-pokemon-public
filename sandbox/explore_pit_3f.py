import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 5:
        if new_pos == pos:
            print("Did not move. Checking for direction turn, wall, or battle...")
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            
            if new_pos == pos:
                print("Still did not move. Checking for battle...")
                handle_battle()
                time.sleep(0.5)
                mgba.press_buttons([direction])
                time.sleep(0.5)
                new_pos = mgba.get_coordinates()
        else:
            print(f"We are at unexpected position {new_pos}. Retrying {direction}...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    print("Dismissing 'Got away safely!' text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Overworld coordinates:", pos)
    
    if pos == {'x': 23, 'y': 5}:
        # Walk to (24, 5) -> (24, 6) -> (25, 6) (Test for pit!)
        path = [
            ("Right", 24, 5),
            ("Down", 24, 6),
        ]
        
        success = True
        for direction, tx, ty in path:
            if not step_to(direction, tx, ty):
                print(f"Failed to reach ({tx}, {ty})!")
                success = False
                break
                
        if success:
            print("At (24, 6). Testing (25, 6) (Right) for pit drop...")
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            
            pos_test = mgba.get_coordinates()
            print("Coordinates after Right:", pos_test)
            
            if pos_test['x'] != 25 or pos_test['y'] != 6:
                print("FELL THROUGH PIT AT (25, 6)!!! Warp completed!")
                time.sleep(2.5) # Wait for landing
                
                pos_landing = mgba.get_coordinates()
                print("Landed! Current position:", pos_landing)
                mgba.take_screenshot()
            else:
                print("(25, 6) is walkable too. Walking back Left to (24, 6)...")
                mgba.press_buttons(["Left"])
                time.sleep(0.5)
                
                # Test (24, 7) (Down) for pit drop
                print("Testing (24, 7) (Down) for pit drop...")
                mgba.press_buttons(["Down"])
                time.sleep(0.5)
                
                pos_test = mgba.get_coordinates()
                print("Coordinates after Down:", pos_test)
                
                if pos_test['x'] != 24 or pos_test['y'] != 7:
                    print("FELL THROUGH PIT AT (24, 7)!!! Warp completed!")
                    time.sleep(2.5)
                    
                    pos_landing = mgba.get_coordinates()
                    print("Landed! Current position:", pos_landing)
                    mgba.take_screenshot()
                else:
                    print("(24, 7) is walkable. Taking screenshot of surroundings.")
                    mgba.take_screenshot()
    else:
        print("Unexpected overworld position!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
