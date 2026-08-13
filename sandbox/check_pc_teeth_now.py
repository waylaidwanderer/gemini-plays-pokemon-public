# Script to recover from Bill's PC and open Ace's PC item withdrawal menu
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== RECOVERING FROM BILL'S PC TO ACE'S PC ===")
    
    # Dismiss "There are no Pokemon here!" popup
    bridge.press_buttons(["B", "sleep 800"])
    
    # Exit Bill's PC (either by pressing B or selecting SEE YA!)
    bridge.press_buttons(["B", "sleep 1200"])
    
    # We should be back at the main PC menu:
    # BILL's PC
    # ACE's PC
    # PROF. OAK's PC
    # LOG OFF
    
    # Move down to ACE's PC and select it
    bridge.press_buttons(["Down", "sleep 200"])
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Select WITHDRAW ITEM
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Ace's PC item withdraw list should now be open!")

if __name__ == "__main__":
    main()
