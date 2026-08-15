import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
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
        time.sleep(0.4)

def use_cut_robust():
    print("Executing CUT on bush at (26, 13)...")
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    # Align to POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
    # Select POKÉMON (Down once from POKÉDEX, A)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1200"])
    # Select TRUFFLE slot 2 (assuming cursor starts on slot 1, press Down once, A)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    # Select CUT (first option in menu, press A)
    bridge.press_buttons(["A", "sleep 3000"])
    # Clear any leftover textbox
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])

def main():
    pos = get_pos()
    print(f"Starting end-to-end teeth run from: {pos}")
    
    if pos == (5, 5):
        # We are inside the Pokemon Center. Walk to the exit mat.
        print("Walking to exit...")
        navigate_to(3, 5)
        navigate_to(3, 7)
        # Take the step down to exit
        print("Stepping out of Pokemon Center...")
        bridge.press_buttons(["Down", "sleep 1500"])
        
    pos = get_pos()
    print(f"Coordinates outside: {pos}")
    
    # 2. Walk to Cut-able bush at (26, 14)
    if pos is not None and pos[0] < 26:
        print("Navigating to Cut-able bush...")
        navigate_to(19, 30)
        navigate_to(26, 30)
        navigate_to(26, 14)
        
    # We should be standing at (26, 14) facing UP. Use CUT.
    pos = get_pos()
    if pos == (26, 14):
        use_cut_robust()
        
    # Walk through the cut path
    pos = get_pos()
    if pos == (26, 14):
        print("Walking UP past the cut bush...")
        navigate_to(26, 9)
        
    # Walk to the Safari Gatehouse at (18, 3)
    pos = get_pos()
    if pos is not None and pos[1] == 9:
        print("Walking to Safari Gatehouse...")
        navigate_to(19, 9)
        navigate_to(19, 8)
        navigate_to(37, 8)
        navigate_to(37, 2)
        navigate_to(22, 2)
        navigate_to(22, 4)
        navigate_to(18, 4)
        print("Stepping into Safari Gatehouse...")
        bridge.press_buttons(["Up", "sleep 1500"])

    pos = get_pos()
    print(f"Position in Safari Gatehouse: {pos}")

if __name__ == "__main__":
    main()
