# Script to walk from current position (23, 8) to the Safari Zone Gatehouse via Row 9 horizontal path.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 250"])
    return get_pos()

def walk_to(target_x, target_y):
    print(f"Navigating to ({target_x}, {target_y})...")
    stuck_count = 0
    last_pos = None
    
    while True:
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos == (target_x, target_y):
            print(f"Arrived at {pos}")
            break
            
        if pos == last_pos:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {pos} while trying to reach ({target_x}, {target_y})!")
                return False
        else:
            stuck_count = 0
            last_pos = pos
            
        curr_x, curr_y = pos
        if curr_x < target_x:
            walk_step("Right")
        elif curr_x > target_x:
            walk_step("Left")
        elif curr_y < target_y:
            walk_step("Down")
        elif curr_y > target_y:
            walk_step("Up")
            
    return True

def main():
    print("=== FUCHSIA CITY TO SAFARI ZONE GATEHOUSE (DETOURING VIA ROW 9) ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (23, 8)
    # Step 1: Walk Down to Row 9
    if not walk_to(23, 9):
        return
        
    # Step 2: Walk Right on Row 9 to Column 37
    if not walk_to(37, 9):
        return
        
    # Step 3: Walk Up Column 37 to Row 2
    if not walk_to(37, 2):
        return
        
    # Step 4: Walk Left on Row 2 to Column 22
    if not walk_to(22, 2):
        return
        
    # Step 5: Walk Down to Column 22 Row 4
    if not walk_to(22, 4):
        return
        
    # Step 6: Walk Up to enter Gatehouse at (22, 3)
    print("Entering Gatehouse...")
    bridge.press_buttons(["Up", "sleep 1000"])
    pos = get_pos()
    print(f"Inside? Coordinates: {pos}")

if __name__ == "__main__":
    main()
