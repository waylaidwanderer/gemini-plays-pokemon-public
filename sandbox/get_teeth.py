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
    # We start at (15, 25) in Safari Zone Center.
    
    # Phase 1: Safari Zone Center to Area 1 (East)
    # Target transition is (30, 10). We use intermediate waypoints to avoid pond/fences.
    phase1_waypoints = [
        (15, 22),
        (28, 22),
        (28, 10),
        (30, 10) # transitions to Area 1 (East)
    ]
    
    # Phase 2: Area 1 (East) to Area 2 (North)
    # Transition at (0, 5)
    phase2_waypoints = [
        (0, 24),
        (20, 24),
        (20, 20), # plateau climb
        (12, 20),
        (12, 22), # plateau descend
        (8, 22),
        (8, 8),
        (12, 8),
        (12, 6),  # northern plateau climb
        (17, 6),
        (17, 8),  # plateau descend
        (20, 8),
        (20, 3),
        (7, 3),
        (7, 5),
        (0, 5)    # transition to Area 2 (North)
    ]
    
    # Phase 3: Area 2 (North) to Area 3 (West)
    # Transition at (8, 36)
    phase3_waypoints = [
        (22, 31),
        (22, 22), # plateau climb
        (16, 22),
        (16, 28), # plateau descend
        (12, 28),
        (12, 30), # bypass pond
        (8, 30),
        (8, 35),
        (8, 36)   # transition to Area 3 (West)
    ]
    
    # Phase 4: Area 3 (West) to Gold Teeth (Southern Approach)
    # Target is (19, 26) facing UP
    phase4_waypoints = [
        (26, 2),
        (25, 2),
        (25, 18),
        (21, 18),
        (21, 26), # Southern ground passage
        (19, 26)  # Directly south of Gold Teeth
    ]
    
    # Combine all waypoints in sequence
    all_waypoints = phase1_waypoints + phase2_waypoints + phase3_waypoints + phase4_waypoints
    
    print("Beginning the Safari Zone Golden Route...")
    for i, wp in enumerate(all_waypoints, 1):
        print(f"\n--- WAYPOINT {i}/{len(all_waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    print("\nFacing UP towards Gold Teeth...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    print("Pressing A to retrieve Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Clear dialogue
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
