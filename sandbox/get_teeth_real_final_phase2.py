import time
import sys
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
        print("Menu active, pressing B...")
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 400"])
    
    new_pos = get_pos()
    if new_pos is None:
        print("Menu active, pressing B...")
        bridge.press_buttons(["B", "sleep 200"])
        return get_pos()
        
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    return new_pos

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
        time.sleep(0.3)

def buy_ticket_and_enter():
    print("Talking to Gatekeeper clerk...")
    # Walk UP to clerk
    for _ in range(3):
        bridge.press_buttons(["Up", "sleep 450"])
    bridge.press_buttons(["Up", "sleep 500", "A", "sleep 1000"])
    
    # Progress dialog and buy ticket (always selecting YES)
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1200"]) # Select YES
    for _ in range(5):
        bridge.press_buttons(["A", "sleep 500"])
    time.sleep(2.0)

def main():
    pos = get_pos()
    print(f"Initial Position: {pos}")
    
    # 1. Walk from (26, 14) through the cut bush to the Gatehouse
    waypoints_to_gate = [
        (26, 8),
        (37, 8),
        (37, 2),
        (22, 2),
        (22, 4),
        (18, 4)
    ]
    
    print("Navigating to Safari Zone Gatehouse...")
    for wp in waypoints_to_gate:
        navigate_to(wp[0], wp[1])
        
    print("Entering Gatehouse and buying ticket...")
    buy_ticket_and_enter()
    
    pos = get_pos()
    print(f"Final Position inside Safari Zone Center: {pos}")

if __name__ == "__main__":
    main()
