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
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    pos = get_pos()
    print(f"Coordinates after dialog handling: {pos}")
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
    print("Closing Trainer Card...")
    bridge.press_buttons(["B", "sleep 500"])
    
    print("Closing START menu...")
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Talk to the clerk at (4,2) from (4,3) facing UP
    print("Talking to clerk...")
    bridge.press_buttons(["Up", "sleep 200", "A", "sleep 600"])
    
    # Buy Safari ticket by pressing A repeatedly (NEVER PRESS B so YES is selected)
    print("Mashing A to buy ticket...")
    attempts = 0
    while attempts < 25:
        pos = get_pos()
        if pos == (15, 25):
            print("Successfully warped to Safari Zone Center!")
            break
        print(f"Still in Gatehouse at {pos}, pressing A...")
        bridge.press_buttons(["A", "sleep 400"])
        attempts += 1
        
    # Walk to Area 1 (East)
    pos = get_pos()
    if pos == (15, 25):
        print("In Safari Zone Center. Starting Phase 1 walk...")
        navigate_to(15, 22)
        navigate_to(27, 22)
        navigate_to(27, 10)
        # Transition to Area 1
        print("Warping to Area 1...")
        navigate_to(29, 10)
        pos = get_pos()
        if pos == (29, 10):
            walk_step_robust("Right")
        time.sleep(1.5)
        
    print(f"Chunk 1 finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
