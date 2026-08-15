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
    # Starting at (22, 30) after fleeing Nidorina in Area 2 (North)
    # We must first press B to clear the 'Got away safely!' text if needed
    pos = get_pos()
    if pos is None:
        print("Clearing initial text box...")
        bridge.press_buttons(["B", "sleep 300"])
        time.sleep(1.0)
        
    waypoints = [
        (22, 22),  # Up 8 steps along Column 22 (climbing stairs at 22,23)
        (16, 22),  # Left 6 steps on the plateau
        (16, 28),  # Down 6 steps (descending stairs at 16,27) to grass
        (12, 28),  # Left 4 steps
        (12, 30),  # Down 2 steps (to bypass pond!)
        (8, 30),   # Left 4 steps
        (8, 35),   # Down 5 steps through statue gap
        (8, 36)    # Down 1 step to Transition to Area 3 (West)
    ]
    
    print("Executing Safari Chunk 4 Resume: Area 2 (North) to Area 3 (West)...")
    for i, wp in enumerate(waypoints, 1):
        pos = get_pos()
        if pos is None:
            print("Map changed or battle occurred, stopping script.")
            break
        # If map transitions to Area 3, coordinates will wrap to Area 3 coordinates (like x=26, y=0)
        if pos[0] < 30 and pos[0] > 10 and pos[1] < 5:
            print("Successfully inside Area 3 (West)!")
            break
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position at end of Chunk 4 Resume: {pos}")

if __name__ == "__main__":
    main()
