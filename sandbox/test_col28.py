import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_up_col28():
    print("Starting Column 28 upward probe...")
    stuck_count = 0
    target_y = 10
    
    while True:
        pos = get_pos()
        if pos is None:
            print("Dialogue or battle detected! Exiting safely.")
            return True
            
        cx, cy = pos
        print(f"Current position: ({cx}, {cy})")
        
        if cy == target_y:
            print("REACHED ROW 10! The ground corridor to the East is open!")
            break
            
        if cy < target_y:
            print("Overshot target row!")
            break
            
        # Walk 1 step Up
        print("Walking Up...")
        bridge.press_buttons(["Up", "sleep 350"])
        
        new_pos = get_pos()
        if new_pos is None:
            print("Dialogue or battle detected after movement! Exiting safely.")
            return True
            
        ncx, ncy = new_pos
        if ncx == cx and ncy == cy:
            stuck_count += 1
            print(f"Stuck! Didn't move from ({cx}, {cy}). Stuck count: {stuck_count}")
            if stuck_count > 3:
                print("Stuck too long. Blocked by solid obstacle or battle started. Exiting safely.")
                return True
        else:
            stuck_count = 0

if __name__ == "__main__":
    walk_up_col28()
