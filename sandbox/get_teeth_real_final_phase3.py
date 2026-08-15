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
    pos = get_pos()
    print(f"Starting Phase 3 at: {pos}")
    
    # We are currently at (39, 31)
    waypoints = [
        (22, 31),  # Walk Left 17 steps along Row 31
        (22, 22),  # Walk Up 9 steps (climbing Western Southern Plateau stairs)
        (16, 22),  # Walk Left 6 steps on the plateau
        (16, 28),  # Walk Down 6 steps (descending stairs)
        (12, 28),  # Walk Left 4 steps
        (12, 30),  # Walk Down 2 steps (bypass pond)
        (8, 30),   # Walk Left 4 steps
        (8, 36)    # Transition Down to Area 3 (West) at (26, 0)
    ]
    
    print("Executing Safari Phase 3: Area 2 (North) to Area 3 (West)...")
    for i, wp in enumerate(waypoints, 1):
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                print("Map changed or battle occurred, stopping script.")
                break
        
        # If we successfully transitioned to Area 3 (West), the position will warp to around (26, 0)
        # We can check if pos[1] <= 2 (since the transition is on row 0 of Area 3)
        if pos[1] <= 2 and pos[0] == 26:
            print("Transition to Area 3 (West) detected! Stopping script.")
            break
            
        print(f"\n--- WAYPOINT {i}/{len(waypoints)}: {wp} ---")
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position at end of Phase 3: {pos}")

if __name__ == "__main__":
    main()
