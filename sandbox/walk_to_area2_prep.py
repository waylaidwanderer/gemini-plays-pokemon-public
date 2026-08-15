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
    print(f"Starting Area 2 (North) ground-level walk. Position: {pos}")
    
    # Walk to (22, 31) starting from the ground corridor at (22, 19)
    if pos is not None and pos == (22, 19):
        # Walk RIGHT to Column 25 and DOWN to Row 31 (bypassing the plateau wall at 22, 20)
        navigate_to(25, 19)
        navigate_to(25, 31)
        navigate_to(22, 31)
        
        # Now walk LEFT to transition to Area 3 (West) at (26, 0)
        navigate_to(12, 28)
        navigate_to(12, 30)
        navigate_to(8, 30)
        navigate_to(8, 35)
        print("Warping to Area 3 (West)...")
        navigate_to(8, 36)
        pos = get_pos()
        if pos == (8, 36):
            walk_step_robust("Down")
        time.sleep(1.5)
        
    print(f"Walk to Area 3 finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
