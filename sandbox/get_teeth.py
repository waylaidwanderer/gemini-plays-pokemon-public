import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

def main():
    print("Pressing Down to face the Gold Teeth at (19, 25)...")
    bridge.press_buttons(["Down", "sleep 500"])
    
    print("Interacting (Pressing A) to pick up the Gold Teeth...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Clearing dialogue boxes (Pressing B)...")
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 250"])

if __name__ == "__main__":
    main()
