# Robust script to navigate Fuchsia City from Pokemon Center (19, 28) to the Safari Zone Gatehouse.
# It handles cutting the overworld bush at (26, 13) using TRUFFLE (Paras).
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
    print("=== FUCHSIA CITY TO SAFARI ZONE GATEHOUSE ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # Step 1: Walk to (24, 28)
    if not walk_to(24, 28):
        return
        
    # Step 2: Walk to (24, 21)
    if not walk_to(24, 21):
        return
        
    # Step 3: Walk to (22, 21)
    if not walk_to(22, 21):
        return
        
    # Step 4: Walk to (22, 14)
    if not walk_to(22, 14):
        return
        
    # Step 5: Walk to (26, 14)
    if not walk_to(26, 14):
        return
        
    # Face UP towards the bush at (26, 13)
    print("Facing Up towards the bush at (26, 13)...")
    walk_step("Up")
    time.sleep(0.5)
    
    # Step 6: Cut the bush using TRUFFLE (Paras)
    print("Using CUT...")
    bridge.press_buttons(["Start", "sleep 1000"])
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])  # PKMN
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])  # TRUFFLE (Paras)
    bridge.press_buttons(["A", "sleep 2000"])                       # CUT
    bridge.press_buttons(["A", "sleep 1000"])                       # Advance text
    bridge.press_buttons(["B", "sleep 500"])                        # Back out of menu if any left
    
    # Step 7: Continue walk up Column 26 to Row 9
    if not walk_to(26, 9):
        return
        
    # Step 8: Walk Left to (19, 9)
    if not walk_to(19, 9):
        return
        
    # Step 9: Walk Up to (19, 8)
    if not walk_to(19, 8):
        return
        
    # Step 10: Walk Right to (37, 8)
    if not walk_to(37, 8):
        return
        
    # Step 11: Walk Up to (37, 2)
    if not walk_to(37, 2):
        return
        
    # Step 12: Walk Left to (22, 2)
    if not walk_to(22, 2):
        return
        
    # Step 13: Walk Down to (22, 4)
    if not walk_to(22, 4):
        return
        
    # Step 14: Walk Up to enter Gatehouse at (22, 3)
    print("Entering Gatehouse...")
    bridge.press_buttons(["Up", "sleep 1000"])
    print(f"Inside? Coordinates: {get_pos()}")

if __name__ == "__main__":
    main()
