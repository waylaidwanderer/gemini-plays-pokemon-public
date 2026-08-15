import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("No movement detected. Checking for text box or battle...")
    # Try to clear any dialogue text with B
    bridge.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    
    # Try to flee: press Down, then A
    print("Attempting to run from battle...")
    bridge.press_buttons(["Down", "sleep 100", "A", "sleep 1000"])
    
    # Check if we are back in the overworld
    pos = get_pos()
    print(f"Coordinates after flee attempt: {pos}")
    return pos

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 350"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    # If position is same, wait a bit and check again
    time.sleep(1.0)
    new_pos = get_pos()
    if new_pos == pos:
        return handle_textbox_or_battle()
    return new_pos

def main():
    # Start at (3, 23)
    # Path:
    # 1. Right 18 to (21, 23)
    # 2. Down 1 to (21, 24)
    # 3. Left 2 to (19, 24)
    path = ["Right"] * 18 + ["Down"] + ["Left"] * 2
    
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            continue
            
        print(f"Path step {idx+1}/{len(path)}: currently at {pos}, target direction {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        if new_pos is not None:
            if new_pos != pos:
                idx += 1
                stuck_count = 0
            else:
                print("No progress made. Retrying step...")
                stuck_count += 1
                if stuck_count > 3:
                    print("Repeated stuck! Clearing with B.")
                    bridge.press_buttons(["B", "sleep 300"])
                    stuck_count = 0
        time.sleep(0.5)
        
    print(f"Arrived at (19, 24): {get_pos()}")
    
    # Force facing Down
    print("Facing Down...")
    bridge.press_buttons(["Down", "sleep 500"])
    
    # Press A to pick up item
    print("Pressing A to pick up Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Take screenshot of the result to verify
    screenshot = bridge.send_request("/api/screenshot")
    print("Finished pickup attempt.")

if __name__ == "__main__":
    main()
