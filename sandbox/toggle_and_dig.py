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
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Attempting to escape battle or clear text...")
        handle_battle()
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("Retrying movement step...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            
    return new_pos['x'] == tx and new_pos['y'] == ty

def follow_path(path):
    for d, tx, ty in path:
        attempts = 0
        while not step_to(d, tx, ty):
            attempts += 1
            if attempts > 5:
                print(f"Failed to move to ({tx}, {ty}) after 5 attempts.")
                mgba.take_screenshot()
                return False
    return True

def toggle_and_dig():
    print("Starting western switch toggle to State B...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # We are at (7, 11) on 3F. Walk to (2, 12)
    path = [
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
        ("Down", 3, 12),
        ("Left", 2, 12),
    ]
    if not follow_path(path):
        return False
        
    # Toggle switch to State B
    print("At (2, 12). Toggling western switch to State B...")
    mgba.press_buttons(["Up", "sleep 300", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Position after toggle:", pos)
    mgba.take_screenshot()
    
    # Use DIG using Paras (TRUFFLE)
    print("Opening menu to use DIG...")
    # Menu -> Pokémon -> TRUFFLE (second or third? usually second) -> DIG
    # Let's do it safely: press Start, sleep, A to open menu
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    # Cursor is on POKeMON by default if we used it last, or we can move there.
    # Let's write a dedicated python block to select DIG!
    return True

if __name__ == "__main__":
    toggle_and_dig()
