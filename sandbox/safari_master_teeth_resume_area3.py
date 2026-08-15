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
    print("Executing Safari Master Route Area 3 (West) - Final teeth pickup...")
    
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
    print(f"Starting Position in Area 3 (West): {pos}")
    
    # Traverse Area 3 (West) to Gold Teeth
    waypoints_area3 = [
        (25, 2),   # Already here!
        (25, 18),  # Down Column 25 to Row 18
        (21, 18),  # Left to Column 21 on Row 18
        (21, 23),  # Down Column 21 to Row 23
        (19, 23),  # Left to Column 19 on Row 23
        (19, 24)   # Down to stand at (19, 24) facing DOWN
    ]
    
    print("\n=== PHASE 3: NAVIGATING AREA 3 (WEST) TO GOLD TEETH ===")
    
    start_idx = 0
    if pos is not None:
        if pos == (25, 2):
            start_idx = 1
            print("Already at (25, 2), starting from next waypoint...")
            
    for i in range(start_idx, len(waypoints_area3)):
        wp = waypoints_area3[i]
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"Moving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    print("\nAttempting first pickup at (19, 24) facing DOWN...")
    bridge.press_buttons(["Down", "sleep 500"]) # Ensure facing down
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Optional Fallback: Stand at (19, 26) facing UP and press A
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
