import time
import sys
import os
import json

# Add current path to import bridge
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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
        time.sleep(0.1)

def buy_safari_ticket():
    print("Buying Safari ticket...")
    # Talk to the clerk at (3, 2) from (3, 3) facing UP
    # Turn up to face clerk
    bridge.press_buttons(["Up", "sleep 200"])
    
    # Press A to start dialog
    bridge.press_buttons(["A", "sleep 600"])
    
    # Mash through dialogue and select YES
    for _ in range(8):
        bridge.press_buttons(["A", "sleep 500"])
        bridge.press_buttons(["B", "sleep 200"])
    
    # Wait for the transition to finish
    time.sleep(1.5)
    print("Safari Zone ticket purchased. Checking position...")

def main():
    pos = get_pos()
    print(f"Starting execution. Current position: {pos}")
    
    # --- PHASE 0: Fuchsia City to Gatehouse ---
    if pos is not None and pos[0] >= 18 and pos[1] >= 4 and pos[1] <= 18:
        print("Starting in Fuchsia City overworld. Navigating to Safari Gatehouse...")
        navigate_to(26, 9)
        navigate_to(19, 9)
        navigate_to(19, 8)
        navigate_to(37, 8)
        navigate_to(37, 2)
        navigate_to(22, 2)
        navigate_to(22, 4)
        navigate_to(18, 4)
        # Transition to Gatehouse
        print("Transitioning into the Gatehouse...")
        walk_step_robust("Up")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position after Phase 0: {pos}")
    
    # --- Inside Safari Gatehouse ---
    # Inside the gatehouse, coordinates are usually (3, 5) or similar
    pos = get_pos()
    if pos is not None and pos[1] > 3 and pos[0] < 10:
        print("Inside Safari Gatehouse. Walking to clerk...")
        navigate_to(3, 3)
        buy_safari_ticket()
        
    pos = get_pos()
    print(f"Position after entering Safari Zone: {pos}")
    
    # --- PHASE 1: Safari Zone Center to Area 1 (East) ---
    # Check if we are in Safari Zone Center (usually around (15, 25))
    pos = get_pos()
    if pos is not None and pos == (15, 25):
        print("In Safari Zone Center. Starting Golden Route Phase 1...")
        navigate_to(15, 22)
        navigate_to(27, 22)
        navigate_to(27, 10)
        # Warp to Area 1
        print("Warping to Area 1 (East)...")
        navigate_to(29, 10)
        # Just walk right once more to trigger warp if not done
        pos = get_pos()
        if pos == (29, 10):
            walk_step_robust("Right")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position after Phase 1: {pos}")
    
    # --- PHASE 2: Area 1 (East) to Area 2 (North) ---
    pos = get_pos()
    if pos is not None and pos[0] <= 5 and pos[1] >= 20:
        print("In Area 1 (East). Starting Golden Route Phase 2...")
        navigate_to(20, 22)
        navigate_to(20, 20)
        navigate_to(12, 20)
        navigate_to(12, 22)
        navigate_to(8, 22)
        navigate_to(8, 8)
        navigate_to(12, 8)
        navigate_to(12, 6)
        navigate_to(17, 6)
        navigate_to(17, 8)
        navigate_to(20, 8)
        navigate_to(20, 3)
        navigate_to(7, 3)
        navigate_to(7, 5)
        # Warp to Area 2
        print("Warping to Area 2 (North)...")
        navigate_to(0, 5)
        pos = get_pos()
        if pos == (0, 5):
            walk_step_robust("Left")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position after Phase 2: {pos}")
    
    # --- PHASE 3: Area 2 (North) to Area 3 (West) ---
    pos = get_pos()
    if pos is not None and pos[0] >= 30 and pos[1] >= 25:
        print("In Area 2 (North). Starting Golden Route Phase 3...")
        navigate_to(22, 31)
        navigate_to(22, 22)
        navigate_to(16, 22)
        navigate_to(16, 28)
        navigate_to(12, 28)
        navigate_to(12, 30)
        navigate_to(8, 30)
        navigate_to(8, 35)
        # Warp to Area 3
        print("Warping to Area 3 (West)...")
        navigate_to(8, 36)
        pos = get_pos()
        if pos == (8, 36):
            walk_step_robust("Down")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position after Phase 3: {pos}")
    
    # --- PHASE 4: Area 3 (West) to Gold Teeth ---
    pos = get_pos()
    if pos is not None and pos[1] <= 5:
        print("In Area 3 (West). Starting Golden Route Phase 4...")
        navigate_to(26, 2)
        navigate_to(25, 2)
        navigate_to(25, 18)
        navigate_to(21, 18)
        navigate_to(21, 23)
        navigate_to(19, 23)
        navigate_to(19, 24)
        navigate_to(18, 24)
        navigate_to(18, 26)
        navigate_to(19, 26)
        
        pos = get_pos()
        if pos == (19, 26):
            print("Arrived at Gold Teeth pick-up location!")
            # Ensure we are facing UP
            bridge.press_buttons(["Up", "sleep 200"])
            # Press A to pick up Gold Teeth
            print("Pressing A to retrieve Gold Teeth...")
            bridge.press_buttons(["A", "sleep 1000"])
            # Dismiss any dialog
            for _ in range(5):
                bridge.press_buttons(["B", "sleep 200"])
                
    pos = get_pos()
    print(f"Final script position: {pos}")

if __name__ == "__main__":
    main()
