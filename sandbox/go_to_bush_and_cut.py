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

def use_cut():
    print("Executing CUT menu sequence...")
    # Open Start menu
    bridge.press_buttons(["Start", "sleep 500"])
    # Guarantee cursor at POKÉDEX
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
    # Move to POKÉMON (2nd)
    bridge.press_buttons(["Down", "sleep 400"])
    # Open POKÉMON
    bridge.press_buttons(["A", "sleep 1000"])
    # Select TRUFFLE (2nd Pokémon slot)
    bridge.press_buttons(["Down", "sleep 400"])
    # Select TRUFFLE
    bridge.press_buttons(["A", "sleep 800"])
    # Move cursor to CUT (2nd field move under DIG)
    bridge.press_buttons(["Down", "sleep 400"])
    # Select CUT
    bridge.press_buttons(["A", "sleep 1500"])
    # Clear "TRUFFLE used CUT!" text and menus with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])

def main():
    # Starting at (19, 28)
    waypoints = [
        (24, 28),  # Right to Column 24
        (24, 21),  # Up to Row 21
        (22, 21),  # Left to Column 22
        (22, 14),  # Up to Row 14
        (26, 14)   # Right to Column 26 (standing in front of CUT bush)
    ]
    
    print("Navigating to CUT bush at (26, 13)...")
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    # Stand facing UP
    print("Facing UP towards bush...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Use CUT
    use_cut()
    time.sleep(1.0)
    
    # Take 1 step UP through the cut bush
    print("Walking UP through cut bush...")
    walk_step_robust("Up")
    
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final position after CUT: {pos}")

if __name__ == "__main__":
    main()
