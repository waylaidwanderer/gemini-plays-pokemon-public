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
    # Align to POKÉDEX (press UP 6 times to wrap/ensure starting point)
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 150"])
    # Select POKÉMON (Down once from POKÉDEX, A)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1200"])
    # Select TRUFFLE slot 2 (press Down once, A)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    # Select CUT (first option in menu, press A)
    bridge.press_buttons(["A", "sleep 3000"])
    # Clear any leftover textbox
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])

def main():
    pos = get_pos()
    print(f"Starting Phase 1 from: {pos}")
    
    # Walk around the horizontal fence:
    # 1. Left to Column 24
    # 2. Up to Row 21
    # 3. Left to Column 22
    # 4. Up to Row 14
    # 5. Right to Column 26 (standing directly below the bush at 26,13)
    print("Navigating to Cut-able bush at (26, 14)...")
    navigate_to(24, 30)
    navigate_to(24, 21)
    navigate_to(22, 21)
    navigate_to(22, 14)
    navigate_to(26, 14)
    
    # We should be standing at (26, 14) facing UP. Use CUT.
    pos = get_pos()
    if pos == (26, 14):
        use_cut_robust()
        
    # Walk through the cut path to (26, 9)
    pos = get_pos()
    if pos == (26, 14):
        print("Walking UP past the cut bush...")
        navigate_to(26, 9)
        
    pos = get_pos()
    print(f"Phase 1 complete! Final position: {pos}")

if __name__ == "__main__":
    main()
