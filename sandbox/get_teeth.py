import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

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
    return new_pos

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
        time.sleep(0.1)

def use_dig_safe():
    print("Using DIG to warp out of Safari Zone...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Start", "sleep 500"])
    # Open POKEMON menu (second item slot)
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 1000"]) # POKÉMON
    # Select TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 800"])
    # Select DIG and warp!
    bridge.press_buttons(["A", "sleep 4000"])

def main():
    pos = get_pos()
    print(f"Starting Golden Route to Gold Teeth from: {pos}")
    
    waypoints = [
        (26, 2),
        (25, 2),
        (25, 18),
        (21, 18),
        (21, 23),
        (19, 23),
        (19, 24),
        (18, 24),
        (18, 26),
        (19, 26)
    ]
    
    for i, wp in enumerate(waypoints, 1):
        navigate_to(wp[0], wp[1])
        
    # Arrived at (19, 26). Interact UP to retrieve Gold Teeth!
    print("Standing directly below Gold Teeth. Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    print("Interacting to retrieve Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    print("Clearing textbox after picking up Gold Teeth...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 250"])
        
    use_dig_safe()

if __name__ == "__main__":
    main()
