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
    # Golden Route:
    # 1. Left 8 to (21, 23)
    # 2. Up 7 to (21, 16) (stairs)
    # 3. Left 15 to (6, 16)
    # 4. Down 4 to (6, 20) (stairs)
    # 5. Left 3 to (3, 20)
    # 6. Down 6 to (3, 26)
    # 7. Right 16 to (19, 26)
    # 8. Up 1 to face UP and bump (19, 25)
    # 9. Press A to pick up Gold Teeth!
    
    path = (
        ["Left"] * 8 +
        ["Up"] * 7 +
        ["Left"] * 15 +
        ["Down"] * 4 +
        ["Left"] * 3 +
        ["Down"] * 6 +
        ["Right"] * 16 +
        ["Up"]
    )
    
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
                # We moved! Advance path index.
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
        
    print(f"Arrived at destination: {get_pos()}. Pressing A to pick up teeth...")
    bridge.press_buttons(["A", "sleep 1000", "B", "sleep 300"])
    print(f"Done! Final coordinates: {get_pos()}")

if __name__ == "__main__":
    main()
