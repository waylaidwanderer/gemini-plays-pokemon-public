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
            # Clear any text boxes with B
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
    # 1. Dismiss battle text box (pressing B once)
    print("Dismissing 'Got away safely!' text box...")
    bridge.press_buttons(["B", "sleep 1000"])
    
    pos = get_pos()
    print(f"Starting overworld walk inside Safari Center. Position: {pos}")
    
    # 2. Walk to Area 1 (East) transition at (29, 10)
    if pos is not None and pos == (27, 15):
        navigate_to(27, 10)
        print("Warping to Area 1 (East)...")
        navigate_to(29, 10)
        pos = get_pos()
        if pos == (29, 10):
            walk_step_robust("Right")
        time.sleep(1.5)
        
    print(f"Safari Center chunk finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
