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

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential dialogue...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    pos = get_pos()
    print(f"Coordinates after dialogue handling: {pos}")
    return pos

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    return new_pos

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
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
    pos = get_pos()
    print(f"Starting detour walk to Safari Gatehouse from: {pos}")
    
    # Detoured path to bypass Hiker at (24, 8)
    waypoints_to_gatehouse = [
        (23, 9),
        (37, 9),
        (37, 2),
        (22, 2),
        (22, 4),
        (18, 4),
        (18, 3)
    ]
    
    for wp in waypoints_to_gatehouse:
        navigate_to(wp[0], wp[1])
        
    print("Entered Gatehouse! Waiting for map transition...")
    time.sleep(2.0)
    
    pos_inside = get_pos()
    print(f"Position inside Gatehouse: {pos_inside}")
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot}")

if __name__ == "__main__":
    main()
