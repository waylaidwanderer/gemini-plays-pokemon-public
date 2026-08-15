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

def main():
    print("Starting eastern gap search script...")
    # Clear any menus
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    pos = get_pos()
    print(f"Current Position: {pos}")
    
    # We are currently at (10, 24).
    # First, let's walk UP to (10, 23) (open grass).
    navigate_to(10, 23)
    
    # Let's walk Right on Row 23 and try to go DOWN at each column from 16 to 29.
    # If we succeed in going Down, we print SUCCESS and the coordinates!
    
    for col in range(16, 30):
        pos = get_pos()
        if pos is None:
            pos = handle_textbox_or_battle()
            if pos is None:
                continue
                
        print(f"\nProbing Column {col} Row 23...")
        # Walk Right to target column
        while pos[0] < col:
            pos = walk_step_robust("Right")
            if pos is None:
                pos = handle_textbox_or_battle()
                break
                
        pos = get_pos()
        if pos is None or pos[0] != col or pos[1] != 23:
            print(f"Failed to align to ({col}, 23), we are at {pos}")
            continue
            
        # Try to step DOWN (to Row 24)
        print(f"At ({col}, 23), trying to step DOWN...")
        pos_down1 = walk_step_robust("Down")
        if pos_down1 is not None and pos_down1[1] == 24:
            print(f"At ({col}, 24), trying to step DOWN to Row 25...")
            pos_down2 = walk_step_robust("Down")
            if pos_down2 is not None and pos_down2[1] == 25:
                print(f"At ({col}, 25), trying to step DOWN to Row 26...")
                pos_down3 = walk_step_robust("Down")
                if pos_down3 is not None and pos_down3[1] == 26:
                    print(f"FOUND COMPLETE GAP!!! Column {col} is FULLY WALKABLE to Row 26! Position reached: {pos_down3}")
                    # Step back UP to continue searching
                    walk_step_robust("Up")
                    walk_step_robust("Up")
                    walk_step_robust("Up")
                else:
                    print(f"Column {col} Row 25 -> Row 26 is BLOCKED.")
                    walk_step_robust("Up")
                    walk_step_robust("Up")
            else:
                print(f"Column {col} Row 24 -> Row 25 is BLOCKED.")
                walk_step_robust("Up")
        else:
            print(f"Column {col} Row 23 -> Row 24 is BLOCKED.")
            
        time.sleep(0.3)
        
    print("Eastern gap search completed.")

if __name__ == "__main__":
    main()
