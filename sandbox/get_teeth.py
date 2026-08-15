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
    
    # Phase 1: Safari Zone Center
    # Stand position is at (26, 10). Let's navigate to (29, 10) at warp edge
    navigate_to(29, 10)
    print("At warp tile (29, 10). Warping to Area 1...")
    bridge.press_buttons(["Right", "sleep 2000"])
    
    pos = get_pos()
    print(f"Emerged in Area 1 East at: {pos}")
    
    # Phase 2: Area 1 (East)
    waypoints_area1 = [
        (0, 24),
        (20, 24),
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
        navigate_to(wp[0], wp[1])
    print("At warp tile (0, 5). Warping to Area 2...")
    bridge.press_buttons(["Left", "sleep 2000"])
    
    pos = get_pos()
    print(f"Emerged in Area 2 North at: {pos}")
    
    # Phase 3: Area 2 (North)
    waypoints_area2 = [
        (22, 31),
        (22, 23),
        (22, 22),
        (16, 22),
        (16, 27),
        (16, 28),
        (12, 28),
        (12, 30),
        (8, 30),
        (8, 35)
    ]
    for wp in waypoints_area2:
        navigate_to(wp[0], wp[1])
    print("At warp tile (8, 35). Warping to Area 3...")
    bridge.press_buttons(["Down", "sleep 2000"])
    
    pos = get_pos()
    print(f"Emerged in Area 3 West at: {pos}")
    
    # Phase 4: Area 3 (West)
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
        
    print("Arrived at stand position (19, 26). Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    print("Interacting to retrieve Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Dismiss dialogue text boxes
    print("Dismissing dialogue text boxes...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 250"])
        
    # Open START menu
    print("Opening START menu to verify Bag...")
    bridge.press_buttons(["Start", "sleep 500"])
    
    img = mgba.take_screenshot()
    print(f"START_MENU_VERIFICATION: {img}")

if __name__ == "__main__":
    main()
