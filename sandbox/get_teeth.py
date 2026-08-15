import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling battle or dialogue...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1200"])
    
    # Clear post-flee text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
        
    pos = get_pos()
    print(f"Coordinates after battle/dialogue handling: {pos}")
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
    return new_pos

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
            
        # Special warp-transition bypass:
        # If the target is a warp tile, we might transition maps immediately upon stepping on it.
        # This will cause get_pos() to return a coordinate very far away from (tx, ty) on the new map.
        # If the coordinate is on the next map, we can consider this waypoint reached!
        if (tx, ty) == (29, 10) and pos[0] < 5: # Emerge in Area 1 East around x=0
            print(f"Detected transition to Area 1 East! pos: {pos}")
            break
        if (tx, ty) == (0, 5) and pos[0] > 30: # Emerge in Area 2 North around x=39
            print(f"Detected transition to Area 2 North! pos: {pos}")
            break
        if (tx, ty) == (8, 36) and pos[1] < 5: # Emerge in Area 3 West around y=0
            print(f"Detected transition to Area 3 West! pos: {pos}")
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
        time.sleep(0.05)

def main():
    pos = get_pos()
    print(f"Starting actual walkable route to Gold Teeth from: {pos}")
    
    waypoints = [
        # Map 1: Safari Zone Center
        (15, 22),
        (27, 22),
        (27, 10),
        (29, 10),  # Warp to Area 1 (East)
        
        # Map 2: Area 1 (East)
        (0, 22),   # Emerge
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
        (0, 5),    # Warp to Area 2 (North)
        
        # Map 3: Area 2 (North)
        (39, 31),  # Emerge
        (22, 31),
        (22, 23),
        (22, 22),
        (16, 22),
        (16, 27),
        (16, 28),
        (12, 28),
        (12, 30),
        (8, 30),
        (8, 35),
        (8, 36),   # Warp to Area 3 (West)
        
        # Map 4: Area 3 (West)
        (26, 0),   # Emerge
        (26, 2),
        (25, 2),
        (25, 18),
        (21, 18),
        (21, 23),
        (19, 23),
        (19, 24),
        (18, 24),
        (18, 26),
        (19, 26)   # Stand at (19, 26) directly below the Gold Teeth
    ]
    
    for i, wp in enumerate(waypoints, 1):
        # If we already passed an emerge waypoint due to warp detection, skip it
        current_p = get_pos()
        if current_p is None:
            handle_textbox_or_battle()
            current_p = get_pos()
            
        if wp == (0, 22) and current_p[0] != 0:
            print("Skipping emerge waypoint (0, 22)")
            continue
        if wp == (39, 31) and current_p[0] != 39:
            print("Skipping emerge waypoint (39, 31)")
            continue
        if wp == (26, 0) and current_p[1] != 0:
            print("Skipping emerge waypoint (26, 0)")
            continue
            
        print(f"Heading to Waypoint {i}: {wp}")
        navigate_to(wp[0], wp[1])
        
    # Stand at (19, 26) facing UP
    print("Arrived at target stand position (19, 26). Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Interact with Gold Teeth at (19, 25)
    print("Retrieving Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Dismiss dialogue text boxes
    print("Dismissing dialogue text boxes...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 250"])
        
    # Audit inventory to verify Gold Teeth
    print("Opening START menu to verify Bag...")
    bridge.press_buttons(["Start", "sleep 500"])
    
    # We want POKeMON or ITEM? We want ITEM!
    # Let's find ITEM in START menu.
    # Cursor starts on last used option, but let's navigate to ITEM safely.
    # Take screenshot of the start menu
    img = mgba.take_screenshot()
    print(f"BAG_VERIFICATION_START_MENU: {img}")

if __name__ == "__main__":
    main()
