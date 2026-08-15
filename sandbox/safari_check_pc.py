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
            bridge.press_buttons(["B", "sleep 200"])
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
    # Starting at (3, 7) inside Pokémon Center
    waypoints = [
        (3, 5),   # Up 2 steps
        (13, 5),  # Right 10 steps
        (13, 4)   # Up 1 step to stand in front of PC
    ]
    
    print("Navigating to PC...")
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    # Stand facing UP
    print("Facing UP towards PC...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Boot PC
    print("Booting PC...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Select PC (A on standard prompt)
    print("Progressing boot text...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Move cursor down to ACE's PC
    print("Selecting ACE's PC...")
    bridge.press_buttons(["Down", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Select Withdraw Item (1st option)
    print("Opening Withdraw menu...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final state reached. Current position (should be None if menu open): {pos}")

if __name__ == "__main__":
    main()
