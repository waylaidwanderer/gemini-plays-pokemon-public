import mgba
import time

def run_away():
    print("Attempting to run away from battle...")
    # Go to RUN option and press A
    mgba.press_buttons(["Right", "Down", "A", "sleep 1000", "B", "sleep 500", "B", "sleep 500"])

def clear_dialog():
    print("Clearing text boxes...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])

def walk_step(direction, target_x, target_y):
    for attempt in range(15):
        pos = mgba.get_coordinates()
        print(f"Attempt {attempt+1}: Standing at {pos}. Pressing {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == target_x and new_pos['y'] == target_y:
            print(f"Success! Reached {new_pos}")
            return True
        
        # If we didn't reach, we might be in battle, blocked by NPC, or text box open
        print(f"Did not reach target ({target_x}, {target_y}). Checking for battle/text...")
        clear_dialog()
        run_away()
        time.sleep(0.5)
        
    print(f"Failed to reach target ({target_x}, {target_y}) after 15 attempts.")
    return False

def solve_all():
    # Current is at (6, 11) on 2F in State A
    # We want to go to the switch at (2, 12)
    # Since NPC is around (4, 11) / (5, 11), let's use a path that bypasses row 11 if needed, or just try to walk.
    # Actually, let's walk through row 10 if we get blocked on row 11!
    # Let's see: we can go:
    # (6, 11) -> (6, 10) -> (5, 10) -> (4, 10) -> (3, 10) -> (3, 11) is wall.
    # So from (4, 10) we can go: (4, 11) -> (3, 11) is wall. So (4, 12) -> (3, 12) -> (2, 12).
    # Let's try the standard path first:
    path_to_nw_switch = [
        ("Left", 5, 11),
        ("Down", 5, 12),
        ("Left", 4, 12),
        ("Left", 3, 12),
        ("Down", 3, 13),
        ("Left", 2, 13),
        ("Left", 1, 13),
        ("Up", 1, 12),
        ("Up", 1, 11),
        ("Down", 1, 12),
        ("Right", 2, 12),
    ]
    
    # Let's execute the path to the NW switch
    for d, tx, ty in path_to_nw_switch:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False

    # 2. Toggle switch to State B
    print("Step 2: Toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A"])
    time.sleep(1.0)
    
    # 3. Walk to stairs in State B (via Row 11, Column 11, Row 5, Column 18)
    print("Step 3: Walking to stairs in State B...")
    path_to_stairs_b = [
        ("Right", 3, 12),
        ("Up", 3, 11),
        ("Right", 4, 11),
        ("Right", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11),
        ("Right", 11, 11),
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5), # Gate (15, 5) is OPEN in State B!
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Down", 18, 6),
        ("Down", 18, 7),
    ]
    for d, tx, ty in path_to_stairs_b:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # 4. Step Down onto (18, 8) stairs to warp to 3F in State B
    print("Step 4: Ascending to 3F in State B...")
    mgba.press_buttons(["Down"])
    time.sleep(1.2)
    print("Warp complete! Position on 3F:", mgba.get_coordinates())
    
    # 5. Walk to balcony drop on 3F (State B)
    print("Step 5: Walking to balcony drop on 3F...")
    path_to_balcony = [
        ("Up", 18, 7),
        ("Up", 18, 6),
        ("Up", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
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
    for d, tx, ty in path_to_balcony:
        if not walk_step(d, tx, ty):
            mgba.take_screenshot()
            return False
            
    # Drop to 1F!
    print("Step 6: Dropping to 1F...")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    print("Landed on 1F! Position:", mgba.get_coordinates())
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    solve_all()
