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
    print(f"Starting Phase 1 overworld walk. Position: {pos}")
    
    # --- Inside Safari Center ---
    if pos is not None and pos == (27, 12):
        navigate_to(27, 10)
        # Warp to Area 1 East at (0, 22)
        print("Warping to Area 1 East...")
        navigate_to(29, 10)
        pos = get_pos()
        if pos == (29, 10):
            walk_step_robust("Right")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position inside Area 1 East: {pos}")
    
    # --- Inside Area 1 East ---
    if pos is not None and pos[0] <= 2 and pos[1] >= 20:
        navigate_to(0, 24)
        navigate_to(20, 24)
        navigate_to(20, 22)
        navigate_to(20, 20)  # Climb plateau
        navigate_to(12, 20)
        navigate_to(12, 22)  # Descend plateau
        navigate_to(8, 22)
        navigate_to(8, 8)
        navigate_to(12, 8)
        navigate_to(12, 6)   # Climb northern plateau
        
    print(f"Chunk 2 finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
