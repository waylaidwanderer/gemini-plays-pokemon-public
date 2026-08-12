import bridge
import time

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos
        bridge.press_buttons(["sleep 50"])
    return None

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
    bridge.press_buttons([direction])
    for _ in range(5):
        bridge.press_buttons(["sleep 100"])
        new_pos = get_pos()
        if new_pos is not None and new_pos != pos:
            return new_pos
    return pos

def run_path(path):
    idx = 0
    stuck_count = 0
    while idx < len(path):
        pos = get_pos()
        if pos is None:
            continue
        print(f"At {pos}, walking {path[idx]}")
        new_pos = walk_step_robust(path[idx])
        if new_pos is None:
            continue
        if new_pos == pos:
            time.sleep(0.5)
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Pressing B...")
                bridge.press_buttons(["B", "sleep 300"])
                stuck_count = 0
        else:
            stuck_count = 0
            idx += 1
    return True

def main():
    print("=== GET TEETH FROM (29, 23) ===")
    pos = get_pos()
    print("Starting position:", pos)
    
    if pos == (29, 23):
        print("Walking Left to Column 19...")
        if not run_path(["Left"] * 10):
            return
            
    pos = get_pos()
    print("Position in Area 3:", pos)
    
    if pos == (19, 23):
        print("Walking Down to (19, 24)...")
        if not run_path(["Down"]):
            return
            
    pos = get_pos()
    print("Final position before pickup:", pos)
    
    if pos == (19, 24):
        print("=== INTERACTING TO PICK UP GOLD TEETH ===")
        # Press Down to face Down, then A to interact, then A to dismiss textbox, then B to close menu
        bridge.press_buttons(["Down", "sleep 500", "A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
        print("Pickup interaction sent.")

if __name__ == "__main__":
    main()
