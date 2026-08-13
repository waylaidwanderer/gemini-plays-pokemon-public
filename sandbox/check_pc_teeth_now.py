# Script to advance the PC withdrawal text and scroll down to audit remaining PC items
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== PC AUDIT: SCROLLING THROUGH PC ITEMS ===")
    
    # 1. Press A to dismiss "Withdrew TOWN MAP." popup
    bridge.press_buttons(["A", "sleep 800"])
    
    # 2. Press Down 5 times to scroll the PC list down and reveal other items
    for i in range(5):
        bridge.press_buttons(["Down", "sleep 400"])
        
    print("Done! Check the screen next turn to see the rest of the PC inventory.")

if __name__ == "__main__":
    main()
