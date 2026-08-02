import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting go_to_left_room from {pos}")

if pos['x'] == 24 and pos['y'] == 7:
    # Walk to (23, 13)
    pos = move(['Right'])  # (25, 7)
    for _ in range(6):
        pos = move(['Down'])  # (25, 13)
    pos = move(['Left'])   # (24, 13)
    pos = move(['Left'])   # (23, 13)
    
    # Face Down
    print("Facing Down...")
    mgba.press_buttons(['Down'])
    time.sleep(0.3)
    
    # Use Cut on the bush at (23, 14)
    print("Opening menu to use CUT...")
    mgba.press_buttons(['Start'])
    time.sleep(0.5)
    mgba.press_buttons(['Down'])  # Cursor to POKEMON (usually 2nd option)
    time.sleep(0.3)
    mgba.press_buttons(['A'])     # Enter POKEMON menu
    time.sleep(0.5)
    mgba.press_buttons(['A'])     # Select first Pokémon (SHELLBY)
    time.sleep(0.5)
    mgba.press_buttons(['A'])     # Select CUT (usually first option or we need to find it)
    time.sleep(1.0)
    # Press B to dismiss any dialog
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    mgba.press_buttons(['B'])
    time.sleep(0.5)
    
    # Let's check if the bush is gone by trying to move Down
    print("Trying to walk Down through cut bush...")
    pos = move(['Down'])
    
    # If we are at (23, 14), we successfully cut the bush!
    if pos['y'] == 14:
        # Walk Left to (12, 14)
        for _ in range(11):
            pos = move(['Left'])
            
        # Walk Up onto the spinner at (12, 13)
        print("Stepping UP onto the spinner...")
        pos = move(['Up'])
        print("Waiting for slide...")
        time.sleep(5.0)
        print(f"Final position after slide: {mgba.get_coordinates()}")

mgba.take_screenshot()
