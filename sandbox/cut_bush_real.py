import time
import sys
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Opening POKÉMON menu...")
    # Currently on POKÉMON in Start menu. Press A.
    bridge.press_buttons(["A", "sleep 1000"])
    
    # We are in Choose a POKÉMON menu. Let's make sure we select TRUFFLE (slot 2).
    # Since cursor memory might be on TRUFFLE already, let's align.
    # To be safe, let's take a screenshot to verify cursor, or we can just:
    # In Gen 1, if we just came from using DIG on TRUFFLE, the cursor is pointing to TRUFFLE.
    # Let's press A to select the highlighted Pokémon.
    bridge.press_buttons(["A", "sleep 1000"])
    
    # Now we are in TRUFFLE's options menu.
    # Since TRUFFLE has DIG and CUT, the options are:
    # DIG
    # CUT
    # STATS
    # SWITCH
    # CANCEL
    # Let's press DOWN once to highlight CUT, and press A!
    # Wait, let's make sure we don't accidentally use DIG!
    # If the cursor was not on TRUFFLE, then pressing A might have opened SHELLBY's menu.
    # If we are in SHELLBY's menu, pressing Down once and A will select STATS (since SHELLBY doesn't have DIG/CUT).
    # That is safe and won't use DIG.
    # So let's press Down once, and A!
    bridge.press_buttons(["Down", "sleep 400", "A", "sleep 3000"])
    
    # Clear any textbox with B
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 300"])
        
    pos = get_pos()
    print(f"Position after CUT: {pos}")
    img = mgba.take_screenshot()
    print(f"Screenshot: {img}")

if __name__ == "__main__":
    main()
