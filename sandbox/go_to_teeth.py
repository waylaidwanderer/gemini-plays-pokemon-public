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
    # Waypoints to reach (19, 24) facing DOWN from (26, 0)
    waypoints = [
        (25, 2),   # Down to row 2, Left to Column 25
        (25, 18),  # Down Column 25 to row 18
        (21, 18),  # Left to Column 21
        (21, 23),  # Down Column 21 to row 23
        (19, 23),  # Left to Column 19 on row 23
        (19, 24)   # Down 1 step to stand at (19, 24) facing DOWN
    ]
    
    for wp in waypoints:
        print(f"\nMoving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    # We are now at (19, 24) facing DOWN.
    # Let's interact with the ground below (19, 25)
    print("\nAttempting first pickup at (19, 24) facing DOWN...")
    bridge.press_buttons(["A", "sleep 500"])
    
    # Let's navigate to (19, 26) facing UP as well
    print("\nNavigating to (19, 26) facing UP...")
    waypoints_up = [
        (21, 24),  # Back to Column 21
        (21, 26),  # Down Column 21 to row 26
        (19, 26)   # Left to Column 19 on row 26
    ]
    for wp in waypoints_up:
        navigate_to(wp[0], wp[1])
        
    # Face UP: walk UP to (19, 25)? No, that might walk us onto it if it's not there.
    # We can just walk UP 1 step from (19, 26) to (19, 25).
    # If the item is there, we face UP and bump. If not, we step onto it.
    print("Facing UP by attempting to walk UP 1 step...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Press A
    print("Attempting second pickup facing UP...")
    bridge.press_buttons(["A", "sleep 500"])
    
    # Wait a bit and get final position
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position at end of go_to_teeth: {pos}")

if __name__ == "__main__":
    main()
