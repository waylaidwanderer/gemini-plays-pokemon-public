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

def use_dig_safe():
    print("Using DIG to warp out of Safari Zone...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Start", "sleep 500"])
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "A", "sleep 1000"]) # POKÉMON
    for _ in range(5):
        bridge.press_buttons(["Up", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 800"]) # TRUFFLE (slot 2)
    bridge.press_buttons(["A", "sleep 4000"]) # Select DIG and wait for warp!

def main():
    pos = get_pos()
    print(f"Starting Golden Route from: {pos}")
    
    # We are currently at (9, 23)
    # Optimized Column 10 bypass path to minimize tall grass steps!
    waypoints = [
        (10, 23),  # Step 1: Walk to Column 10 (open grass)
        (10, 24),  # Step 2: Walk to Row 24 (open grass)
        (9, 24),   # Step 3: Walk Left onto Column 9 (tall grass - only 1 battle check!)
        (9, 26),   # Step 4: Walk DOWN to Row 26 Highway (open grass)
        (19, 26)   # Step 5: Walk East to stand directly below teeth
    ]
    
    print("Executing Safari Column 10 Golden Route to stand below Gold Teeth...")
    for i, wp in enumerate(waypoints, 1):
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                print("Map changed or battle occurred, stopping script.")
                break
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    pos = get_pos()
    if pos == (19, 26):
        # Face UP towards the Gold Teeth at (19, 25)
        print("Facing UP towards Gold Teeth...")
        bridge.press_buttons(["Up", "sleep 500"])
        
        # Interact to pick up the Gold Teeth!
        print("Interacting to retrieve Gold Teeth...")
        bridge.press_buttons(["A", "sleep 1500"])
        
        # Clear textbox
        print("Clearing textboxes...")
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 250"])
            
        # Use DIG to exit back to Fuchsia City
        use_dig_safe()
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final Position: {pos}")
    
    # Take screenshot of final position
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
