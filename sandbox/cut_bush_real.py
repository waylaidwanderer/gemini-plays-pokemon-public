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

def use_cut_menu():
    print("Opening menu to use CUT...")
    bridge.press_buttons(["B", "sleep 250", "B", "sleep 250"])
    bridge.press_buttons(["Start", "sleep 500"])
    # Open POKEMON (second option)
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 1000"])
    # Select TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 250", "A", "sleep 800"])
    # Select CUT (usually first custom move or in menu)
    bridge.press_buttons(["A", "sleep 3000"])
    # Dismiss any leftover textboxes
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 250"])

def main():
    pos = get_pos()
    print(f"Starting walk to cut bush and enter Safari Gatehouse from: {pos}")
    
    # 1. Walk to the bush at (26, 14)
    waypoints_to_bush = [
        (30, 28),
        (30, 30),
        (24, 30),
        (24, 21),
        (22, 21),
        (22, 14),
        (26, 14)
    ]
    
    for wp in waypoints_to_bush:
        navigate_to(wp[0], wp[1])
        
    # Stand at (26, 14) facing UP (north) towards the bush at (26, 13)
    print("Standing at (26, 14). Facing UP...")
    bridge.press_buttons(["Up", "sleep 500"])
    
    # Use CUT
    use_cut_menu()
    
    # 2. Walk to the Gatehouse at (18, 3)
    waypoints_to_gatehouse = [
        (26, 9),
        (19, 9),
        (19, 8),
        (37, 8),
        (37, 2),
        (22, 2),
        (22, 4),
        (18, 4),
        (18, 3)
    ]
    
    for wp in waypoints_to_gatehouse:
        navigate_to(wp[0], wp[1])
        
    print("Arrived at the Gatehouse entrance!")

if __name__ == "__main__":
    main()
