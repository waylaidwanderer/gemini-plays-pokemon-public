import mgba
import time

def handle_battle():
    print("Encountered battle or text! Attempting to escape/dismiss...")
    mgba.press_buttons(["B", "sleep 300", "Down", "sleep 100", "Right", "sleep 100", "A", "sleep 1000", "B"])

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"Current pos: {pos}. Pressing {direction} to reach ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 10:
        if new_pos == pos:
            # Check if we merely turned in place (Gen 1 turning mechanics)
            print("Did not move. Retrying once to handle turning in place...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Still did not move. Checking for battle or text...")
                handle_battle()
                time.sleep(0.5)
                mgba.press_buttons([direction])
                time.sleep(0.4)
                new_pos = mgba.get_coordinates()
        else:
            print(f"Unexpected position {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def follow_path(path):
    for d, tx, ty in path:
        if not step_to(d, tx, ty):
            print(f"Failed to move to ({tx}, {ty}).")
            mgba.take_screenshot()
            return False
    return True

def main():
    print("Currently at:", mgba.get_coordinates())
    
    # Path to West Wing (2, 12) bypassing all obstacles on 3F (State B)
    path = [
        ("Up", 12, 11),
        ("Up", 12, 10),
        ("Left", 11, 10),
        ("Left", 10, 10),
        ("Left", 9, 10),
        ("Down", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Up", 7, 10),
        ("Left", 6, 10),
        ("Left", 5, 10),
        ("Left", 4, 10),
        ("Left", 3, 10),
        ("Left", 2, 10),
        ("Down", 2, 11),
        ("Down", 2, 12),
    ]
    
    print("Walking to west wing (2, 12)...")
    if not follow_path(path):
        return
        
    print("Reached west wing! Now exploring balcony door...")
    # From (2, 12), try walking Down to (2, 14)
    path_to_balcony = [
        ("Down", 2, 13),
        ("Down", 2, 14),
    ]
    if follow_path(path_to_balcony):
        print("At (2, 14). Walking Right to find the balcony doorway...")
        # Walk Right as far as possible (we want to reach column 15/16/17 where the door might be)
        for i in range(15):
            print(f"Step {i+1}: Trying Right...")
            pos_before = mgba.get_coordinates()
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
            pos_after = mgba.get_coordinates()
            print("Position:", pos_after)
            if pos_after == pos_before:
                # Blocked. Let's try to walk Down to enter the balcony if we are at column 15/16/17!
                print("Blocked walking Right. Trying Down to enter balcony...")
                mgba.press_buttons(["Down"])
                time.sleep(0.5)
                pos_down = mgba.get_coordinates()
                print("Position down:", pos_down)
                if pos_down['y'] != pos_before['y']:
                    # We walked Down! Let's check if we dropped or are on the balcony
                    print("Successfully walked Down! Landed/Moved to:", pos_down)
                    mgba.take_screenshot()
                    break
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
