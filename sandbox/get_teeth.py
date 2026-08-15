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
    # Starting at (25, 2) in Area 3 (West)
    # Waypoints:
    # 1. (25, 18) - Down Column 25 to row 18
    # 2. (21, 18) - Left Row 18 to Column 21
    # 3. (21, 24) - Down Column 21 to Row 24
    # 4. (19, 24) - Left Row 24 to Column 19 (the open gap to southern corridor)
    # 5. (19, 26) - Down Column 19 to Row 26 (Row 26 Highway)
    waypoints = [
        (25, 18),
        (21, 18),
        (21, 24),
        (19, 24),
        (19, 26)
    ]
    
    print("Navigating to Gold Teeth location...")
    for i, wp in enumerate(waypoints, 1):
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    print("\nFacing UP towards Gold Teeth at (19, 25)...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    print("Pressing A to retrieve Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Clear dialogue
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after teeth pickup: {pos}")
    
    # Take screenshot of the screen to confirm
    img_path = bridge.take_screenshot()
    print(f"Final screenshot saved: {img_path}")

if __name__ == "__main__":
    main()
