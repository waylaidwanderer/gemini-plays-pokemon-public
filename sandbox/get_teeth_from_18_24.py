import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting direct teeth acquisition from (18, 24)...")
    
    # 1. Walk RIGHT to (19, 24)
    print("Walking RIGHT to (19, 24)...")
    bridge.press_buttons(["Right", "sleep 500"])
    
    pos = get_pos()
    print(f"Position: {pos}")
    
    if pos == (19, 24):
        # 2. Turn DOWN to face the Gold Teeth at (19, 25)
        print("Turning DOWN to face the teeth...")
        bridge.press_buttons(["Down", "sleep 300"])
        
        # 3. Press A to interact with the item ball
        print("Pressing A to pick up Gold Teeth...")
        bridge.press_buttons(["A", "sleep 1200"])
        
        # 4. Mash B to clear dialogue
        print("Clearing dialogue...")
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 300"])
            
    pos = get_pos()
    print(f"Final Position: {pos}")

if __name__ == "__main__":
    main()
