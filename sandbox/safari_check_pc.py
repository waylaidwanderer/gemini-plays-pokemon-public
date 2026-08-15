import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_dialog():
    print("Dialogue or menu active, pressing B...")
    bridge.press_buttons(["B", "sleep 150"])
    return get_pos()

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_dialog()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_dialog()
        
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_dialog()
    return new_pos

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            handle_textbox_or_dialog()
            continue
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
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
    print("Navigating to PC in Pokémon Center...")
    # Safe bypass of NPC at (4, 5)
    waypoints = [
        (3, 6),   # Up 1 step to (3, 6)
        (5, 6),   # Right 2 steps to (5, 6)
        (5, 5),   # Up 1 step to (5, 5)
        (13, 5),  # Right 8 steps to (13, 5)
        (13, 4)   # Up 1 step to PC at (13, 4)
    ]
    
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    # Stand facing UP
    print("Facing UP towards PC...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Boot PC
    print("Booting PC...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Progress boot text
    print("Progressing boot text...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Select ACE's PC (2nd option)
    print("Selecting ACE's PC...")
    bridge.press_buttons(["Down", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Select Withdraw Item (1st option)
    print("Opening Withdraw menu...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    pos = get_pos()
    print(f"Done. Current position (should be None since menu is open): {pos}")

if __name__ == "__main__":
    main()
