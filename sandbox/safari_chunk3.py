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
    print("Executing Safari Chunk 3: Area 1 Northern Plateau to Area 2...")
    
    waypoints = [
        (8, 22),   # Left to Column 8
        (8, 8),    # Up Column 8 to Row 8
        (12, 8),   # Right along Row 8 to Column 12
        (12, 6),   # Up to climb northern plateau stairs to Row 6
        (17, 6),   # Right along Row 6 on plateau to Column 17
        (17, 8),   # Down to descend northern plateau stairs to Row 8
        (20, 8),   # Right along Row 8 to Column 20
        (20, 5),   # Up Column 20 to Row 5 (Northeast channel)
        (0, 5)     # Left along Row 5 to Column 0 (transition tile)
    ]
    
    for i, wp in enumerate(waypoints, 1):
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    print("Transitioning Left to Area 2 (North)...")
    bridge.press_buttons(["Left", "sleep 1500"])
    
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position at end of Chunk 3: {pos}")

if __name__ == "__main__":
    main()
