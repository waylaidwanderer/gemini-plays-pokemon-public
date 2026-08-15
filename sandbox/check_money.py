import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Opening START menu and moving cursor to top...")
    # Open START menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    # Press UP 7 times to guarantee we are at the top item (POKéDEX)
    for _ in range(7):
        bridge.press_buttons(["Up", "sleep 150"])
        
    print("Cursor at top (POKéDEX). Moving down 3 times to ACE...")
    # Move DOWN 3 times to ACE
    for _ in range(3):
        bridge.press_buttons(["Down", "sleep 150"])
        
    print("Opening Trainer Card...")
    # Press A to open Trainer Card
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Take screenshot of Trainer Card
    mgba.take_screenshot()
    print("Trainer card screenshot taken.")

if __name__ == "__main__":
    main()
