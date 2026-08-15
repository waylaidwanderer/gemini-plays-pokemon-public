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
    print("Closing PC menu...")
    # Press B multiple times to close the PC menu completely
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 400"])
        
    pos = get_pos()
    print(f"Position after PC close: {pos}")
    
    if pos == (13, 4):
        # Walk LEFT to (3, 4)
        navigate_to(3, 4)
        # Walk DOWN to doormat at (3, 7)
        navigate_to(3, 7)
        # Exit Pokémon Center
        print("Exiting Pokémon Center...")
        bridge.press_buttons(["Down", "sleep 1500"])
        
    pos = get_pos()
    print(f"Outside in Fuchsia City: {pos}")
    
    # 2. Walk to Warden's House at (27, 27)
    if pos == (19, 28):
        print("Navigating to Warden's House...")
        navigate_to(19, 30)
        navigate_to(25, 30)
        navigate_to(30, 30)
        navigate_to(30, 28)
        navigate_to(27, 28)
        # Step into Warden's House door
        print("Entering Warden's House...")
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Inside Warden's House: {pos}")
    
    # 3. Walk to the Warden at (2, 3)
    if pos == (4, 7):
        print("Walking to the Warden...")
        navigate_to(4, 3)
        navigate_to(2, 3)
        
        # Face UP and talk to him
        print("Facing UP and talking to the Warden...")
        bridge.press_buttons(["Up", "sleep 500"])
        bridge.press_buttons(["A", "sleep 1200"])
        
        # Take a screenshot of the dialogue!
        img = mgba.take_screenshot()
        print(f"Dialogue Screenshot: {img}")
        
        # Clear textbox
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 300"])

if __name__ == "__main__":
    main()
