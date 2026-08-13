# Script to walk from current position (26, 14) to the Safari Zone Gatehouse.
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
    print("=== FUCHSIA CITY TO SAFARI ZONE GATEHOUSE (CONTINUING) ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (26, 14) and the bush at (26, 13) has been cut.
    
    # Step 1: Walk to (26, 9)
    if not walk_to(26, 9):
        return
        
    # Step 2: Walk to (19, 9)
    if not walk_to(19, 9):
        return
        
    # Step 3: Walk to (19, 8)
    if not walk_to(19, 8):
        return
        
    # Step 4: Walk to (37, 8)
    if not walk_to(37, 8):
        return
        
    # Step 5: Walk to (37, 2)
    if not walk_to(37, 2):
        return
        
    # Step 6: Walk to (22, 2)
    if not walk_to(22, 2):
        return
        
    # Step 7: Walk to (22, 4)
    if not walk_to(22, 4):
        return
        
    # Step 8: Walk Up to enter Gatehouse at (22, 3)
    print("Entering Gatehouse...")
    bridge.press_buttons(["Up", "sleep 1000"])
    pos = get_pos()
    print(f"Inside? Coordinates: {pos}")

if __name__ == "__main__":
    main()
