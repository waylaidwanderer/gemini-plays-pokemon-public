import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step_robust(direction):
    bridge.press_buttons([direction, "sleep 450"])
    return get_pos()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            # Clear text
            bridge.press_buttons(["B", "sleep 250"])
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
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
        else:
            stuck_count = 0
        time.sleep(0.4)

def main():
    pos = get_pos()
    print(f"Starting at: {pos}")
    
    # 1. Step UP to enter Warden's House
    if pos == (27, 28):
        print("Stepping UP to enter Warden's House...")
        bridge.press_buttons(["Up", "sleep 1500"])
        
    pos = get_pos()
    print(f"Position inside Warden's House: {pos}")
    
    # 2. Walk to the Warden at (2, 3)
    if pos == (4, 7):
        print("Navigating to Warden...")
        navigate_to(4, 3)
        navigate_to(2, 3)
        
        # Face UP and talk
        print("Talking to Warden...")
        bridge.press_buttons(["Up", "sleep 500"])
        bridge.press_buttons(["A", "sleep 1500"])
        
        # Clear dialog text or take screenshot of the first dialogue box!
        img = mgba.take_screenshot()
        print(f"Dialogue Screenshot: {img}")
        
        # Keep progressing dialog to see what he says
        for i in range(10):
            bridge.press_buttons(["A", "sleep 1000"])
            
        # Try to clear remaining text boxes with B
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 250"])

if __name__ == "__main__":
    main()
