import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F spinner navigation from:", pos)

if pos['x'] == 27 and pos['y'] == 8:
    # 1. Walk Down 5 steps to Row 13
    print("Walking Down to Row 13...")
    for _ in range(5):
        pos = move(["Down"])
        
    # 2. Walk Left to the spinner entrance at (12, 13)
    # We are at (27, 13). Walk Left 15 steps.
    print("Walking Left to (12, 13)...")
    for _ in range(15):
        pos = move(["Left"])
        
    # Wait for the spinner slide to complete
    print("Waiting for spinner slide to finish...")
    time.sleep(5.0)
    
    pos = mgba.get_coordinates()
    print("Position after spinner slide 1:", pos)

mgba.take_screenshot()
