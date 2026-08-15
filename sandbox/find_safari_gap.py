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

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos is None:
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
    return new_pos

def main():
    print("Starting gap search script inside Area 3 (West)...")
    # Clear any active menus
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 300"])
        
    pos = get_pos()
    print(f"Current Position: {pos}")
    
    # We are at (15, 24).
    # Let's walk Left on Row 24 and try to go DOWN at each column from 15 down to 10.
    # If we succeed in going Down, we print SUCCESS and the coordinates!
    
    for col in range(15, 9, -1):
        # Navigate to (col, 24)
        pos = get_pos()
        if pos is None:
            continue
            
        print(f"\nProbing Column {col} Row 24...")
        # Walk Left to target column
        while pos[0] > col:
            pos = walk_step_robust("Left")
            if pos is None:
                break
                
        pos = get_pos()
        if pos is None or pos[0] != col or pos[1] != 24:
            print(f"Failed to align to ({col}, 24), we are at {pos}")
            continue
            
        # Try to step DOWN
        print(f"At ({col}, 24), trying to step DOWN...")
        pos_down = walk_step_robust("Down")
        if pos_down is not None and pos_down[1] > 24:
            print(f"FOUND GAP!!! Column {col} Row 25 is WALKABLE! Position reached: {pos_down}")
            # Step back UP to continue searching if desired
            walk_step_robust("Up")
        else:
            print(f"Column {col} Row 25 is BLOCKED.")
            
        time.sleep(0.3)
        
    print("Gap search completed.")

if __name__ == "__main__":
    main()
