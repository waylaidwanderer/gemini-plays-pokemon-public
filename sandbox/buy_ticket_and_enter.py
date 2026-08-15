import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    pos = get_pos()
    print(f"Starting final entry phase from: {pos}")
    
    # 1. Clear "We'll call you..." text box
    print("Clearing 'We'll call you...' text box...")
    bridge.press_buttons(["B", "sleep 500"])
    
    # 2. Clear "Our Safari Game..." text box (if any)
    print("Clearing potential final text box...")
    bridge.press_buttons(["B", "sleep 500"])
    
    # 3. Walk LEFT to Column 3
    print("Walking LEFT to Column 3...")
    bridge.press_buttons(["Left", "sleep 500"])
    
    # 4. Walk UP through the warp to enter Safari Zone Center
    print("Walking UP into the Safari Zone warp...")
    bridge.press_buttons(["Up", "sleep 450", "Up", "sleep 1000"])
    
    print(f"Final position inside Safari Zone Center: {get_pos()}")

if __name__ == "__main__":
    main()
