import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting step-by-step cut from {pos}")

if pos['x'] == 2 and pos['y'] == 7:
    # Face Down
    mgba.press_buttons(['Down'])
    time.sleep(0.5)
    
    # Open START menu
    mgba.press_buttons(['Start'])
    time.sleep(1.0)
    
    # Reset cursor
    for _ in range(7):
        mgba.press_buttons(['Up'])
        time.sleep(0.2)
        
    # Select POKÉMON
    mgba.press_buttons(['Down'])
    time.sleep(0.3)
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    
    # Select TRUFFLE (Down once, then A)
    mgba.press_buttons(['Down'])
    time.sleep(0.3)
    mgba.press_buttons(['A'])
    time.sleep(1.0)
    
    # Select CUT (Down once, then A)
    mgba.press_buttons(['Down'])
    time.sleep(0.3)
    mgba.press_buttons(['A'])
    
    # Wait for the overworld to load, the animation to play, and text to appear
    print("Waiting for CUT execution...")
    time.sleep(4.0)
    
    # Take screenshot of the text box
    mgba.take_screenshot()
    
    # Press B to dismiss any dialog
    print("Dismissing text...")
    mgba.press_buttons(['B'])
    time.sleep(1.0)
    
    # Try to walk Down
    print("Trying to walk Down...")
    pos = move(['Down'])

mgba.take_screenshot()
