import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Progress text with B
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to flee
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
        
    # If we didn't move, let's try pressing B and checking again
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
        
    # Still didn't move? Maybe we ran into a battle that hasn't cleared or there's an obstacle.
    # We will let the greedy loop handle it.
    return new_pos

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                continue
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        # If we have transitioned map, stop!
        # Area 3 (West) has y coordinates near 0 when we transition from Area 2 (North) at (8, 36)
        if pos[1] < 10 and (pos[0] == 26 or pos[0] == 27):
            print(f"Map transition detected! Position is {pos}. Stopping navigation.")
            return True
            
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
        else:
            print("Already at coordinate, but pos != target. Breaking.")
            break
            
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
    return False

def main():
    print("Navigating from current position in Area 2 to Area 3...")
    
    # Starting at current position (should be (22, 25))
    waypoints_area2 = [
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
        transitioned = navigate_to(wp[0], wp[1])
        if transitioned:
            print("Successfully transitioned maps during navigation.")
            return
            
    # Emerge in Area 3 (West) by stepping down
    pos = get_pos()
    if pos == (8, 36):
        print("Stepping down to transition to Area 3 (West)...")
        bridge.press_buttons(["Down", "sleep 1500"])
        time.sleep(1.0)
        pos = get_pos()
        print(f"Emerged in Area 3 (West) at: {pos}")

if __name__ == "__main__":
    main()
