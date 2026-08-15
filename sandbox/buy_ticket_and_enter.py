import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Mashing B to clear dialogue...")
    # Press B 8 times to clear any remaining dialogue boxes
    for _ in range(8):
        bridge.press_buttons(["B", "sleep 300"])
        
    print("Walking UP to enter the Safari Zone...")
    # Walk UP 2 steps to enter the warp at (4, 0)
    bridge.press_buttons(["Up", "sleep 450", "Up", "sleep 2000"])
    
    pos = get_pos()
    print(f"Current position after entering Safari Zone: {pos}")
    
    screenshot = mgba.take_screenshot()
    print(f"Screenshot taken: {screenshot}")

if __name__ == "__main__":
    main()
