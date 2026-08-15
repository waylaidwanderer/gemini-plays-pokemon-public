import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
    # Clear post-flee text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
        
    pos = get_pos()
    print(f"Coordinates after battle handling: {pos}")
    return pos

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
        
    return handle_textbox_or_battle()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            continue
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        print(f"Current: {pos}, Target: ({tx}, {ty})")
        # Determine direction
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
                print("Stuck trying to move! Clearing with B...")
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
        else:
            stuck_count = 0
        time.sleep(0.5)

def main():
    # Starting at (29, 23) in Area 3 (West)
    # Waypoints:
    # 1. (31, 23) (Right to Column 31)
    # 2. (31, 26) (Down to Row 26)
    # 3. (19, 26) (Left along Row 26 to Column 19)
    waypoints = [
        (31, 23),
        (31, 26),
        (19, 26)
    ]
    
    for wp in waypoints:
        print(f"\nMoving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    # Stand at (19, 26) facing UP
    print("\nFacing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Press A to pick up Gold Teeth
    print("Pressing A to pick up item...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Check if a dialog box popped up (position is None)
    pos = get_pos()
    print(f"Position after pickup attempt: {pos}")
    if pos is None:
        print("We found a dialog box! Successfully picked up the Gold Teeth!")
        # Clear the dialog box
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 300"])
            
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position at end of get_teeth_south: {pos}")

if __name__ == "__main__":
    main()
