import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

# Verified ground-level walkable route via Row 26
ROUTE = [
    # Start at (15, 24)
    (15, 24), (15, 25), (15, 26),
    # Row 26 all the way to Column 30
    (16, 26), (17, 26), (18, 26), (19, 26), (20, 26), (21, 26), (22, 26), (23, 26), (24, 26), (25, 26), (26, 26), (27, 26), (28, 26), (29, 26), (30, 26),
    # Up Column 30 to Row 11
    (30, 25), (30, 24), (30, 23), (30, 22), (30, 21), (30, 20), (30, 19), (30, 18), (30, 17), (30, 16), (30, 15), (30, 14), (30, 13), (30, 12), (30, 11),
    # Setup for transition
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
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 350"])

def find_closest_route_index(cx, cy):
    for i, (rx, ry) in enumerate(ROUTE):
        if rx == cx and ry == cy:
            return i
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
        
        route_idx = find_closest_route_index(cx, cy)
        if route_idx == -1:
            print(f"Position ({cx}, {cy}) is off the ROUTE. Checking if we transitioned to Area 1...")
            # If we transitioned to Area 1 East, our coordinates might be near (0, 23)
            # Let's see if we are at x=0
            if cx == 0:
                print("Successfully transitioned to Area 1 (East)!")
                return True
            return False
            
        if cx == 29 and cy == 11:
            print("At setup tile (29, 11). Walking Right to transition to Area 1...")
            walk_step("Right")
            time.sleep(1.0)
            return True
            
        tx, ty = ROUTE[route_idx + 1]
        
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
            continue
            
        print(f"Step {route_idx} -> {route_idx + 1}: Moving {direction} to ({tx}, {ty})")
        walk_step(direction)
        buttons_pressed += 1
        
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
