import time
import sys
import os

# Add current path to import bridge
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

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
    
    # Try to RUN from battle
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

def main():
    pos = get_pos()
    print(f"Starting walk to Area 2 (North) southern corridor. Position: {pos}")
    
    # --- Inside Area 1 East ---
    if pos is not None and pos == (12, 6):
        navigate_to(17, 6)
        navigate_to(17, 8)  # descend stairs
        navigate_to(20, 8)
        navigate_to(20, 3)
        navigate_to(7, 3)
        navigate_to(7, 5)
        # Warp to Area 2 (North)
        print("Warping to Area 2 (North)...")
        navigate_to(0, 5)
        pos = get_pos()
        if pos == (0, 5):
            walk_step_robust("Left")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position check after Area 1 walk: {pos}")
    
    # --- Inside Area 2 North ---
    if pos is not None and pos[0] >= 30 and pos[1] >= 25:
        print("Entering Area 2 (North) southern corridor walk...")
        navigate_to(22, 31)
        
    print(f"Walk to (22, 31) finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
