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
            bridge.press_buttons(["B", "sleep 200"])
            continue
            
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
    # Waypoints to (26, 12) from (18, 4) detouring around the Gatehouse
    waypoints = [
        (22, 4),  # Right on Row 4 to Column 22
        (22, 2),  # Up on Column 22 to Row 2
        (37, 2),  # Right on Row 2 to Column 37
        (37, 9),  # Down on Column 37 to Row 9
        (26, 9),  # Left on Row 9 to Column 26
        (26, 12)  # Down on Column 26 to Row 12
    ]
    
    for wp in waypoints:
        print(f"\nMoving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    time.sleep(1.0)
    pos = get_pos()
    print(f"Arrived at cut bush face coordinate: {pos}")

if __name__ == "__main__":
    main()
