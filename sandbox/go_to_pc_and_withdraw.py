# Robust script to walk to the PC, boot it up, go to ACE's PC, and select WITHDRAW ITEM.
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
    print("=== NAVIGATING TO PC AND OPENING ACE'S STORAGE ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (3, 7)
    # Walk to (3, 5)
    if not walk_to(3, 5):
        return
        
    # Walk to (13, 5)
    if not walk_to(13, 5):
        return
        
    # Walk to (13, 4)
    if not walk_to(13, 4):
        return
        
    # Face Up
    print("Facing Up to PC...")
    walk_step("Up")
    time.sleep(1.0)
    
    # Interacting with PC
    print("Pressing A to boot PC...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Pressing A to advance boot dialogue...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Selecting ACE's PC...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Selecting WITHDRAW ITEM...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Done! Let's check the screen next turn.")

if __name__ == "__main__":
    main()
