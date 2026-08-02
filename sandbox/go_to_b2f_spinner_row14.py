import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting Row 14 navigation from:", pos)

if pos['x'] == 25 and pos['y'] == 13:
    # Walk Down to Row 14
    pos = move(["Down"])
    
    # Walk Left to Column 12 (13 steps)
    print("Walking Left on Row 14...")
    for _ in range(13):
        pos = move(["Left"])
        
    # Wait for any potential spinner slide
    print("Waiting 3 seconds...")
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position after Row 14 walk:", pos)
    
    # If we are at (12, 14) and not on a spinner, walk Up 1 step to (12, 13)
    if pos['x'] == 12 and pos['y'] == 14:
        print("At (12, 14). Walking Up onto the UP spinner...")
        pos = move(["Up"])
        time.sleep(5.0)
        print("Position after slide:", mgba.get_coordinates())

mgba.take_screenshot()
