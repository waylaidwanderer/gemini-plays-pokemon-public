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
            # Maybe map transition occurred!
            print("Position is None. Possibly map transition occurred.")
            break
            
        # If we successfully transitioned to the Gatehouse, coordinates will change dramatically 
        # or we will be on a different map layout (e.g. x < 10, y < 10).
        # Fuchsia City has y up to 35, and we were at y=4. Gatehouse has coordinates like (3, 5).
        # Let's check if we transitioned. We will check if the script is still running but position is inside Gatehouse.
        if pos[1] > 15 and (tx, ty) == (18, 3):
            # If our target was the gatehouse entrance, but we are suddenly at y > 15, we are not in Fuchsia's north side anymore!
            # But wait, gatehouse coordinates are small, like (3, 5). Fuchsia is (18, 4).
            # So if x changes significantly away from 18, we probably transitioned.
            pass

        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        print(f"Current: {pos}, Target: ({tx}, {ty})")
        
        # Simple pathfinding: horizontal first, then vertical
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
    # Starting at (26, 9) in Fuchsia City.
    # Waypoints:
    # 1. (37, 9) - Walk East along Row 9 to Column 37 (to bypass Row 7 tree barrier)
    # 2. (37, 2) - Walk North along Column 37 to Row 2
    # 3. (22, 2) - Walk West along Row 2 to Column 22
    # 4. (22, 4) - Walk South along Column 22 to Row 4
    # 5. (18, 4) - Walk West along Row 4 to Column 18
    # 6. (18, 3) - Enter Gatehouse door
    waypoints = [
        (37, 9),
        (37, 2),
        (22, 2),
        (22, 4),
        (18, 4),
        (18, 3)
    ]
    
    for wp in waypoints:
        print(f"\nMoving to Waypoint: {wp}")
        pos = get_pos()
        if pos is None:
            print("Map changed or menu active.")
            break
        # If we are already on a different map (e.g. inside Gatehouse), we can stop.
        # Gatehouse maps usually have width < 10. Fuchsia has width 40.
        # Let's check if the current coordinate is valid for Fuchsia's north corridor.
        # If we transitioned to Gatehouse, the x coordinate will likely be < 10.
        if pos[0] < 10 and pos[1] < 10:
            print("Detected gatehouse coordinates. Exiting fuchsia_to_gatehouse.")
            break
            
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final coordinate: {pos}")

if __name__ == "__main__":
    main()
