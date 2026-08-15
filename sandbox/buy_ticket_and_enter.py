import time
import sys
import os

# Add current path to import bridge
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return None
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            # We are likely in a text box or battle. But in Safari Center, we shouldn't have any battles or dialogs.
            # However, if we do, B can clear it.
            bridge.press_buttons(["B", "sleep 200"])
            continue
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        print(f"Current: {pos}, Target: ({tx}, {ty})")
        if pos[0] < tx:
            direction = "Right"
        elif pos[0] > tx:
            direction = "Left"
        elif pos[1] < ty:
            direction = "Down"
        elif pos[1] > ty:
            direction = "Up"
            
        new_pos = walk_step_robust(direction)
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Clearing with B...")
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
        else:
            stuck_count = 0
        time.sleep(0.1)

def main():
    print("Mashing A to buy Safari Zone ticket...")
    
    # Loop pressing A until we warp into Safari Zone Center at (15, 25)
    attempts = 0
    while attempts < 25:
        pos = get_pos()
        if pos == (15, 25):
            print("Successfully warped into Safari Zone Center!")
            break
        print(f"Still in Gatehouse dialog. Pressing A... (Attempt {attempts+1})")
        bridge.press_buttons(["A", "sleep 450"])
        attempts += 1
        
    pos = get_pos()
    print(f"Position check after warp: {pos}")
    
    # Walk through Safari Zone Center to Area 1 (East)
    if pos is not None and pos == (15, 25):
        print("Starting Safari Center navigation...")
        navigate_to(15, 22)
        navigate_to(27, 22)
        navigate_to(27, 10)
        # Warp to Area 1
        print("Warping to Area 1 East...")
        navigate_to(29, 10)
        pos = get_pos()
        if pos == (29, 10):
            walk_step_robust("Right")
        time.sleep(1.5)
        
    print(f"Safari ticket and Center navigation finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
