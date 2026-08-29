import mgba
import time

def handle_battle_if_present():
    print("Checking/handling battle...")
    # Standard battle escape sequence
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def move_safe(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving '{step}' to target ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
        if pos_before == pos_after:
            print("Did not move. Checking battle...")
            handle_battle_if_present()
        else:
            print(f"Moved to unexpected position: {pos_after}. Checking battle...")
            handle_battle_if_present()
        
        print(f"Retrying move '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    print(f"Success! Arrived at: {pos_after}")
    return pos_after

def main():
    # We are at (1, 10)
    pos = mgba.get_coordinates()
    print(f"Starting pos: {pos}")
    
    # 1. Walk up to (1, 8)
    pos = move_safe("Up", 1, 9)
    pos = move_safe("Up", 1, 8)
    
    # 2. Try walking Right on Row 8 to see how far we can go!
    for x in range(2, 22):
        print(f"Attempting to move Right to Column {x} Row 8...")
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        
        if pos_before == pos_after:
            # We didn't move! Could be a battle, or a wall.
            # Let's check if we can run away
            print("Didn't move. Checking if battle...")
            handle_battle_if_present()
            pos_test = mgba.get_coordinates()
            if pos_test == pos_before:
                # Still didn't move! It's a wall.
                print(f"BUMPED! Wall detected at Column {x} Row 8.")
                break
        else:
            print(f"Moved to: {pos_after}")
            
if __name__ == "__main__":
    main()
