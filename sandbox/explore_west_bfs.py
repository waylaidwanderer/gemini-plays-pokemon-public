import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def find_open_west_path():
    print("Starting BFS to find open western path to Celadon City...")
    # We are at (2, 8)
    # Let's explore Row 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 7, 6, 5, 4, 3, 2, 1, 0!
    # On each row, we walk to Column 2 and try to walk LEFT.
    # If we successfully step onto Column 1 or Column 0, we found the path!
    
    # Let's first move to Column 2 (we are already there)
    # Let's try LEFT at current Row 8:
    print("Testing Row 8...")
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 8, Col {pos['x']}!")
        return

    # Let's try Row 9:
    print("Testing Row 9...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 9, Col {pos['x']}!")
        return
        
    # Let's try Row 10:
    print("Testing Row 10...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 10, Col {pos['x']}!")
        return

    # Let's try other rows! We can go up to Row 2
    # To reach Row 2, we must go around the ledge via Column 8
    print("Going around ledge via Column 8 to test upper rows...")
    press_and_wait("Right", 0.25)
    press_and_wait("Right", 0.25)
    press_and_wait("Right", 0.25)
    press_and_wait("Right", 0.25)
    press_and_wait("Right", 0.25)
    press_and_wait("Right", 0.25) # now at column 8 row 10
    
    # Walk UP Column 8 to Row 2
    for _ in range(8):
        press_and_wait("Up", 0.25) # now at (8, 2)
        
    # Test Row 2 Column 2: walk left to Column 2
    for _ in range(6):
        press_and_wait("Left", 0.25) # now at (2, 2)
        
    print("Testing Row 2...")
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 2, Col {pos['x']}!")
        return
        
    # Test Row 3:
    print("Testing Row 3...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 3, Col {pos['x']}!")
        return

    # Test Row 4:
    print("Testing Row 4...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 4, Col {pos['x']}!")
        return

    # Test Row 5:
    print("Testing Row 5...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 5, Col {pos['x']}!")
        return

    # Test Row 6:
    print("Testing Row 6...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 6, Col {pos['x']}!")
        return

    # Test Row 7:
    print("Testing Row 7...")
    press_and_wait("Down", 0.3)
    press_and_wait("Left", 0.3)
    pos = mgba.get_coordinates()
    if pos['x'] < 2:
        print(f"FOUND OPEN PATH AT Row 7, Col {pos['x']}!")
        return

    print("All tests completed. None found open. Taking screenshot.")
    mgba.take_screenshot()

find_open_west_path()
