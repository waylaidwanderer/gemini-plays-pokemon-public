import mgba
import time

def handle_battle():
    # If we get into a battle during the script, escape it
    print("Encountered battle! Fleeing...")
    # Advance text
    mgba.press_buttons(["B", "sleep 500", "B", "sleep 500", "B", "sleep 500"])
    # Run away
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 2000"])
    # Check if we got away safely
    pos = mgba.get_coordinates()
    print("Coordinates after fleeing attempt:", pos)
    mgba.press_buttons(["B", "sleep 500"]) # Dismiss text

def walk_step(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction, "sleep 150"])
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 2:
        if new_pos == pos:
            print("Did not move. Retrying direction...")
            mgba.press_buttons([direction, "sleep 150"])
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # We might be in a battle! Check if screen changed
                print(f"Blocked moving {direction} from {pos}. Possibly in battle.")
                return False
        else:
            print(f"Unexpected pos {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction, "sleep 150"])
            new_pos = mgba.get_coordinates()
        attempts += 1
    return new_pos == {'x': tx, 'y': ty}

def main():
    pos = mgba.get_coordinates()
    print("Starting ultimate victory script. Position:", pos)
    
    # Step 1: Use DIG to exit mansion and reset switch state to State A
    print("Using DIG to exit the mansion...")
    # Open Menu
    mgba.press_buttons(["Start", "sleep 400"])
    # Go down to PKMN
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    # Select TRUFFLE (Paras) - usually 2nd PKMN
    mgba.press_buttons(["Down", "sleep 200", "A", "sleep 500"])
    # Select DIG (Option 1)
    mgba.press_buttons(["A", "sleep 3000"]) # Wait for DIG animation to complete and overworld to load
    
    pos = mgba.get_coordinates()
    print("Landed outside Cinnabar Pokémon Center! Position:", pos)
    
    # Step 2: Walk to Mansion entrance at (6, 3)
    # Cinnabar Pokémon Center door is at (11, 11). We step Down to (11, 12) on landing.
    path_to_mansion = [
        ("Left", 10, 12), ("Left", 9, 12), ("Left", 8, 12), ("Left", 7, 12), ("Left", 6, 12),
        ("Up", 6, 11), ("Up", 6, 10), ("Up", 6, 9), ("Up", 6, 8), ("Up", 6, 7), ("Up", 6, 6), ("Up", 6, 5), ("Up", 6, 4),
        ("Up", 6, 3) # Enter Mansion!
    ]
    for d, tx, ty in path_to_mansion:
        if not walk_step(d, tx, ty):
            print("Failed on way to Mansion entrance!")
            mgba.take_screenshot()
            return
            
    time.sleep(2.0) # Wait for Mansion to load
    pos = mgba.get_coordinates()
    print("Entered Mansion! Position (should be 1F 5, 27):", pos)
    
    # Step 3: Walk to 2F stairs at (7, 10) on 1F
    # In State A, the central barriers are closed, but the corridor is walkable to the stairs.
    # From (5, 27) on 1F:
    path_to_2f_stairs = [
        ("Right", 6, 27), ("Right", 7, 27),
        ("Up", 7, 26), ("Up", 7, 25), ("Up", 7, 24), ("Up", 7, 23), ("Up", 7, 22), ("Up", 7, 21), ("Up", 7, 20), ("Up", 7, 19), ("Up", 7, 18), ("Up", 7, 17), ("Up", 7, 16), ("Up", 7, 15), ("Up", 7, 14), ("Up", 7, 13), ("Up", 7, 12), ("Up", 7, 11),
        ("Up", 7, 10) # Ascend to 2F!
    ]
    for d, tx, ty in path_to_2f_stairs:
        if not walk_step(d, tx, ty):
            print("Failed on way to 2F stairs!")
            mgba.take_screenshot()
            return
            
    time.sleep(2.0) # Wait for 2F to load
    pos = mgba.get_coordinates()
    print("Landed on 2F! Position (should be 7, 11):", pos)
    
    # Step 4: Walk straight to 3F stairs at (7, 10) on 2F
    # In State A, the stairs gate at (5, 7) is open, so we can walk directly.
    # From (7, 11) on 2F:
    path_to_3f_stairs = [
        ("Up", 7, 10) # Ascend to 3F!
    ]
    for d, tx, ty in path_to_3f_stairs:
        if not walk_step(d, tx, ty):
            print("Failed on way to 3F stairs!")
            mgba.take_screenshot()
            return
            
    time.sleep(2.0) # Wait for 3F to load
    pos = mgba.get_coordinates()
    print("Landed on 3F! Position (should be 7, 11):", pos)
    
    # Step 5: Walk straight to the switch at (12, 11) on 3F
    # In State A, the column 10 gate is open!
    # From (7, 11) on 3F:
    path_to_switch = [
        ("Right", 8, 11), ("Right", 9, 11), ("Right", 10, 11), ("Right", 11, 11)
    ]
    for d, tx, ty in path_to_switch:
        if not walk_step(d, tx, ty):
            print("Failed on way to the 3F switch!")
            mgba.take_screenshot()
            return
            
    print("At 3F switch landing (11, 11)! Facing Right...")
    mgba.press_buttons(["Right", "sleep 300"])
    
    # Toggle switch to State B
    print("Toggling 3F switch at (12, 11) to State B...")
    mgba.press_buttons(["A", "sleep 500", "A", "sleep 500", "B", "sleep 500"])
    print("Switch toggled!")
    
    # Step 6: Walk to the pit at (25, 6) on 3F in State B
    path_to_pit = [
        ("Right", 12, 11),
        ("Up", 12, 10), ("Up", 12, 9), ("Up", 12, 8), ("Up", 12, 7), ("Up", 12, 6),
        ("Right", 13, 6), ("Right", 14, 6), ("Right", 15, 6), ("Right", 16, 6), ("Right", 17, 6), ("Right", 18, 6), ("Right", 19, 6), ("Right", 20, 6), ("Right", 21, 6),
        ("Up", 21, 5), ("Up", 21, 4), ("Up", 21, 3), # Gate at (21, 5) is OPEN in State B!
        ("Right", 22, 3), ("Right", 23, 3), ("Right", 24, 3), ("Right", 25, 3), ("Right", 26, 3),
        ("Down", 26, 4), ("Down", 26, 5), ("Down", 26, 6)
    ]
    for d, tx, ty in path_to_pit:
        if not walk_step(d, tx, ty):
            print("Failed on way to the pit!")
            mgba.take_screenshot()
            return
            
    print("At (26, 6). Stepping Left into the pit...")
    mgba.press_buttons(["Left", "sleep 4000"]) # Wait for falling animation
    
    final_pos = mgba.get_coordinates()
    print("Landed on 1F fenced area! Position:", final_pos)
    mgba.take_screenshot()
    
    # Step 7: Walk Up into B1F stairs on 1F
    print("Walking onto B1F stairs...")
    mgba.press_buttons(["Up", "sleep 250", "Up", "sleep 250", "Up", "sleep 250", "Up", "sleep 250", "Up", "sleep 2000"])
    
    final_pos = mgba.get_coordinates()
    print("Landed on B1F! Position:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
