# Robust script to exit the Fuchsia Pokemon Center using waypoints to avoid potted plants.
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
    print("=== EXITING POKEMON CENTER ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (13, 4)
    # Waypoint 1: Walk to (11, 5) (bypasses PC counter)
    if not walk_to(11, 5):
        return
        
    # Waypoint 2: Walk to (11, 6)
    if not walk_to(11, 6):
        return
        
    # Waypoint 3: Walk to (8, 6)
    if not walk_to(8, 6):
        return
        
    # Waypoint 4: Walk to (8, 5)
    if not walk_to(8, 5):
        return
        
    # Waypoint 5: Walk to (3, 5)
    if not walk_to(3, 5):
        return
        
    # Waypoint 6: Walk to (3, 7) (entrance mat)
    if not walk_to(3, 7):
        return
        
    # Step 7: Step DOWN to exit
    print("Stepping DOWN to exit...")
    bridge.press_buttons(["Down", "sleep 1000"])
    pos = get_pos()
    print(f"Final coords outside: {pos}")

if __name__ == "__main__":
    main()
