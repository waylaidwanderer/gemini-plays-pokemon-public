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
            
        # Detect if we successfully entered the Warden's House.
        # Entrance lands us at (4, 7) or similar inside the house.
        if pos[0] < 10 and pos[1] < 10:
            print("Successfully entered Warden's House!")
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
    # Starting at (19, 28) in Fuchsia City outside Pokemon Center.
    # Waypoints to enter the Warden's House at (27, 27):
    waypoints = [
        (19, 30),  # Down to Row 30
        (30, 30),  # Right along Row 30 to Column 30
        (30, 28),  # Up Column 30 to Row 28
        (27, 28),  # Left along Row 28 to Column 27 (facing Warden's door)
        (27, 27)   # Enter Warden's House!
    ]
    
    print("Navigating to Warden's House door...")
    for i, wp in enumerate(waypoints, 1):
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        pos = get_pos()
        if pos is None:
            print("Map changed or menu active.")
            break
        if pos[0] < 10 and pos[1] < 10:
            print("Detected Warden's House interior coordinates. Stopping navigation.")
            break
            
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
