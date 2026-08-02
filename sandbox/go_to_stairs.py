import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting go_to_stairs from:", pos)

if pos['x'] == 22 and pos['y'] == 13:
    # 1. Walk Left to (21, 13)
    pos = move(["Left"])
    
    # 2. Walk Up along Column 21 to Row 8
    print("Walking Up Column 21 to Row 8...")
    for _ in range(5):
        pos = move(["Up"])
        
    # Wait to see if map transition occurs
    print("Checking if we transitioned to B3F...")
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position:", pos)
    
mgba.take_screenshot()
