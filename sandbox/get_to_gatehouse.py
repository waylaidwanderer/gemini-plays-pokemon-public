import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        print("Menu or text box active, pressing B...")
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 400"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            print("Position is None. Possibly map transition occurred.")
            break
            
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

def use_cut():
    print("Executing CUT menu sequence...")
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    # Down to POKEMON
    bridge.press_buttons(["Down", "sleep 400"])
    # Open POKEMON
    bridge.press_buttons(["A", "sleep 1000"])
    # Down to TRUFFLE (2nd slot)
    bridge.press_buttons(["Down", "sleep 400"])
    # Select TRUFFLE
    bridge.press_buttons(["A", "sleep 800"])
    # Select CUT (1st option)
    bridge.press_buttons(["A", "sleep 1500"])
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])

def main():
    # Starting at (27, 28)
    waypoints_part1 = [
        (30, 28),  # Right 3 to Column 30
        (30, 30),  # Down 2 to Row 30
        (24, 30),  # Left 6 to Column 24
        (24, 21),  # Up 9 to Row 21
        (22, 21),  # Left 2 to Column 22
        (22, 14),  # Up 7 to Row 14
        (26, 14),  # Right 4 to Column 26 (facing the Cut bush at 26,13)
    ]
    
    print("Navigating to the CUT bush...")
    for wp in waypoints_part1:
        navigate_to(wp[0], wp[1])
        
    # Stand facing UP towards the bush at (26, 13)
    print("Making sure player faces UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Use CUT
    use_cut()
    time.sleep(1.0)
    
    # Navigate to Gatehouse
    waypoints_part2 = [
        (26, 9),   # Up 5 steps (through cut bush) to Row 9
        (37, 9),   # Right 11 along Row 9 to Column 37
        (37, 2),   # Up 7 Column 37 to Row 2
        (22, 2),   # Left 15 Row 2 to Column 22
        (22, 4),   # Down 2 Column 22 to Row 4
        (18, 4),   # Left 4 Row 4 to Column 18
        (18, 3)    # Up 1 step to Enter Safari Gatehouse!
    ]
    
    print("\nNavigating to Safari Gatehouse...")
    for wp in waypoints_part2:
        pos = get_pos()
        if pos is None:
            print("Map changed, stopping navigation.")
            break
        # If we enter the gatehouse, coordinates will change to gatehouse interior
        if pos[0] < 10 and pos[1] < 10:
            print("Successfully inside Gatehouse!")
            break
        navigate_to(wp[0], wp[1])
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position inside or near Gatehouse: {pos}")

if __name__ == "__main__":
    main()
