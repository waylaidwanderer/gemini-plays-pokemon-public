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

if pos['x'] == 2 and pos['y'] == 9:
    # 1. Walk to (10, 12)
    pos = move(['Right'])  # (3, 9)
    pos = move(['Down'])   # (3, 10)
    pos = move(['Down'])   # (3, 11)
    
    print("Stepping onto (4, 11) RIGHT-pointing spinner...")
    pos = move(['Right'])
    print("Waiting for slide...")
    time.sleep(5.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")
    
    # Walk to (10, 12)
    pos = move(['Right'])  # (9, 11)
    pos = move(['Right'])  # (10, 11)
    pos = move(['Down'])   # (10, 12)
    
    # 2. Walk to (10, 14)
    pos = move(['Down'])   # (10, 13)
    pos = move(['Down'])   # (10, 14)
    
    # 3. Step onto (11, 14) DOWN-pointing spinner
    print("Stepping onto (11, 14) DOWN-pointing spinner...")
    pos = move(['Right'])  # Step Right onto (11, 14)
    print("Waiting for slide...")
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")
    
    # 4. Step onto (11, 16) RIGHT-pointing spinner (if we are at (11, 15) or similar)
    if pos['x'] == 11 and pos['y'] == 15:
        print("Stepping onto (11, 16) RIGHT-pointing spinner...")
        pos = move(['Down'])  # Step Down onto (11, 16)
        print("Waiting for slide...")
        time.sleep(5.0)
        pos = mgba.get_coordinates()
        print(f"Position after slide: {pos}")
        
    # Let's print adjacent walkable tiles and see where we are
    print("Final position:", mgba.get_coordinates())

mgba.take_screenshot()
