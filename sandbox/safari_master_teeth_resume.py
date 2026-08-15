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

def buy_safari_ticket():
    print("Talking to Safari Gatehouse clerk...")
    # Stand facing UP
    bridge.press_buttons(["Up", "sleep 500"])
    # Talk
    bridge.press_buttons(["A", "sleep 1200"])
    # Progress text
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    # Say YES (A)
    bridge.press_buttons(["A", "sleep 1200"])
    # Progress post-buy text
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    time.sleep(1.0)

def main():
    print("Executing Unified Safari Master Route...")
    
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
    print(f"Initial Position: {pos}")
    
    # State 1: inside Fuchsia City (outside Pokemon Center)
    if pos is not None and pos[1] >= 14 and pos[0] < 38 and pos != (3, 7) and pos[0] != 13:
        print("Navigating Fuchsia City to Safari Gatehouse via Column 37 Passage...")
        navigate_to(19, 30)
        navigate_to(25, 30)
        navigate_to(37, 30)
        navigate_to(37, 2)
        navigate_to(22, 2)
        navigate_to(22, 4)
        navigate_to(18, 4)
        
        # Enter Gatehouse
        print("Entering Safari Gatehouse...")
        bridge.press_buttons(["Up", "sleep 1500"])
        time.sleep(1.0)
        pos = get_pos()
        print(f"Position in Gatehouse: {pos}")
        
    # State 2: inside Gatehouse (usually at (3, 5) or (4, 5))
    pos = get_pos()
    if pos is not None and pos[1] >= 4 and pos[0] <= 10:
        print("Inside Safari Gatehouse, buying ticket...")
        navigate_to(3, 3) # Stand in front of clerk
        buy_safari_ticket()
        time.sleep(1.5)
        pos = get_pos()
        print(f"Position after ticket purchase: {pos}")
        
    # State 3: inside Safari Zone Center (starts at (15, 25))
    pos = get_pos()
    if pos == (15, 25) or (pos is not None and pos[0] == 15 and pos[1] == 25):
        print("\n=== PHASE 1: NAVIGATING CENTER TO AREA 1 (EAST) ===")
        navigate_to(15, 22)
        navigate_to(27, 22)
        navigate_to(27, 10)
        navigate_to(29, 10)
        print("Transitioning to Area 1 (East)...")
        bridge.press_buttons(["Right", "sleep 1500"])
        time.sleep(1.0)
        pos = get_pos()
        print(f"Position in Area 1 (East): {pos}")
        
    # State 4: inside Area 1 (East)
    pos = get_pos()
    if pos is not None and pos[0] <= 5 and pos[1] == 22:
        print("\n=== PHASE 2: NAVIGATING AREA 1 (EAST) TO AREA 2 (NORTH) ===")
        waypoints_area1 = [
            (20, 22),
            (20, 20),
            (12, 20),
            (12, 22),
            (8, 22),
            (8, 8),
            (12, 8),
            (12, 6),
            (17, 6),
            (17, 8),
            (20, 8),
            (20, 3),
            (7, 3),
            (7, 5),
            (0, 5)
        ]
        for wp in waypoints_area1:
            pos = get_pos()
            if pos is None:
                pos = handle_textbox_or_battle()
            navigate_to(wp[0], wp[1])
            
        print("Transitioning to Area 2 (North)...")
        bridge.press_buttons(["Left", "sleep 1500"])
        time.sleep(1.0)
        pos = get_pos()
        print(f"Position in Area 2 (North): {pos}")
        
    # State 5: inside Area 2 (North)
    pos = get_pos()
    if pos is not None and pos[0] >= 30 and pos[1] == 31:
        print("\n=== PHASE 3: NAVIGATING AREA 2 (NORTH) TO AREA 3 (WEST) ===")
        waypoints_area2 = [
            (22, 31),
            (22, 22),
            (16, 22),
            (16, 28),
            (12, 28),
            (12, 30),
            (8, 30),
            (8, 35),
            (8, 36)
        ]
        for wp in waypoints_area2:
            pos = get_pos()
            if pos is None:
                pos = handle_textbox_or_battle()
            navigate_to(wp[0], wp[1])
            
        print("Transitioning to Area 3 (West)...")
        bridge.press_buttons(["Down", "sleep 1500"])
        time.sleep(1.0)
        pos = get_pos()
        print(f"Position in Area 3 (West): {pos}")
        
    # State 6: inside Area 3 (West)
    pos = get_pos()
    if pos is not None and pos[1] <= 5:
        print("\n=== PHASE 4: NAVIGATING AREA 3 (WEST) TO GOLD TEETH ===")
        waypoints_area3 = [
            (25, 2),
            (25, 18),
            (21, 18),
            (21, 23),
            (19, 23),
            (19, 24)
        ]
        for wp in waypoints_area3:
            pos = get_pos()
            if pos is None:
                pos = handle_textbox_or_battle()
            navigate_to(wp[0], wp[1])
            
        # Stand facing DOWN and pick up the teeth
        print("Standing at (19, 24) facing DOWN, pressing A...")
        bridge.press_buttons(["Down", "sleep 500"])
        bridge.press_buttons(["A", "sleep 1500"])
        
        # Clear textbox "ACE found GOLD TEETH!"
        print("Clearing textbox...")
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 200"])
            
        print("Gold Teeth pickup sequence executed!")
        time.sleep(1.0)
        
    print("Script main loop finished.")

if __name__ == "__main__":
    main()
