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
            # Check if we transitioned or got warped
            return
            
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
    pos = get_pos()
    print(f"Starting step exhaustion routine from: {pos}")
    
    # We are at (19, 24). Walk to Row 26: (19, 26)
    navigate_to(19, 26)
    
    # Loop walking back and forth until warped to Gatehouse at (4, 3)
    step_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            # Potential warp or textbox
            for _ in range(5):
                bridge.press_buttons(["B", "sleep 250"])
            pos = get_pos()
            
        if pos is not None and pos[1] < 10 and pos[0] < 10:
            print(f"Successfully arrived in Gatehouse! Position: {pos}")
            break
            
        # Walk back and forth on Row 26
        print(f"Loop {step_count}: Walking to (25, 26)...")
        navigate_to(25, 26)
        
        pos = get_pos()
        if pos is not None and pos[1] < 10 and pos[0] < 10:
            print(f"Successfully arrived in Gatehouse! Position: {pos}")
            break
            
        print(f"Loop {step_count}: Walking to (19, 26)...")
        navigate_to(19, 26)
        
        step_count += 1
        if step_count > 25: # Safe break just in case
            print("Step count limit reached inside script, pausing.")
            break
            
    # Take screenshot of current position
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
