import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Talking to clerk...")
    # Stand at (4,3) facing UP and press A
    bridge.press_buttons(["Up", "sleep 100"])
    bridge.press_buttons(["A", "sleep 600"])
    
    # Take screenshot 1
    mgba.take_screenshot()
    print("Dialog started.")
    
    # Press A to advance
    bridge.press_buttons(["A", "sleep 600"])
    mgba.take_screenshot()
    
    # Press A to advance
    bridge.press_buttons(["A", "sleep 600"])
    mgba.take_screenshot()

    # Press A to advance
    bridge.press_buttons(["A", "sleep 600"])
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
