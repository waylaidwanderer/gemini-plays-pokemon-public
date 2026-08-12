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
    print("=== TESTING SOUTHERN CORRIDOR FOR PATH WEST ===")
    
    # We are currently at (19, 32)
    # Let's try walking Left on Row 33
    # First, let's walk Down to (19, 33)
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    pos = get_pos()
    print("At:", pos)
    
    if pos == (19, 33):
        # Walk Left up to 10 steps to see if we can cross column 15
        print("Walking Left on Row 33...")
        for i in range(10):
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
        pos_after = get_pos()
        print(f"Position after Left on Row 33: {pos_after}")
        
        # Go back to (19, 33)
        if pos_after is not None and pos_after[0] < 19:
            # We moved! Walk back Right
            steps = 19 - pos_after[0]
            for _ in range(steps):
                bridge.press_buttons(["Right"])
                time.sleep(0.5)
                
    # Next, let's walk Down to (19, 34)
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    pos = get_pos()
    print("At:", pos)
    
    if pos == (19, 34):
        # Walk Left up to 10 steps
        print("Walking Left on Row 34...")
        for i in range(10):
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
        pos_after = get_pos()
        print(f"Position after Left on Row 34: {pos_after}")
        
        # Go back to (19, 34)
        if pos_after is not None and pos_after[0] < 19:
            steps = 19 - pos_after[0]
            for _ in range(steps):
                bridge.press_buttons(["Right"])
                time.sleep(0.5)
                
    # Next, let's walk Down to (19, 35)
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    pos = get_pos()
    print("At:", pos)
    
    if pos == (19, 35):
        # Walk Left up to 10 steps
        print("Walking Left on Row 35...")
        for i in range(10):
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
        pos_after = get_pos()
        print(f"Position after Left on Row 35: {pos_after}")
        
        # Go back to (19, 35)
        if pos_after is not None and pos_after[0] < 19:
            steps = 19 - pos_after[0]
            for _ in range(steps):
                bridge.press_buttons(["Right"])
                time.sleep(0.5)

if __name__ == "__main__":
    main()
