import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

PHASE_FILE = "current_phase.txt"

def get_saved_phase():
    if os.path.exists(PHASE_FILE):
        try:
            with open(PHASE_FILE, "r") as f:
                return int(f.read().strip())
        except Exception:
            pass
    return 1

def save_phase(phase):
    try:
        with open(PHASE_FILE, "w") as f:
            f.write(str(phase))
        print(f"Saved phase {phase} to {PHASE_FILE}")
    except Exception as e:
        print(f"Error saving phase: {e}")

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
    
    # Dynamic sleep: 1100ms for stair tiles, 600ms for standard tiles
    stair_tiles = [(20, 21), (12, 21), (12, 7), (17, 7), (22, 23), (16, 27), (21, 17), (6, 19)]
    sleep_time = 1100 if pos in stair_tiles else 600
    
    bridge.press_buttons([direction, f"sleep {sleep_time}"])
    
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
    # Pre-emptively clear any active battle/textbox
    print("Dismissing any active battle or dialogue textbox...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    
    pos = get_pos()
    print(f"Starting actual walkable route to Gold Teeth from: {pos}")
    
    # Load or initialize phase
    current_phase = get_saved_phase()
    if not os.path.exists(PHASE_FILE) and pos is not None:
        x, y = pos
        if x == 5 and y == 22:
            current_phase = 2
        elif x == 15 and y == 24:
            current_phase = 2
        elif x == 12 and (y == 21 or y == 22):
            current_phase = 2
        elif x == 0 and (y == 22 or y == 23 or y == 24):
            current_phase = 2
        elif x == 39 and y == 31:
            current_phase = 3
        elif x == 26 and y == 0:
            current_phase = 4
        save_phase(current_phase)
        
    print(f"Loaded starting Phase: {current_phase}")
    
    # Phase 1: Safari Zone Center
    if current_phase <= 1:
        navigate_to(29, 10)
        print("At warp tile (29, 10). Warping to Area 1...")
        bridge.press_buttons(["Right", "sleep 2000"])
        save_phase(2)
        
        pos = get_pos()
        print(f"Emerged in Area 1 East at: {pos}")
    
    # Phase 2: Area 1 (East)
    if current_phase <= 2:
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
        
        # Filter waypoints that we have already completed in Area 1 East
        current_p = get_pos()
        if current_p is not None:
            cx, cy = current_p
            if cy == 3:
                print(f"Bypassing completed Area 1 waypoints up to (20, 3) as we are on Row 3: {current_p}")
                waypoints_area1 = waypoints_area1[14:] # Start directly from (7, 3)
            elif cx == 8 and cy == 8:
                print(f"Bypassing completed Area 1 waypoints up to (8, 8) as we are at {current_p}")
                waypoints_area1 = waypoints_area1[8:] # Start directly from (12, 8)
            elif (cy == 22 and cx <= 12 and cx >= 8) or (cy == 21 and cx == 12):
                print(f"Bypassing completed Area 1 waypoints as we are at {current_p}")
                waypoints_area1 = waypoints_area1[6:] # Start directly from (8, 22)
                
        for wp in waypoints_area1:
            navigate_to(wp[0], wp[1])
        print("At warp tile (0, 5). Warping to Area 2...")
        bridge.press_buttons(["Left", "sleep 2000"])
        save_phase(3)
        
        pos = get_pos()
        print(f"Emerged in Area 2 North at: {pos}")
    
    # Phase 3: Area 2 (North)
    if current_phase <= 3:
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
        
        # Filter waypoints that we have already completed in Area 2 North
        current_p = get_pos()
        if current_p is not None:
            cx, cy = current_p
            if cx == 22 and cy <= 31 and cy >= 23:
                print(f"Bypassing completed Area 2 waypoints as we are at {current_p}")
                waypoints_area2 = waypoints_area2[1:] # Start directly from (22, 23)
                
        for wp in waypoints_area2:
            navigate_to(wp[0], wp[1])
        print("At warp tile (8, 35). Warping to Area 3...")
        bridge.press_buttons(["Down", "sleep 2000"])
        save_phase(4)
        
        pos = get_pos()
        print(f"Emerged in Area 3 West at: {pos}")
    
    # Phase 4: Area 3 (West)
    if current_phase <= 4:
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
        
        # Filter waypoints that we have already completed in Area 3 West
        current_p = get_pos()
        if current_p is not None:
            cx, cy = current_p
            if cx == 25 and cy <= 18 and cy >= 2:
                print(f"Bypassing completed Area 3 waypoints as we are at {current_p}")
                waypoints_area3 = waypoints_area3[2:] # Start directly from (25, 18)
                
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
        
        # Delete the phase file as we are done
        if os.path.exists(PHASE_FILE):
            os.remove(PHASE_FILE)

if __name__ == "__main__":
    main()
