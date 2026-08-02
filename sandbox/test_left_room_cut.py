import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting test_left_room_cut from {pos}")

if pos['x'] == 2 and pos['y'] == 7:
    # Face Down (looking at the cuttable bush at (2, 8))
    print("Turning Down...")
    mgba.press_buttons(['Down'])
    time.sleep(0.3)
    
    # Use CUT
    print("Opening START menu...")
    mgba.press_buttons(['Start'])
    time.sleep(0.5)
    
    # Since cursor is on EXIT (usually), let's move Up 5 times to POKÉMON
    for _ in range(5):
        mgba.press_buttons(['Up'])
        time.sleep(0.2)
        
    mgba.press_buttons(['A'])     # Enter POKÉMON menu
    time.sleep(0.5)
    
    mgba.press_buttons(['Down'])  # Move cursor to TRUFFLE
    time.sleep(0.2)
    mgba.press_buttons(['A'])     # Select TRUFFLE
    time.sleep(0.5)
    
    # TRUFFLE has DIG as 1st option, CUT as 2nd option.
    # Move Down to CUT and select it
    mgba.press_buttons(['Down'])
    time.sleep(0.2)
    mgba.press_buttons(['A'])     # Select CUT
    time.sleep(1.0)
    
    # Dismiss menu
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    
    # Try to walk Down onto (2, 8)
    print("Trying to walk Down onto (2, 8)...")
    pos = move(['Down'])

mgba.take_screenshot()
