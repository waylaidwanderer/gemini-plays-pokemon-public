# Script to dynamically talk to the Safari clerk in the Gatehouse and enter the Safari Zone
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 250"])
    return get_pos()

def walk_to_pos(tx, ty):
    print(f"Walking to ({tx}, {ty})...")
    stuck_count = 0
    last_pos = None
    
    while True:
        pos = get_pos()
        if pos is None:
            # Maybe in dialogue, press B to clear
            bridge.press_buttons(["B", "sleep 200"])
            continue
            
        if pos == (tx, ty):
            return True
            
        if pos == last_pos:
            stuck_count += 1
            if stuck_count > 3:
                print(f"Stuck at {pos} trying to reach ({tx}, {ty})!")
                return False
        else:
            stuck_count = 0
            last_pos = pos
            
        cx, cy = pos
        if cx < tx:
            walk_step("Right")
        elif cx > tx:
            walk_step("Left")
        elif cy < ty:
            walk_step("Down")
        elif cy > ty:
            walk_step("Up")

def try_talk(direction):
    print(f"Facing {direction} and trying to talk...")
    # Face direction
    bridge.press_buttons([direction, "sleep 250"])
    
    # Talk and advance
    bridge.press_buttons(["A", "sleep 800"])
    
    # Press A to progress through the payment dialogue
    for i in range(5):
        bridge.press_buttons(["A", "sleep 1200"])
        
    # Check if we transitioned to Safari Zone Center
    time.sleep(1.0)
    pos = get_pos()
    print(f"Position after interaction: {pos}")
    if pos == (15, 25):
        print("=== SUCCESS! Entered Safari Zone Center! ===")
        return True
    return False

def main():
    print("=== DYNAMIC SAFARI GATEKEEPER INTERACTION ===")
    
    # 1. Walk to (3, 4) which is the corridor
    if not walk_to_pos(3, 4):
        return
        
    # Try different rows facing LEFT
    for test_y in [4, 3, 2]:
        if not walk_to_pos(3, test_y):
            continue
        if try_talk("Left"):
            return
            
    # Try Row 5
    if walk_to_pos(3, 5):
        if try_talk("Left"):
            return
        if try_talk("Up"):
            return
            
    print("All interaction points failed. Please check the screen.")

if __name__ == "__main__":
    main()
