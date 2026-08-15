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
    print("Executing Safari Master Route to Gold Teeth...")
    
    # We are currently at (20, 5) in Area 1 (East).
    # Step 1: Traverse Area 1 (East)
    waypoints_area1 = [
        (20, 22),  # Right to Column 20 (on ground)
        (20, 20),  # Up to Row 20 (climbing stairs to plateau)
        (12, 20),  # Left along plateau Row 20
        (12, 22),  # Down to descend stairs to Row 22
        (8, 22),   # Left along Row 22 to Column 8
        (8, 8),    # Up Column 8 to Row 8
        (12, 8),   # Right along Row 8 to Column 12
        (12, 6),   # Up to climb northern plateau stairs to Row 6
        (17, 6),   # Right along Row 6 on plateau to Column 17
        (17, 8),   # Down to descend northern plateau stairs to Row 8
        (20, 8),   # Right to Column 20
        (20, 3),   # Up Column 20 to Row 3 (bypassing building)
        (7, 3),    # Left along Row 3 to Column 7 (bypassing building and pine tree at (5,3))
        (7, 5),    # Down to Row 5 (below the pine tree)
        (0, 5)     # Left along Row 5 to Column 0 (enters Area 2 North)
    ]
    
    print("\n=== PHASE 1: NAVIGATING AREA 1 (EAST) TO AREA 2 (NORTH) ===")
    
    # Find closest waypoint to start from, in case we are partially through
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
        
    start_idx = 0
    if pos is not None:
        # Determine where we can resume in Area 1
        if pos[1] == 5 and pos[0] == 20:
            # We are at (20, 5), we can resume from (20, 3)
            start_idx = 11
            print(f"Resuming from (20, 5) to (20, 3) at index {start_idx}")
        elif pos[1] == 20 and 12 <= pos[0] <= 20:
            # We are on the southern plateau, we can resume from (12, 20)
            start_idx = 2
            print(f"Resuming from plateau waypoint at index {start_idx} (target: (12, 20))")
            
    for i in range(start_idx, len(waypoints_area1)):
        wp = waypoints_area1[i]
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"Moving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    print("\nTransitioning to Area 2 (North)...")
    bridge.press_buttons(["Left", "sleep 1500"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
    print(f"Current Position in Area 2 (North): {pos}")
    
    # Step 2: Traverse Area 2 (North)
    waypoints_area2 = [
        (22, 31),  # Left along southern corridor Row 31
        (22, 22),  # Up to climb Western Southern Plateau stairs to Row 22
        (16, 22),  # Left on plateau Row 22 to Column 16
        (16, 28),  # Down to descend stairs to Row 28
        (12, 28),  # Left along Row 28 to Column 12
        (12, 30),  # Down Column 12 to Row 30 (bypasses pond)
        (8, 30),   # Left along Row 30 to Column 8
        (8, 35),   # Down Column 8 past statue gap to Row 35
        (8, 36)    # Down 1 step (enters Area 3 West)
    ]
    
    print("\n=== PHASE 2: NAVIGATING AREA 2 (NORTH) TO AREA 3 (WEST) ===")
    for wp in waypoints_area2:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"Moving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    print("\nTransitioning to Area 3 (West)...")
    bridge.press_buttons(["Down", "sleep 1500"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
    print(f"Current Position in Area 3 (West): {pos}")
    
    # Step 3: Traverse Area 3 (West) to Gold Teeth
    waypoints_area3 = [
        (25, 2),   # Down to Row 2, Left to Column 25
        (25, 18),  # Down Column 25 to Row 18
        (21, 18),  # Left to Column 21 on Row 18
        (21, 23),  # Down Column 21 to Row 23
        (19, 23),  # Left to Column 19 on Row 23
        (19, 24)   # Down to stand at (19, 24) facing DOWN
    ]
    
    print("\n=== PHASE 3: NAVIGATING AREA 3 (WEST) TO GOLD TEETH ===")
    for wp in waypoints_area3:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"Moving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    print("\nAttempting first pickup at (19, 24) facing DOWN...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Optional Step 4: Stand at (19, 26) facing UP and press A (if first pickup was solid)
    print("\nNavigating to (19, 26) facing UP as a fallback...")
    waypoints_area3_up = [
        (21, 24),  # Back to Column 21 Row 24
        (21, 26),  # Down to Row 26
        (19, 26)   # Left to Column 19 on Row 26
    ]
    for wp in waypoints_area3_up:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"Moving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    print("\nAttempting second pickup at (19, 26) facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1500"])
    
    pos = get_pos()
    print(f"\nFinal Position: {pos}")
    print("Gold Teeth pickup attempt complete!")

if __name__ == "__main__":
    main()
