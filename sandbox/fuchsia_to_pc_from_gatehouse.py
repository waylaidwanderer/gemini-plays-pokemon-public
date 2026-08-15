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

def use_cut():
    print("Standing in front of bush, opening menu to use CUT...")
    # Open menu
    bridge.press_buttons(["Start", "sleep 500"])
    # Select POKÉMON (Down twice, then A)
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 800"])
    # TRUFFLE (Paras) is Pokémon 2. Move Down once, then A
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 600"])
    # Select CUT
    bridge.press_buttons(["A", "sleep 2000"])
    
    # Progress text "TRUFFLE hacked away with CUT!"
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 200"])
    print("CUT sequence finished.")
    time.sleep(1.0)

def main():
    print("Walking from Safari Gatehouse exit to the regrown bush at (26, 12)...")
    
    pos = get_pos()
    print(f"Emerged in Fuchsia City at: {pos}")
    
    # Detour to (26, 12) to cut the bush
    waypoints = [
        (22, 4),
        (22, 2),
        (37, 2),
        (37, 9),
        (26, 9),
        (26, 12) # Stand directly above the regrown bush
    ]
    
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    # Cut the bush
    use_cut()
    print("Phase 1 complete.")

if __name__ == "__main__":
    main()
