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
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
    return get_pos()

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
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
        time.sleep(0.4)

def main():
    # 1. Use DIG to warp out of the Safari Zone
    print("Step 1: Using DIG to warp out...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    bridge.press_buttons(["Start", "sleep 500"])
    for _ in range(6):
        bridge.press_buttons(["Up", "sleep 200"])
    bridge.press_buttons(["Down", "sleep 250", "Down", "sleep 250", "A", "sleep 1000"]) # POKÉMON
    for _ in range(5):
        bridge.press_buttons(["Up", "sleep 250"])
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 800"]) # TRUFFLE (slot 2)
    bridge.press_buttons(["A", "sleep 4000"]) # Select DIG and wait for warp!
    
    pos = get_pos()
    print(f"Warped! Position outside: {pos}")
    
    # 2. Enter the Pokémon Center
    if pos == (19, 28):
        print("Step 2: Entering Pokémon Center...")
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Position inside Pokémon Center: {pos}")
    
    # 3. Navigate to the PC at (13, 4)
    # Emerge inside at columns 3-4, row 8. Let's use robust navigation waypoints:
    if pos is not None and pos[1] >= 7:
        print("Step 3: Navigating to PC...")
        waypoints_pc = [
            (5, 5),    # Walk Up/Right to Column 5 Row 5
            (13, 5),   # Walk Right along Row 5 to Column 13
            (13, 4)    # Walk Up 1 step to stand in front of PC
        ]
        for wp in waypoints_pc:
            navigate_to(wp[0], wp[1])
            
        print("Facing UP towards PC...")
        bridge.press_buttons(["Up", "sleep 500"])
        
        # 4. Open the PC menu and go to Withdraw Item
        print("Step 4: Opening PC menu...")
        bridge.press_buttons(["A", "sleep 1200"]) # Turn on PC
        bridge.press_buttons(["A", "sleep 1200"]) # Progress boot text
        bridge.press_buttons(["Down", "sleep 500", "A", "sleep 1200"]) # Select ACE's PC
        bridge.press_buttons(["A", "sleep 1500"]) # Select WITHDRAW ITEM
        
    time.sleep(2.0)
    pos = get_pos()
    print(f"Final Position (should be None inside menu): {pos}")
    
    # Take screenshot of final screen (which should be the PC Withdraw Item menu!)
    img = mgba.take_screenshot()
    print(f"Screenshot of PC menu: {img}")

if __name__ == "__main__":
    main()
