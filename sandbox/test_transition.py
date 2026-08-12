import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is not None:
        return pos[0], pos[1]
    return None

def main():
    print("=== EXPLORING ROUTE 19 TRANSITION ===")
    
    # Let's walk to (23, 35) and see if we can transition to Route 19
    # From (19, 35), walk Right to (23, 35)
    for _ in range(4):
        bridge.press_buttons(["Right"])
        time.sleep(0.5)
        
    pos = get_pos()
    print("At:", pos)
    
    # Now walk Down to transition
    print("Walking Down to transition...")
    for _ in range(4):
        bridge.press_buttons(["Down"])
        time.sleep(0.5)
        
    pos_outside = get_pos()
    print("Position after transition:", pos_outside)
    
    # If we transitioned to Route 19, let's see if we can walk Left and then Up!
    if pos_outside is not None:
        # In Route 19, let's try walking Left
        print("Testing Left on Route 19...")
        for _ in range(15):
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
        pos_left = get_pos()
        print("Position after walking Left:", pos_left)
        
        # Now try walking Up to re-enter Fuchsia City on the west side
        print("Testing Up to re-enter Fuchsia City...")
        for _ in range(10):
            bridge.press_buttons(["Up"])
            time.sleep(0.5)
        pos_up = get_pos()
        print("Position after walking Up:", pos_up)

if __name__ == "__main__":
    main()
