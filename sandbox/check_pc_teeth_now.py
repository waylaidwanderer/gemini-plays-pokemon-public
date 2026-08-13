# Script to select ACE's PC and Withdraw Item menu
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== PC AUDIT: SELECTING ACE'S PC ===")
    
    # 1. Press Down to move to ACE's PC
    bridge.press_buttons(["Down", "sleep 150"])
    
    # 2. Select ACE's PC
    bridge.press_buttons(["A", "sleep 1000"])
    
    # 3. Select Withdraw Item
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Withdraw list should be open. Take a screenshot!")

if __name__ == "__main__":
    main()
