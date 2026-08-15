import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_dialog():
    print("Dialogue or textbox active, pressing B...")
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
    print("Executing Phase 2: Walking from (26, 12) to Pokémon Center...")
    
    # Dismiss the "TRUFFLE hacked away with CUT!" dialogue box
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 250"])
        
    pos = get_pos()
    print(f"Current position in overworld: {pos}")
    
    pc_waypoints = [
        (26, 14), # Walk through cut bush
        (22, 14),
        (22, 21),
        (24, 21),
        (24, 28),
        (19, 28),
        (19, 27) # Outside Pokémon Center door
    ]
    
    for wp in pc_waypoints:
        navigate_to(wp[0], wp[1])
        
    # Enter Pokémon Center
    print("Entering Pokémon Center...")
    walk_step_robust("Up")
    time.sleep(1.5)
    
    pos = get_pos()
    print(f"Inside Pokémon Center: {pos}")

if __name__ == "__main__":
    main()
