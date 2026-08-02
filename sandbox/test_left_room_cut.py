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
    
    # Open START menu
    print("Opening START menu...")
    mgba.press_buttons(['Start'])
    time.sleep(0.5)
    
    # Reset cursor to POKÉDEX at the top (Up 7 times)
    print("Resetting cursor to top...")
    for _ in range(7):
        mgba.press_buttons(['Up'])
        time.sleep(0.1)
        
    # Move Down 1 time to POKÉMON
    print("Selecting POKÉMON...")
    mgba.press_buttons(['Down'])
    time.sleep(0.2)
    mgba.press_buttons(['A'])
    time.sleep(0.5)
    
    # Move Down 1 time to select TRUFFLE (the 2nd Pokémon)
    print("Selecting TRUFFLE...")
    mgba.press_buttons(['Down'])
    time.sleep(0.2)
    mgba.press_buttons(['A'])
    time.sleep(0.5)
    
    # Move Down 1 time to select CUT (the 2nd option, after DIG)
    print("Selecting CUT...")
    mgba.press_buttons(['Down'])
    time.sleep(0.2)
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    
    # Close any open dialogs/menus (Press B 3 times)
    print("Closing menus...")
    for _ in range(3):
        mgba.press_buttons(['B'])
        time.sleep(0.3)
        
    # Walk Down onto (2, 8)
    print("Trying to walk Down onto (2, 8)...")
    pos = move(['Down'])

mgba.take_screenshot()
