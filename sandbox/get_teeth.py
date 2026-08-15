import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("No movement detected. Checking for text box or battle...")
    # First, try to clear any dialogue text with B
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
    # Target path from (29, 23)
    # 1. Right to (30, 23)
    # 2. Down 3 steps to (30, 26)
    # 3. Left 11 steps to (19, 26)
    path = ["Right"] + ["Down"] * 3 + ["Left"] * 11
    
    idx = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            continue
            
        print(f"Path step {idx+1}/{len(path)}: currently at {pos}, target direction {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        if new_pos is not None:
            # Check if we actually made progress in the expected direction
            # If we transitioned to a new position, advance the path
            if new_pos != pos:
                idx += 1
            else:
                print("Step failed, retrying...")
        time.sleep(0.5)
        
    print(f"Arrived at destination! Final coordinates: {get_pos()}")

if __name__ == "__main__":
    main()
