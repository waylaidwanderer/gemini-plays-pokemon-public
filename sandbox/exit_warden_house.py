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

def use_cut_truffle():
    print("Using CUT on the bush...")
    # Open START menu
    bridge.press_buttons(["Start", "sleep 600"])
    
    # Press UP 7 times to guarantee we are at the top (POKÉDEX)
    for _ in range(7):
        bridge.press_buttons(["Up", "sleep 150"])
        
    # Move DOWN 1 time to POKÉMON (2)
    bridge.press_buttons(["Down", "sleep 200", "A", "sleep 1200"])
    
    # Move DOWN 1 time to select TRUFFLE (slot 2)
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"])
    
    # Select CUT (which is the first option, so just press A)
    bridge.press_buttons(["A", "sleep 3000"])
    print("CUT executed.")

def main():
    pos = get_pos()
    print(f"Starting exit and cut script. Position: {pos}")
    
    # 1. Exit Warden's House
    if pos is not None and pos == (2, 7):
        navigate_to(4, 7)
        print("Stepping out of the house...")
        walk_step_robust("Down")
        time.sleep(1.5)
        
    pos = get_pos()
    print(f"Position outside Warden's House: {pos}")
    
    # 2. Walk to the cut bush at (26, 14)
    if pos is not None and pos == (27, 28):
        navigate_to(26, 28)
        navigate_to(26, 21)
        navigate_to(22, 21)
        navigate_to(22, 14)
        navigate_to(26, 14)
        
        # Ensure we face UP towards (26, 13)
        bridge.press_buttons(["Up", "sleep 250"])
        
        # Use CUT
        use_cut_truffle()
        
        # Walk through the cut bush
        navigate_to(26, 12)
        
    print(f"Script finished. Final position: {get_pos()}")

if __name__ == "__main__":
    main()
