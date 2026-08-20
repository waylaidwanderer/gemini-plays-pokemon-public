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
    print("Testing 3F balcony shutter gates at (24, 13)...")
    
    # We are currently at (28, 12)
    # 1. Walk Left to (24, 12)
    path = [
        ("Left", 27, 12),
        ("Left", 26, 12),
        ("Left", 25, 12),
        ("Left", 24, 12),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("At (24, 12). Attempting to move Down to (24, 13)...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        print("Coordinates after attempting Down:", pos)
        
        if pos == {'x': 24, 'y': 13}:
            print("SHUTTER GATE IS OPEN!!! Moving to balcony drop...")
            if step_to("Down", 24, 14):
                print("At (24, 14). Dropping off balcony...")
                mgba.press_buttons(["Left"])
                time.sleep(3.0)
                
                landing_pos = mgba.get_coordinates()
                print("Landed on 1F! Current position:", landing_pos)
                mgba.take_screenshot()
        else:
            print("SHUTTER GATE IS CLOSED! We cannot pass here.")
            mgba.take_screenshot()
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
