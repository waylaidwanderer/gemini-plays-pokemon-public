# Script to walk to the PC inside the Pokémon Center and open the Withdraw Item list
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
    bridge.press_buttons([direction, "sleep 350"])
    return get_pos()

def walk_to(tx, ty):
    print(f"Navigating to ({tx}, {ty})...")
    stuck_count = 0
    last_pos = None
    
    while True:
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos == (tx, ty):
            print(f"Arrived at {pos}")
            break
            
        if pos == last_pos:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {pos} while trying to reach ({tx}, {ty})!")
                return False
        else:
            stuck_count = 0
            last_pos = pos
            
        curr_x, curr_y = pos
        if curr_x < tx:
            walk_step("Right")
        elif curr_x > tx:
            walk_step("Left")
        elif curr_y < ty:
            walk_step("Down")
        elif curr_y > ty:
            walk_step("Up")
            
    return True

def main():
    print("=== PC AUDIT START ===")
    pos = get_pos()
    print("Starting at:", pos)
    if pos is None:
        return

    # Walk to (13, 4)
    if not walk_to(13, 4):
        return

    # Face UP to face the PC at (13, 3)
    print("Facing UP to PC...")
    walk_step("Up")
    time.sleep(0.5)

    # Interact with PC
    print("Booting PC...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # "ACE booted up the PC."
    print("Advancing dialogue...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Select ACE's PC (the first option)
    print("Selecting ACE's PC...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Select WITHDRAW ITEM (the first option)
    print("Selecting WITHDRAW ITEM...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("PC Withdraw Item list should be open on next turn!")

if __name__ == "__main__":
    main()
