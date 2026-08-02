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

if pos['x'] == 25 and pos['y'] == 15:
    # Walk Up to (25, 14)
    pos = move(['Up'])
    
    # Walk Left to (12, 14)
    print("Walking Left on Row 14...")
    for _ in range(13):
        next_pos = move(['Left'])
        if next_pos['x'] == pos['x']:
            print("Blocked Left on Row 14!")
            break
        pos = next_pos
        
    # If we reached (12, 14), walk Up onto the spinner at (12, 13)
    if pos['x'] == 12 and pos['y'] == 14:
        print("Stepping UP onto the spinner at (12, 13)...")
        pos = move(['Up'])
        print("Waiting for slide...")
        time.sleep(5.0)
        print(f"New position: {mgba.get_coordinates()}")

mgba.take_screenshot()
