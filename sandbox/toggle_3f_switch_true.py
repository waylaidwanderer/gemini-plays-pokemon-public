import mgba
import time
import os

def cleanup_files():
    print("Cleaning up obsolete scripts...")
    files_to_delete = [
        "explore_east_road.py",
        "heal_and_clear.py",
        "heal_at_center.py",
        "exit_and_heal.py",
        "toggle_3f_switch.py",
        "run_to_mansion_drop.py"
    ]
    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"Deleted {f}")
            except Exception as e:
                print(f"Failed to delete {f}: {e}")

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
            print("Did not move. Checking for battle or text...")
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
    cleanup_files()
    
    print("Currently at:", mgba.get_coordinates())
    
    # 1. Walk from (8, 13) to (11, 11)
    path_to_switch = [
        ("Right", 9, 13),
        ("Right", 10, 13),
        ("Right", 11, 13),
        ("Up", 11, 12),
        ("Up", 11, 11),
    ]
    
    print("Walking to (11, 11) to face 3F switch...")
    if not follow_path(path_to_switch):
        return
        
    # 2. Face Right towards the statue at (12, 11) and toggle
    print("Standing at (11, 11). Facing Right and pressing A...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # Check if we see the switch dialogue by pressing A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Select YES to toggle, dismiss dialogue
    print("Selecting YES to secret switch...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(2.0)
    
    # 3. Walk to the balcony drop at (24, 14) via Row 5 (State B is active now)
    path_to_balcony = [
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate is OPEN in State B!
        ("Right", 22, 5),
        ("Right", 23, 5),
        ("Right", 24, 5),
        ("Down", 24, 6),
        ("Down", 24, 7),
        ("Down", 24, 8),
        ("Down", 24, 9),
        ("Down", 24, 10),
        ("Down", 24, 11),
        ("Down", 24, 12),
        ("Down", 24, 13),
        ("Down", 24, 14),
    ]
    
    print("Walking to 3F balcony drop...")
    if not follow_path(path_to_balcony):
        return
        
    print("At (24, 14). Dropping off the balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop animation/warp
    
    pos = mgba.get_coordinates()
    print("Landed! Coordinates:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
