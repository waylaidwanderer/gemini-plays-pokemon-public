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
        bridge.press_buttons(["B", "sleep 150"])
        return get_pos()
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos is None:
         bridge.press_buttons(["B", "sleep 150"])
         return get_pos()
    return new_pos

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            bridge.press_buttons(["B", "sleep 150"])
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
        time.sleep(0.4)

def main():
    pos = get_pos()
    print(f"Starting at: {pos}")
    
    # 1. Walk to PC at (13, 4)
    waypoints = [
        (13, 5),
        (13, 4)
    ]
    print("Navigating to PC...")
    for wp in waypoints:
        navigate_to(wp[0], wp[1])
        
    print("Facing UP towards PC...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # 2. Boot PC and open ACE's PC Withdraw menu
    print("Opening PC Withdraw menu...")
    bridge.press_buttons(["A", "sleep 1200"]) # Turn on PC
    bridge.press_buttons(["A", "sleep 1200"]) # Progress boot text
    bridge.press_buttons(["Down", "sleep 500", "A", "sleep 1200"]) # Select ACE's PC
    bridge.press_buttons(["A", "sleep 1500"]) # Select WITHDRAW ITEM
    
    # 3. Take screenshots of PC Withdraw list and scroll down to see more!
    img1 = mgba.take_screenshot()
    print(f"PC Page 1: {img1}")
    
    # Scroll down 4 times
    for _ in range(4):
        bridge.press_buttons(["Down", "sleep 250"])
    time.sleep(0.5)
    img2 = mgba.take_screenshot()
    print(f"PC Page 2: {img2}")
    
    # Scroll down 4 more times
    for _ in range(4):
        bridge.press_buttons(["Down", "sleep 250"])
    time.sleep(0.5)
    img3 = mgba.take_screenshot()
    print(f"PC Page 3: {img3}")
    
    # Close PC
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
        
    print("PC verification complete.")

if __name__ == "__main__":
    main()
