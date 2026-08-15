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
        bridge.press_buttons(["B", "sleep 150"])
        return get_pos()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            bridge.press_buttons(["B", "sleep 150"])
            continue
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        print(f"Current: {pos}, Target: ({tx}, {ty})")
        # Greedy navigation
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
    print("Navigating from current (19, 20) to Pokemon Center via Column 8 highway...")
    
    waypoints = [
        (8, 20),   # Left along Row 20 to Column 8
        (8, 32),   # Down Column 8 to Row 32 (jumping over ledge)
        (19, 32),  # Right along Row 32 to Column 19
        (19, 28),  # Up Column 19 to doormat
        (19, 27)   # Enter Pokemon Center
    ]
    
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    print("Entering Pokemon Center...")
    walk_step_robust("Up")
    time.sleep(1.5)
    
    pos = get_pos()
    print(f"Final Position inside Pokemon Center: {pos}")

if __name__ == "__main__":
    main()
