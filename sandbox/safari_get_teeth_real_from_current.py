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
    print("Executing Golden Route from current (20, 19) to Gold Teeth...")
    
    # 1. Walk to (21, 18)
    navigate_to(21, 18)
    
    # 2. Climb East Stairs to Plateau flat top (21, 16)
    print("\n--- CLIMBING EAST STAIRS TO ROW 16 ---")
    walk_step_robust("Up") # to (21, 17)
    walk_step_robust("Up") # to (21, 16)
    
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
    print(f"Position on Plateau flat top: {pos}")
    
    # 3. Walk across Plateau to (6, 16)
    print("\n--- WALKING PLATEAU TO (6, 16) ---")
    navigate_to(6, 16)
    
    # 4. Descend West Stairs to Row 26
    print("\n--- DESCENDING WEST STAIRS TO ROW 26 ---")
    navigate_to(6, 26)
    
    # 5. Walk East along Row 26 Highway to (19, 26)
    print("\n--- WALKING ROW 26 HIGHWAY TO (19, 26) ---")
    navigate_to(19, 26)
    
    # 6. Stand facing UP and pick up the teeth
    print("\n--- PICKING UP GOLD TEETH ---")
    bridge.press_buttons(["Up", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Clear textbox "ACE found GOLD TEETH!"
    print("Clearing textbox...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 250"])
        
    pos = get_pos()
    print(f"Finished. Position: {pos}")

if __name__ == "__main__":
    main()
