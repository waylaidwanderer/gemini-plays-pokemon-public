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
    print("Navigating to PC inside Pokemon Center...")
    
    # We are at (5, 7)
    waypoints = [
        (5, 5),   # Up to Row 5
        (13, 5),  # Right to Column 13
        (13, 4)   # Up to PC desk
    ]
    
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    # Stand facing UP towards PC
    print("Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Access PC
    print("Accessing PC...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Progress boot text "ACE turned on the PC!"
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Select ACE's PC (2nd option)
    print("Selecting ACE's PC...")
    bridge.press_buttons(["Down", "sleep 500", "A", "sleep 1500"])
    
    # Select "WITHDRAW ITEM" (1st option)
    print("Selecting Withdraw Item...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    print("PC Withdraw menu opened!")

if __name__ == "__main__":
    main()
