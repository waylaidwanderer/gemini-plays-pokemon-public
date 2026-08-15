import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def use_dig_from_bag():
    print("Using DIG from the current Bag screen...")
    # 1. Close Bag (B) and return to Start menu
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 500"])
    
    # Start menu is open. Move cursor to POKEMON (second option)
    # Since cursor was on ITEM when opening, let's just go UP once to POKEMON!
    bridge.press_buttons(["Up", "sleep 250", "A", "sleep 1000"])
    
    # Select TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 800"])
    
    # Select DIG (first option in TRUFFLE menu)
    bridge.press_buttons(["A", "sleep 4000"])
    
    pos = get_pos()
    print(f"Warped out to: {pos}")

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        print("Position is None. Pressing B...")
        bridge.press_buttons(["B", "sleep 200"])
        pos = get_pos()
        if pos is None:
            return None
            
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    new_pos = get_pos()
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
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
        time.sleep(0.05)

def main():
    use_dig_from_bag()
    
    pos = get_pos()
    if pos != (19, 28):
        print(f"Warning: Expected to warp to (19, 28) but got {pos}")
        
    # 2. Walk to the Warden's House door at (27, 27)
    waypoints_to_house = [
        (19, 30),
        (30, 30),
        (30, 28),
        (27, 28),
        (27, 27) # Door transition
    ]
    
    for wp in waypoints_to_house:
        navigate_to(wp[0], wp[1])
        
    print("Entered Warden's House! Waiting for map transition...")
    time.sleep(2.0)
    
    pos_inside = get_pos()
    print(f"Inside Warden's House at: {pos_inside}")
    
    # 3. Walk to the Warden at (2, 4) facing UP
    waypoints_inside = [
        (2, 7),
        (2, 4)
    ]
    
    for wp in waypoints_inside:
        navigate_to(wp[0], wp[1])
        
    # Stand at (2, 4) and face UP
    print("Standing at (2, 4). Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Talk to the Warden!
    print("Interacting with the Warden...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Mash B to advance through all dialogue boxes and receive HM04
    print("Mashing B to clear dialogue and receive HM04 (Strength)...")
    for _ in range(12):
        bridge.press_buttons(["B", "sleep 300"])
        
    # Open START menu to verify Bag
    print("Opening START menu to verify HM04...")
    bridge.press_buttons(["Start", "sleep 500"])
    
    img = mgba.take_screenshot()
    print(f"FINAL_WARDEN_HM04_VERIFICATION: {img}")

if __name__ == "__main__":
    main()
