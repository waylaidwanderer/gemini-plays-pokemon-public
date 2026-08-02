import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Current pos: {pos}")

if pos['x'] == 10 and pos['y'] == 12:
    # Face Right
    print("Turning Right...")
    mgba.press_buttons(['Right'])
    time.sleep(0.3)
    
    # Use Cut on the bush at (11, 12)
    print("Using CUT on bush at (11, 12)...")
    mgba.press_buttons(['Start'])
    time.sleep(0.5)
    mgba.press_buttons(['Down'])  # Cursor to POKEMON
    time.sleep(0.3)
    mgba.press_buttons(['A'])     # Enter POKEMON menu
    time.sleep(0.5)
    mgba.press_buttons(['A'])     # Select SHELLBY
    time.sleep(0.5)
    mgba.press_buttons(['A'])     # Select CUT
    time.sleep(1.0)
    
    # Dismiss menu
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    
    # Try to walk Right
    print("Trying to walk Right onto (11, 12)...")
    pos = move(['Right'])
    
    # If successful, walk Right to (12, 12)
    if pos['x'] == 11 and pos['y'] == 12:
        pos = move(['Right'])
        
mgba.take_screenshot()
