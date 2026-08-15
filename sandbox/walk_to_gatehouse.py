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

def buy_safari_ticket():
    print("Buying Safari ticket...")
    # Turn up to face clerk
    bridge.press_buttons(["Up", "sleep 200"])
    
    # Press A to start dialog
    bridge.press_buttons(["A", "sleep 600"])
    
    # Mash through dialogue and select YES (only pressing A, never B)
    for _ in range(20):
        bridge.press_buttons(["A", "sleep 400"])
    
    # Wait for the transition to finish
    time.sleep(1.5)
    print("Safari Zone ticket purchased. Checking position...")

def main():
    pos = get_pos()
    print(f"Starting walk to Gatehouse. Position: {pos}")
    
    # 1. Walk from (23, 8) in Fuchsia City to the Safari Gatehouse
    if pos is not None and pos == (23, 8):
        navigate_to(23, 9) # detour down to row 9
        navigate_to(37, 9)
        navigate_to(37, 2)
        navigate_to(22, 2)
        navigate_to(22, 4)
        navigate_to(18, 4)
        print("Transitioning into the Gatehouse...")
        walk_step_robust("Up")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position inside Gatehouse check: {pos}")
    
    # Inside Safari Gatehouse: Walk to clerk and buy ticket
    if pos is not None and pos[1] > 3 and pos[0] < 10:
        navigate_to(3, 3)
        buy_safari_ticket()
        
    pos = get_pos()
    print(f"Final position inside Safari Center: {pos}")

if __name__ == "__main__":
    main()
