import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Navigating PC menu from boot text...")
    
    # We are currently showing "ACE turned on the PC."
    # Press A to progress
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Now we see the menu:
    # BILL's PC
    # ACE's PC
    # PROF. OAK's PC
    # LOG OFF
    # Press DOWN once to highlight ACE's PC, then A to select
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 1200"])
    
    # Now we are inside ACE's PC menu:
    # WITHDRAW ITEM
    # DEPOSIT ITEM
    # TOSS ITEM
    # LOG OFF
    # Press A to select WITHDRAW ITEM (first option)
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Take screenshot of page 1 of Withdraw Item
    p1 = mgba.take_screenshot()
    print(f"PC Page 1: {p1}")
    
    # Scroll down 6 times, taking screenshots of each item
    for i in range(6):
        bridge.press_buttons(["Down", "sleep 400"])
        p = mgba.take_screenshot()
        print(f"PC Scroll {i+1}: {p}")
        
    # Close PC safely by pressing B multiple times
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 400"])

if __name__ == "__main__":
    main()
