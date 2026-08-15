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
    print("Scanning Row 25-31 on Column 24 for Leftward openings...")
    
    # We are currently at (24, 25)
    # Let's walk Down Column 24 and try to step Left at each row.
    
    for row in range(25, 32):
        # Walk Down to target row
        pos = get_pos()
        while pos[1] < row:
            pos = walk_step_robust("Down")
            if pos is None:
                break
                
        pos = get_pos()
        if pos is None or pos[1] != row:
            print(f"Failed to reach row {row}")
            continue
            
        print(f"At (24, {row}). Probing Left...")
        new_pos = walk_step_robust("Left")
        if new_pos is not None and new_pos[0] < 24:
            print(f"-> Row {row} is OPEN to the Left! Position reached: {new_pos}")
            # Step back Right to continue probing
            walk_step_robust("Right")
        else:
            print(f"-> Row {row} is BLOCKED.")
            
        time.sleep(0.3)
        
    print("Scan complete.")

if __name__ == "__main__":
    main()
