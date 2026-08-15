import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("No movement detected. Checking for text box or battle...")
    bridge.press_buttons(["B", "sleep 200", "B", "sleep 200"])
    print("Attempting to run from battle...")
    bridge.press_buttons(["Down", "sleep 100", "A", "sleep 1000"])
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
        
    time.sleep(1.0)
    new_pos = get_pos()
    if new_pos == pos:
        return handle_textbox_or_battle()
    return new_pos

def main():
    # Start at (15, 24)
    # Path to (3, 13):
    # 1. Up to (15, 23)
    # 2. Left 12 to (3, 23)
    # 3. Up 10 to (3, 13)
    path = ["Up"] + ["Left"] * 12 + ["Up"] * 10
    
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
                print("No progress made. Retrying...")
                stuck_count += 1
                if stuck_count > 3:
                    bridge.press_buttons(["B", "sleep 300"])
                    stuck_count = 0
        time.sleep(0.5)
        
    print(f"Arrived at (3, 13): {get_pos()}")
    # Take screenshot
    bridge.send_request("/api/screenshot")
    print("Finished.")

if __name__ == "__main__":
    main()
