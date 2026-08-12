import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_to_row22():
    print("Walking down column 24 to reach Row 22 safely...")
    stuck_count = 0
    
    # We want to reach (24, 22)
    target_y = 22
    
    while True:
        pos = get_pos()
        if pos is None:
            print("Dialogue or battle detected! Exiting safely.")
            return True
            
        cx, cy = pos
        print(f"Current position: ({cx}, {cy})")
        
        if cy == target_y:
            print(f"Reached Row {target_y} successfully!")
            break
            
        if cy > target_y:
            print("ERROR: Overshot target y!")
            return False
            
        # Walk 1 step Down
        print("Walking Down...")
        bridge.press_buttons(["Down", "sleep 350"])
        
        new_pos = get_pos()
        if new_pos is None:
            print("Dialogue or battle detected after movement! Exiting safely.")
            return True
            
        ncx, ncy = new_pos
        if ncx == cx and ncy == cy:
            stuck_count += 1
            print(f"Stuck! Didn't move from ({cx}, {cy}). Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Stuck too long. Battle must have started. Exiting safely.")
                return True
        else:
            stuck_count = 0

if __name__ == "__main__":
    walk_to_row22()
