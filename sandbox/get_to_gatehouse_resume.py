import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        print("Menu or text box active, pressing B...")
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 400"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            print("Position is None. Possibly map transition occurred.")
            break
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        print(f"Current: {pos}, Target: ({tx}, {ty})")
        if pos[0] < tx:
            direction = "Right"
        elif pos[0] > tx:
            direction = "Left"
        elif pos[1] < ty:
            direction = "Down"
        elif pos[1] > ty:
            direction = "Up"
            
        new_pos = walk_step_robust(direction)
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Clearing with B...")
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
        else:
            stuck_count = 0
        time.sleep(0.4)

def main():
    # Starting at (26, 14) in Fuchsia City, bush is already cut.
    waypoints = [
        (26, 9),   # Up 5 steps (through cut bush) to Row 9
        (37, 9),   # Right 11 along Row 9 to Column 37
        (37, 2),   # Up 7 Column 37 to Row 2
        (22, 2),   # Left 15 Row 2 to Column 22
        (22, 4),   # Down 2 Column 22 to Row 4
        (18, 4),   # Left 4 Row 4 to Column 18
        (18, 3)    # Up 1 step to Enter Safari Gatehouse!
    ]
    
    print("Navigating to Safari Gatehouse...")
    for i, wp in enumerate(waypoints, 1):
        pos = get_pos()
        if pos is None:
            print("Map changed, stopping navigation.")
            break
        # If we enter the gatehouse, coordinates will change to gatehouse interior
        if pos[0] < 10 and pos[1] < 10:
            print("Successfully inside Gatehouse!")
            break
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position inside or near Gatehouse: {pos}")

if __name__ == "__main__":
    main()
