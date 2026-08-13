# Completely robust script using loop-based pathing to reach the Fuchsia Pokemon Center.
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
            if stuck_count > 5:
                print(f"Stuck at {pos} while trying to reach ({target_x}, {target_y})! Aborting to prevent infinite loops.")
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
    print("=== ROBUST LOOP-BASED PATHING TO POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (1, 27)
    # Step 1: Walk to (1, 32)
    if not walk_to(1, 32):
        return
        
    # Step 2: Walk to (6, 32)
    if not walk_to(6, 32):
        return
        
    # Step 3: Walk to (6, 28)
    if not walk_to(6, 28):
        return
        
    # Step 4: Walk to (19, 28)
    if not walk_to(19, 28):
        return
        
    # Step 5: Walk to (19, 27) to enter
    print("Entering Pokemon Center...")
    walk_step("Up")
    time.sleep(1.0)
    pos = get_pos()
    print(f"Final Coords: {pos}")
    time.sleep(1.0)
    print(f"Inside? Coords: {get_pos()}")

if __name__ == "__main__":
    main()
