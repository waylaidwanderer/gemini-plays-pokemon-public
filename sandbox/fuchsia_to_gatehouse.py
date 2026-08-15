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
            # Map transition or menu active
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
    # Starting at (19, 28) in Fuchsia City (outside Pokemon Center).
    # Waypoints to enter the Safari Zone Gatehouse at (18, 3):
    waypoints = [
        (19, 30),  # Down to Row 30
        (24, 30),  # Right to Column 24
        (24, 21),  # Up to Row 21
        (22, 21),  # Left to Column 22
        (22, 14),  # Up to Row 14
        (26, 14),  # Right to Column 26
        (26, 9),   # Up through the cut bush to Row 9
        (37, 9),   # Right along Row 9 to Column 37 (bypassing horizontal barrier)
        (37, 2),   # Up Column 37 to Row 2
        (22, 2),   # Left along Row 2 to Column 22
        (22, 4),   # Down Column 22 to Row 4
        (18, 4),   # Left along Row 4 to Column 18
        (18, 3)    # Enter Safari Gatehouse door!
    ]
    
    print("Navigating from Fuchsia Pokemon Center to Safari Gatehouse...")
    for i, wp in enumerate(waypoints, 1):
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        pos = get_pos()
        if pos is None:
            print("Map changed or menu active.")
            break
        # If we successfully enter the Gatehouse, we will warp to Gatehouse coordinates (usually x < 10)
        if pos[0] < 10 and pos[1] < 10 and i > 10:
            print("Detected gatehouse coordinates. Stopping navigation.")
            break
            
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
