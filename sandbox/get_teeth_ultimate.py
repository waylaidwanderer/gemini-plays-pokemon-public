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
    pos = get_pos()
    print(f"Starting Area 3 Gold Teeth Retrieval from: {pos}")
    
    # 1. Walk LEFT to Column 25: (25, 3)
    navigate_to(25, 3)
    # 2. Walk DOWN Column 25 to Row 18: (25, 18)
    navigate_to(25, 18)
    # 3. Walk LEFT to (21, 18)
    navigate_to(21, 18)
    # 4. Walk DOWN Column 21 to Row 23: (21, 23)
    navigate_to(21, 23)
    # 5. Walk LEFT to (19, 23)
    navigate_to(19, 23)
    # 6. Walk DOWN to (19, 24) (standing directly above the solid teeth)
    navigate_to(19, 24)
    # 7. Walk LEFT to (18, 24) (detour around teeth)
    navigate_to(18, 24)
    # 8. Walk DOWN to (18, 26)
    navigate_to(18, 26)
    # 9. Walk RIGHT to (19, 26) (standing directly below the teeth!)
    navigate_to(19, 26)
    
    # Face UP
    print("Facing UP towards Gold Teeth...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Press A to pick up Gold Teeth!
    print("Pressing A to retrieve Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 300"])
        
    pos = get_pos()
    print(f"Retrieval complete! Final position: {pos}")
    
    img = mgba.take_screenshot()
    print(f"Screenshot of Gold Teeth pickup: {img}")

if __name__ == "__main__":
    main()
