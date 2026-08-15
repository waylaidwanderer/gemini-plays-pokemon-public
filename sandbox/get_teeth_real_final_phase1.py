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
    print("Coordinates are None. Handling potential battle or dialogue...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
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
    bridge.press_buttons([direction, "sleep 400"])
    
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
        time.sleep(0.3)

def use_cut():
    print("Executing CUT menu sequence...")
    bridge.press_buttons(["Start", "sleep 500"])
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 1000"]) # POKÉMON
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 800"]) # Select TRUFFLE
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 1500"]) # Select CUT
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])

def main():
    pos = get_pos()
    print(f"Initial Position: {pos}")
    
    # 1. Exit Pokémon Center
    if pos is not None and pos[0] == 5 and pos[1] == 7:
        print("Walking to exit mat (4, 7)...")
        navigate_to(4, 7)
        print("Stepping DOWN to exit...")
        bridge.press_buttons(["Down", "sleep 1500"])
        time.sleep(1.0)
        
    pos = get_pos()
    print(f"Position after exiting Pokémon Center: {pos}")
    
    # 2. Walk to CUT bush in Fuchsia City and CUT it
    if pos == (19, 28):
        print("Walking to CUT bush...")
        waypoints_fuchsia = [
            (24, 28),
            (24, 21),
            (22, 21),
            (22, 14),
            (26, 14)
        ]
        for wp in waypoints_fuchsia:
            navigate_to(wp[0], wp[1])
            
        print("Facing UP towards CUT bush...")
        bridge.press_buttons(["Up", "sleep 500"])
        use_cut()
        time.sleep(1.0)
        
        # Step UP through the cut bush
        print("Stepping UP through CUT bush...")
        walk_step_robust("Up")
        time.sleep(1.0)
        
    pos = get_pos()
    print(f"Final position of Phase 1: {pos}")

if __name__ == "__main__":
    main()
