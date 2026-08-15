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
    # Waypoints to enter Warden's House from (26, 12)
    waypoints = [
        (26, 14),  # Down Column 26 to Row 14
        (22, 14),  # Left Row 14 to Column 22
        (22, 21),  # Down Column 22 to Row 21
        (24, 21),  # Right Row 21 to Column 24
        (24, 28),  # Down Column 24 to Row 28
        (27, 28)   # Right Row 28 to Column 27 (Warden's House door mat)
    ]
    
    for wp in waypoints:
        print(f"\nMoving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    # Walk UP into Warden's House
    print("\nEntering Warden's House...")
    walk_step_robust("Up")
    time.sleep(1.0)
    walk_step_robust("Up")
    
    time.sleep(2.0)
    pos = get_pos()
    print(f"Position inside Warden's House: {pos}")

if __name__ == "__main__":
    main()
