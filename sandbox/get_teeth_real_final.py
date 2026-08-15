import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialogue...")
    # Progress text box/battle menus with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN from battle
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
    # Clear any residual menus
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
    bridge.press_buttons([direction, "sleep 400"])
    
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
        time.sleep(0.3)

def use_cut():
    print("Executing CUT menu sequence...")
    bridge.press_buttons(["Start", "sleep 500"])
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 1000"]) # POKÉMON
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 800"]) # Select TRUFFLE
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 1500"]) # Select CUT
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])

def buy_ticket_and_enter():
    print("Talking to Gatekeeper clerk...")
    # Walk UP to clerk
    for _ in range(3):
        bridge.press_buttons(["Up", "sleep 450"])
    bridge.press_buttons(["Up", "sleep 500", "A", "sleep 1000"])
    
    # Progress dialog and buy ticket
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1200"]) # Select YES
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    time.sleep(2.0)

def main():
    pos = get_pos()
    print(f"Initial Position: {pos}")
    
    # PHASE 1: Exit Pokémon Center
    if pos is not None and pos[0] > 6 and pos[1] == 5:
        print("PHASE 1: Exiting Pokémon Center...")
        navigate_to(5, 5)
        # Walk down to Row 8 to trigger exit warp
        for _ in range(4):
            bridge.press_buttons(["Down", "sleep 400"])
        time.sleep(2.0)
        
    pos = get_pos()
    print(f"Position after exiting Pokémon Center: {pos}")
    
    # PHASE 2: Walk to CUT bush in Fuchsia City and CUT it
    if pos == (19, 28):
        print("PHASE 2: Walking to CUT bush...")
        waypoints_fuchsia = [
            (24, 28),
            (24, 21),
            (22, 21),
            (22, 14),
            (26, 14)
        ]
        for wp in waypoints_fuchsia:
            navigate_to(wp[0], wp[1])
            
        print("Facing UP towards CUT bush...")
        bridge.press_buttons(["Up", "sleep 500"])
        use_cut()
        time.sleep(1.0)
        
        # Step UP through the cut bush
        print("Stepping UP through CUT bush...")
        walk_step_robust("Up")
        time.sleep(1.0)
        
    pos = get_pos()
    print(f"Position after cutting bush: {pos}")
    
    # PHASE 3: Walk to Safari Gatehouse
    if pos is not None and pos[1] <= 13:
        print("PHASE 3: Walking to Safari Zone Gatehouse...")
        waypoints_to_gate = [
            (26, 9),
            (26, 8),
            (37, 8),
            (37, 2),
            (22, 2),
            (22, 4),
            (18, 4)
        ]
        for wp in waypoints_to_gate:
            navigate_to(wp[0], wp[1])
            
        print("Entering Gatehouse and buying ticket...")
        # Walk UP to enter Gatehouse, then buy ticket
        buy_ticket_and_enter()
        time.sleep(2.0)
        
    pos = get_pos()
    print(f"Position after entering Safari Zone: {pos}")
    
    # PHASE 4: Safari Zone Center to Area 1 (East)
    if pos == (15, 25):
        print("PHASE 4: Navigating Center to Area 1...")
        waypoints_center = [
            (15, 22),
            (27, 22),
            (27, 10),
            (29, 10)
        ]
        for wp in waypoints_center:
            navigate_to(wp[0], wp[1])
        print("Transitioning to Area 1...")
        bridge.press_buttons(["Right", "sleep 1500"])
        time.sleep(2.0)
        
    pos = get_pos()
    print(f"Position inside Area 1: {pos}")
    
    # PHASE 5: Area 1 (East) to Area 2 (North)
    if pos == (0, 22) or (pos is not None and pos[1] == 22 and pos[0] <= 2):
        print("PHASE 5: Navigating Area 1 to Area 2...")
        waypoints_area1 = [
            (20, 22),
            (20, 20), # Climb plateau stairs
            (12, 20),
            (12, 22), # Descend plateau stairs
            (8, 22),
            (8, 8),
            (12, 8),
            (12, 6),  # Climb northern plateau stairs
            (17, 6),
            (17, 8),  # Descend plateau stairs
            (20, 8),
            (20, 3),
            (7, 3),
            (7, 5),
            (0, 5)    # Transition to Area 2
        ]
        for wp in waypoints_area1:
            navigate_to(wp[0], wp[1])
        print("Transitioning to Area 2...")
        bridge.press_buttons(["Left", "sleep 1500"])
        time.sleep(2.0)
        
    pos = get_pos()
    print(f"Position inside Area 2: {pos}")
    
    # PHASE 6: Area 2 (North) to Area 3 (West)
    if pos == (39, 31) or (pos is not None and pos[1] == 31 and pos[0] >= 37):
        print("PHASE 6: Navigating Area 2 to Area 3...")
        waypoints_area2 = [
            (22, 31),
            (22, 22), # Climb plateau stairs
            (16, 22),
            (16, 28), # Descend plateau stairs
            (12, 28),
            (12, 30),
            (8, 30),
            (8, 35),  # Bypass pond/statues
            (8, 36)   # Transition to Area 3
        ]
        for wp in waypoints_area2:
            navigate_to(wp[0], wp[1])
        print("Transitioning to Area 3...")
        bridge.press_buttons(["Down", "sleep 1500"])
        time.sleep(2.0)
        
    pos = get_pos()
    print(f"Position inside Area 3: {pos}")
    
    # PHASE 7: Area 3 (West) to Gold Teeth!
    if pos == (26, 0) or (pos is not None and pos[0] == 26 and pos[1] <= 2):
        print("PHASE 7: Navigating Area 3 to Gold Teeth...")
        waypoints_area3 = [
            (26, 2),
            (25, 2),
            (25, 18),
            (21, 18),
            (21, 23),
            (19, 23),
            (19, 24),
            (18, 24),
            (18, 26),
            (19, 26)
        ]
        for wp in waypoints_area3:
            navigate_to(wp[0], wp[1])
            
        print("Facing UP towards Gold Teeth...")
        bridge.press_buttons(["Up", "sleep 500"])
        
        print("Attempting to pick up Gold Teeth...")
        bridge.press_buttons(["A", "sleep 1500"])
        
        print("Clearing text box...")
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 250"])
            
    pos = get_pos()
    print(f"Final Position: {pos}")
    
    # Take screenshot of the result
    img = bridge.take_screenshot()
    print(f"Screenshot saved: {img}")

if __name__ == "__main__":
    main()
