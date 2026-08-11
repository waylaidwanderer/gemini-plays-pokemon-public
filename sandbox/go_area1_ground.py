import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

# 100% verified ground-level walkable route from Safari Zone Center (8, 16) to Area 1 (East) at (0, 23)
ROUTE = [
    # Start at (8, 16)
    (8, 16), (8, 17), (8, 18), (8, 19), (8, 20), (8, 21), (8, 22), (8, 23), (8, 24),
    (9, 24), (10, 24),
    # Bypass the signpost at (13, 24)
    (10, 23), (11, 23), (12, 23), (13, 23), (14, 23), (14, 24),
    # Eastern bypass
    (15, 24), (16, 24), (17, 24), (18, 24), (19, 24), (20, 24), (21, 24), (22, 24), (23, 24), (24, 24), (25, 24), (26, 24), (27, 24),
    # Bypass Rhydon statues at row 25
    (27, 25), (27, 26),
    # Go to Column 30
    (28, 26), (29, 26), (30, 26),
    # Go UP Column 30
    (30, 25), (30, 24), (30, 23), (30, 22), (30, 21), (30, 20), (30, 19), (30, 18), (30, 17), (30, 16), (30, 15), (30, 14), (30, 13), (30, 12), (30, 11),
    # Setup for Area 1 East transition
    (29, 11)
]

MAX_BUTTONS_PER_RUN = 70

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # Smash B first to clear text
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def find_closest_route_index(cx, cy):
    # Direct match
    for i, (rx, ry) in enumerate(ROUTE):
        if rx == cx and ry == cy:
            return i
    # Fuzzy match
    for i, (rx, ry) in enumerate(ROUTE):
        if abs(rx - cx) + abs(ry - cy) <= 1:
            return i
    return -1

def execute_route():
    buttons_pressed = 0
    stuck_count = 0
    
    while buttons_pressed < MAX_BUTTONS_PER_RUN:
        pos = get_pos()
        if pos is None:
            run_away()
            buttons_pressed += 5
            continue
            
        cx, cy = pos
        print(f"Current position: ({cx}, {cy})")
        
        # Check if we transitioned to Area 1 (East)
        # Transition can occur at (30, 11) going Right
        # Let's see if our x coord jumped to 0 or we are on a different map
        # Area 1 has different landmarks. If get_pos is not on ROUTE and we transitioned, we will detect it.
        route_idx = find_closest_route_index(cx, cy)
        if route_idx == -1:
            print(f"Position ({cx}, {cy}) is off the ROUTE. We may have transitioned to Area 1 (East)!")
            return True
            
        # If we reached the final coordinate (29, 11), we walk Right to transition
        if cx == 29 and cy == 11:
            print("At setup tile (29, 11). Walking Right to transition to Area 1...")
            walk_step("Right")
            time.sleep(1.0)
            return True
            
        # Next target
        tx, ty = ROUTE[route_idx + 1]
        
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
            # We are already on target, move on
            continue
            
        print(f"Step {route_idx} -> {route_idx + 1}: Moving {direction} to ({tx}, {ty})")
        walk_step(direction)
        buttons_pressed += 1
        
        # Verify movement
        new_pos = get_pos()
        if new_pos is None:
            run_away()
            buttons_pressed += 5
            continue
            
        ncx, ncy = new_pos
        if ncx == cx and ncy == cy:
            stuck_count += 1
            print(f"Stuck at ({cx}, {cy})! Count: {stuck_count}")
            if stuck_count > 3:
                print("Force run sequence to clear stuck state.")
                run_away()
                stuck_count = 0
                time.sleep(1.0)
        else:
            stuck_count = 0

    print("Reached button press limit for this turn.")
    return False

if __name__ == "__main__":
    execute_route()
