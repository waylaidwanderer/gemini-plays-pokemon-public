import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

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
    print("Closing Warden dialogue...")
    # Clear the "Hif fuff hefifoo!" textbox
    bridge.press_buttons(["B", "sleep 400", "B", "sleep 400"])
    
    pos = get_pos()
    print(f"Starting Phase 1 from: {pos}")
    
    if pos == (3, 3):
        # Walk DOWN to (4, 7) (doormat)
        navigate_to(4, 3)
        navigate_to(4, 7)
        # Exit Warden's House
        print("Exiting Warden's House...")
        bridge.press_buttons(["Down", "sleep 1500"])
        
    pos = get_pos()
    print(f"Position outside: {pos}")
    
    if pos == (27, 28):
        # Walk DOWN to Row 30: (27, 30)
        navigate_to(27, 30)
        # Walk LEFT to Column 19: (19, 30)
        navigate_to(19, 30)
        # Walk UP Column 19 to Row 8: (19, 8)
        navigate_to(19, 8)
        # Walk RIGHT to Column 37: (37, 8)
        navigate_to(37, 8)
        # Walk UP to Row 2: (37, 2)
        navigate_to(37, 2)
        # Walk LEFT to Column 22: (22, 2)
        navigate_to(22, 2)
        # Walk DOWN to Row 4: (22, 4)
        navigate_to(22, 4)
        # Walk LEFT to Column 18: (18, 4)
        navigate_to(18, 4)
        # Step UP into the Gatehouse at (18, 3)
        print("Entering Safari Gatehouse...")
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Phase 1 complete! Final position: {pos}")

if __name__ == "__main__":
    main()
