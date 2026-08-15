import time
import sys
import os

# Add current path to import bridge
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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
        return None
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            return None
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
    # 1. Dismiss CUT text box (pressing B once)
    print("Dismissing 'TRUFFLE hacked away with CUT!' text box...")
    bridge.press_buttons(["B", "sleep 1000"])
    
    pos = get_pos()
    print(f"Starting overworld walk. Position: {pos}")
    
    # Walk to (37, 2) in Fuchsia City overworld
    if pos is not None and pos == (26, 14):
        navigate_to(26, 12)
        navigate_to(26, 9)
        navigate_to(19, 9)
        navigate_to(19, 8)
        navigate_to(37, 8)
        navigate_to(37, 2)
        
    print(f"Chunk 1 finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
