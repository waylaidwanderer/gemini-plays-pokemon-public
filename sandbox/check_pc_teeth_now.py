# Script to select ACE's PC and open Withdraw Item menu
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== PC AUDIT: SELECTING ACE'S PC ===")
    
    # 1. Select ACE's PC (since we are already pointing at it, and the 'Accessed Item Storage System' text is open)
    # We must press A to advance dialogue first!
    # Wait, let's look at the screen: "Accessed Item Storage System." is at the bottom with a black arrow.
    # So we must press A to advance the text first, then A to select ACE's PC, then A to select WITHDRAW ITEM!
    # Let's do:
    # A (advance dialogue) -> sleep 800
    # A (select ACE's PC) -> sleep 800
    # A (select WITHDRAW ITEM) -> sleep 800
    bridge.press_buttons(["A", "sleep 800"])
    bridge.press_buttons(["A", "sleep 800"])
    bridge.press_buttons(["A", "sleep 800"])
    
    print("Withdraw list should be open!")

if __name__ == "__main__":
    main()
