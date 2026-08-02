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

if pos['x'] == 14 and pos['y'] == 15:
    # 1. Slide to (16, 13) stopper
    pos = move(['Right'])  # (15, 15)
    pos = move(['Right'])  # (16, 15)
    print("Stepping onto (16, 16) UP spinner...")
    pos = move(['Down'])   # Step Down onto (16, 16)
    print("Waiting for slide...")
    time.sleep(4.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")
    
if pos['x'] == 16 and pos['y'] == 13:
    # 2. Walk to (17, 11) LEFT spinner
    pos = move(['Right'])  # (17, 13)
    pos = move(['Right'])  # (18, 13)
    pos = move(['Right'])  # (19, 13)
    pos = move(['Up'])     # (19, 12)
    pos = move(['Up'])     # (19, 11)
    pos = move(['Left'])   # (18, 11)
    print("Stepping onto (17, 11) LEFT spinner...")
    pos = move(['Left'])   # Step onto (17, 11)
    print("Waiting for slide...")
    time.sleep(5.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")

# Now we should be at (2, 9) on B2F.
# Let's systematically test Column 1, 2, 3, 4 for any staircase warps!
if pos['x'] == 2 and pos['y'] == 9:
    # Walk Left to (1, 9)
    pos = move(['Left'])
    
    # Try walking around the bottom-left area of the room
    print("Testing bottom-left coordinates for warps...")
    for y in [10, 11, 12, 13]:
        for x in [1, 2, 3]:
            # Walk to (x, y)
            print(f"Trying to walk to ({x}, {y})...")
            pos = mgba.get_coordinates()
            # Move towards x
            if x > pos['x']:
                pos = move(['Right'])
            elif x < pos['x']:
                pos = move(['Left'])
            # Move towards y
            if y > pos['y']:
                pos = move(['Down'])
            elif y < pos['y']:
                pos = move(['Up'])
                
            # If coordinates changed, check if we warped
            new_pos = mgba.get_coordinates()
            if new_pos['x'] != pos['x'] or new_pos['y'] != pos['y']:
                print(f"WARPED or moved unexpectedly! Current position: {new_pos}")
                break

mgba.take_screenshot()
