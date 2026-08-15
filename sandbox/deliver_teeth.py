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
    pos = get_pos()
    print(f"Starting overworld walk to Warden's House. Position: {pos}")
    
    # 1. Walk to Warden's House from (1, 16) via Row 21 and Column 22
    if pos is not None and pos == (1, 16):
        navigate_to(1, 21)
        navigate_to(22, 21)
        navigate_to(22, 14)
        navigate_to(26, 14)
        navigate_to(26, 28)
        navigate_to(27, 28)
        print("Entering Warden's House...")
        walk_step_robust("Up")
        time.sleep(1.5)
        
    # Check if we are inside Warden's House
    pos = get_pos()
    print(f"Position check inside: {pos}")
    
    # Inside Warden's House (warp lands us at (4, 7) or similar)
    if pos is not None and pos[1] == 7 and pos[0] < 10:
        navigate_to(2, 7)
        navigate_to(2, 4)
        
        # Face UP
        print("Facing UP towards the Warden...")
        bridge.press_buttons(["Up", "sleep 250"])
        
        # Talk to the Warden
        print("Talking to the Warden to deliver Gold Teeth...")
        bridge.press_buttons(["A", "sleep 1000"])
        
        # Mash through dialogue to get HM04 (Strength)
        print("Mashing through dialogue...")
        for _ in range(12):
            bridge.press_buttons(["A", "sleep 500"])
            bridge.press_buttons(["B", "sleep 200"])
            
    pos = get_pos()
    print(f"Final Position: {pos}")

if __name__ == "__main__":
    main()
