import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def attempt_dig_sequence(up_presses):
    print(f"Attempting DIG sequence with {up_presses} UP presses from start menu...")
    
    # Ensure any open menu is closed first
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
        
    # Open START menu
    bridge.press_buttons(["Start", "sleep 600"])
    
    # Move cursor up by specified presses
    for _ in range(up_presses):
        bridge.press_buttons(["Up", "sleep 200"])
        
    # Open selected option (hopefully POKéMON)
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Inside POKÉMON menu: Select slot 2 (TRUFFLE / Paras)
    # If we are in the correct menu, pressing DOWN and then A will select TRUFFLE.
    # If we are in the wrong menu (like BAG or Trainer Card), pressing DOWN and A will just select something else or close it.
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 800"])
    
    # If we successfully opened TRUFFLE's options, the cursor is on DIG.
    # Press A to select DIG and use it.
    bridge.press_buttons(["A", "sleep 4000"])
    
    # Check if we successfully warped to Fuchsia City (usually (19, 28) or close to PC)
    pos = get_pos()
    print(f"Position after attempt: {pos}")
    if pos is not None and (pos[0] == 19 or pos[0] == 20 or pos[1] == 28):
        print("DIG successful!")
        return True
        
    print("DIG failed on this attempt. Cleaning up menus with B...")
    return False

def main():
    pos = get_pos()
    print(f"Starting DIG search at: {pos}")
    
    # We will try different starting menu assumptions.
    # Since we checked Trainer Card (ACE, 4th item) last, the cursor is likely on ACE.
    # To go to POKÉMON (2nd item) from ACE (4th item), we press UP 2 times.
    # If the cursor was on POKÉDEX, we press DOWN 1 time (which is UP 6 times).
    # We will try offsets: 2 UP presses, then 6 UP presses, then 0 UP presses, then 1 UP press, etc.
    offsets = [2, 6, 0, 1, 3, 4, 5]
    
    for up_press in offsets:
        if attempt_dig_sequence(up_press):
            print("Successfully returned to Fuchsia City!")
            break
        time.sleep(0.5)

if __name__ == "__main__":
    main()
