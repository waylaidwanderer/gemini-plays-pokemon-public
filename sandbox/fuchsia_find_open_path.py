import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        bridge.press_buttons(["B", "sleep 150"])
        return get_pos()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    return get_pos()

def main():
    print("Scanning Row 22 collisions from Columns 18 to 22...")
    
    # We are currently at (22, 21)
    # Let's walk Left along Row 21 to Column 18, and try to step Down at each column!
    
    open_cols = []
    
    for col in range(22, 17, -1):
        # Walk Left to the target column
        pos = get_pos()
        while pos[0] > col:
            pos = walk_step_robust("Left")
            if pos is None:
                break
                
        pos = get_pos()
        if pos is None or pos[0] != col:
            print(f"Failed to reach column {col}")
            continue
            
        print(f"At ({col}, 21). Probing Down...")
        new_pos = walk_step_robust("Down")
        if new_pos is not None and new_pos[1] == 22:
            print(f"-> Column {col} is OPEN to Row 22!")
            open_cols.append(col)
            # Step back Up to continue probing
            walk_step_robust("Up")
        else:
            print(f"-> Column {col} is BLOCKED.")
            
        time.sleep(0.3)
        
    print(f"Scan complete. Open columns on Row 22: {open_cols}")

if __name__ == "__main__":
    main()
