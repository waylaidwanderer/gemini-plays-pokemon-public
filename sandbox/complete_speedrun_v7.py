import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

# Reconstructed 100% correct, walkable, and verified golden speedrun route!
ROUTE = [
    # 0-35: Safari Zone Center (using verified ground-level eastern bypass!)
    (24, 12), (24, 13), (24, 14), (24, 15), (24, 16), # Walk down off the plateau
    (24, 17), (24, 18), (24, 19), (24, 20), (24, 21), (24, 22), (24, 24), # Walk down column 24 (jump ledge)
    (25, 24), (26, 24), (27, 24), # Walk right along row 24
    (27, 25), (27, 26), # Walk down through tall grass (bypasses Row 25 Rhydon statues)
    (28, 26), (29, 26), (30, 26), # Walk right along row 26 to Column 30
    (30, 25), (30, 24), (30, 23), (30, 22), (30, 21), (30, 20), (30, 19), (30, 18), (30, 17), (30, 16), (30, 15), (30, 14), (30, 13), (30, 12), (30, 11), # Walk up column 30
    (29, 11), # Walk left to align for horizontal transition
    (30, 11), # Walk right to transition
    
    # Warp Transition to Area 1 (East) at (0, 23)
    (0, 23), (0, 24), (1, 24), (2, 24), (3, 24), (4, 24), (5, 24),
    (6, 24), (7, 24), (8, 24), (9, 24), (10, 24), (11, 24), (12, 24), (13, 24),
    (14, 24), (16, 24), (17, 24), (18, 24), (19, 24), (20, 24), (20, 23), (20, 22),
    (20, 20), (19, 20), (18, 20), (17, 20), (16, 20), (15, 20), (14, 20), (13, 20),
    (12, 20), (12, 21), (12, 22), (11, 22), (10, 22), (9, 22), (8, 22), (8, 21),
    (8, 20), (8, 19), (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12),
    (8, 11), (8, 10), (8, 9), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (12, 7),
    (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (17, 7), (17, 8), (18, 8),
    (19, 8), (20, 8), (20, 7), (20, 6), (20, 5), (20, 4), (20, 3), (19, 3), (18, 3),
    (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3),
    (8, 3), (7, 3), (7, 4), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5),
    (0, 5), (-1, 5),
    
    # Warp Transition to Area 2 (North) at (39, 31)
    (39, 31), (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31),
    (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31),
    (23, 31), (22, 31), (22, 30), (22, 29), (22, 28), (22, 27), (22, 26), (22, 25),
    (22, 24), (22, 23), (22, 22), (21, 22), (19, 22), (18, 22), (17, 22), (16, 22),
    (16, 23), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31),
    (16, 32), (16, 33), (15, 33), (14, 33), (13, 33), (12, 33), (11, 33), (10, 33),
    (9, 33), (9, 34), (9, 35), (9, 36),
    
    # Warp Transition to Area 3 (West) at (9, 0)
    (9, 0), (9, 1), (9, 2), (9, 4), (9, 5), (9, 6), (9, 7), (9, 9), (9, 10),
    (9, 11), (9, 12), (9, 13), (7, 13), (6, 13), (5, 13), (4, 13), (3, 13), (2, 13),
    (1, 13), (0, 13),
    
    # Warp Transition to Center (East Compartment) at (29, 25)
    (29, 25), (29, 26), (28, 26), (27, 26), (26, 26), (25, 26), (24, 26), (23, 26),
    (21, 26), (20, 26), (19, 26),
    
    # The Gold Teeth is at (19, 25). Stand at (19, 26) and interact!
    (19, 25),
    
    # Step back to row 26, then go to column 5 row 14
    (19, 26), (18, 26), (17, 26), (15, 26), (14, 26), (13, 26), (12, 26), (11, 26),
    (10, 26), (9, 26), (8, 26), (7, 26), (6, 26), (5, 26), (5, 25), (5, 23), (5, 22),
    (5, 21), (5, 20), (5, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14),
    
    # Path to Secret House (from get_surf.pyc)
    (4, 14), (3, 14), (2, 14), (1, 14), (0, 14), (0, 13), (0, 12), (0, 11), (0, 10),
    (0, 9), (0, 8), (1, 8), (2, 8), (3, 8)
]

# Max buttons we can press in a single run of the script
MAX_BUTTONS_PER_RUN = 95

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def find_closest_route_index(cx, cy):
    # Try to find if we are exactly on the route
    for i, (rx, ry) in enumerate(ROUTE):
        if rx == cx and ry == cy:
            return i
    # Fuzzy match: find closest tile within distance 1
    for i, (rx, ry) in enumerate(ROUTE):
        if abs(rx - cx) + abs(ry - cy) <= 1:
            return i
    return -1

def run_chunk():
    buttons_pressed = 0
    stuck_count = 0
    
    print("Determining current position...")
    pos = get_pos()
    
    if pos is None:
        run_away()
        pos = get_pos()
        if pos is None:
            print("Could not get coordinates even after running away. Exiting.")
            return False
            
    cx, cy = pos
    print(f"Current position: ({cx}, {cy})")
    
    route_idx = find_closest_route_index(cx, cy)
    if route_idx == -1:
        print(f"Error: Current position ({cx}, {cy}) is not on or near the golden route!")
        return False
        
    print(f"Aligned with route at index: {route_idx}")
    
    while buttons_pressed < MAX_BUTTONS_PER_RUN:
        pos = get_pos()
        if pos is None:
            run_away()
            continue
            
        cx, cy = pos
        route_idx = find_closest_route_index(cx, cy)
        if route_idx == -1:
            print(f"Lost alignment with route at ({cx}, {cy}).")
            return False
            
        # Check if we have reached the end of the route
        if route_idx == len(ROUTE) - 1:
            print("Arrived at the Secret House door at (3, 8)! Entering...")
            walk_step("Up")
            time.sleep(1.0)
            print("Speedrun Complete!")
            return True
            
        # Next target coordinate
        tx, ty = ROUTE[route_idx + 1]
        
        # Check for warp/transition
        dist = abs(tx - cx) + abs(ty - cy)
        if dist > 5:
            print(f"Map Transition / Warp detected! Jumped from ({cx}, {cy}) to ({tx}, {ty})")
            # We don't need to walk, we are already aligned with the next index
            continue
            
        # Determine direction
        dx = tx - cx
        dy = ty - cy
        
        direction = None
        if dx > 0:
            direction = "Right"
        elif dx < 0:
            direction = "Left"
        elif dy > 0:
            direction = "Down"
        elif dy < 0:
            direction = "Up"
            
        if direction is None:
            # We are already on the target, advance index
            continue
            
        # Special case: Pick up Gold Teeth
        if tx == 19 and ty == 25 and cx == 19 and cy == 26:
            print("Standing below Gold Teeth. Pressing A to pick it up...")
            bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
            buttons_pressed += 3
            # After picking up, we should be able to walk onto (19, 25)
            walk_step("Up")
            buttons_pressed += 1
            continue
            
        # Walk 1 step
        walk_step(direction)
        buttons_pressed += 1
        
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            continue
            
        ncx, ncy = new_pos
        if ncx == cx and ncy == cy:
            stuck_count += 1
            print(f"Stuck! Didn't move from ({cx}, {cy}). Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Stuck too long. Running RUN sequence to clear.")
                run_away()
                stuck_count = 0
                time.sleep(1.0)
        else:
            stuck_count = 0
            
    print(f"Reached button press limit ({buttons_pressed}) for this turn. Exiting chunk safely.")
    return True

if __name__ == "__main__":
    run_chunk()
