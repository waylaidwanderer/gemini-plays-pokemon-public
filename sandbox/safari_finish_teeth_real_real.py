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
    print("Executing final retrieval sequence via Column 22 gap...")
    # Currently standing at (21, 24) in Area 3 (West)
    
    waypoints = [
        (22, 24), # Right to Column 22 (grass, battle possible)
        (22, 26), # Down to Row 26 (highway)
        (19, 26)  # Left to Column 19 (directly under the teeth)
    ]
    
    for wp in waypoints:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
        print(f"Moving to Waypoint: {wp}")
        navigate_to(wp[0], wp[1])
        
    # Face UP
    print("Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Pick up Gold Teeth
    print("Pressing A to pick up Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    pos = get_pos()
    print(f"Final Position: {pos}")
    print("Sequence complete!")

if __name__ == "__main__":
    main()
