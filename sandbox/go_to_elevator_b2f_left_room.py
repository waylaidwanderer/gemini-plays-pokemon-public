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

if pos['x'] == 15 and pos['y'] == 18:
    # 1. Slide to B2F Left Room at (2, 9)
    pos = move(['Left'])   # (14, 18)
    print("Stepping onto (13, 18) LEFT spinner...")
    pos = move(['Left'])   # Step onto (13, 18)
    print("Waiting for slide...")
    time.sleep(5.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")

if pos['x'] == 2 and pos['y'] == 9:
    # 2. Walk to (2, 7)
    pos = move(['Left'])   # (1, 9)
    pos = move(['Up'])     # (1, 8)
    pos = move(['Up'])     # (1, 7)
    pos = move(['Right'])  # (2, 7)
    
    # 3. Walk to (7, 7) using the safe path
    pos = move(['Right'])  # (3, 7)
    pos = move(['Right'])  # (4, 7)
    pos = move(['Right'])  # (5, 7)
    pos = move(['Down'])   # (5, 8)
    pos = move(['Down'])   # (5, 9)
    pos = move(['Right'])  # (6, 9)
    pos = move(['Right'])  # (7, 9)
    pos = move(['Up'])     # (7, 8)
    pos = move(['Up'])     # (7, 7)
    
    # 4. Try walking Right from (7, 7) to Column 21!
    print("Testing if we can walk Right on Row 7...")
    for _ in range(15):
        next_pos = move(['Right'])
        if next_pos['x'] == pos['x']:
            print("Blocked going Right on Row 7!")
            break
        pos = next_pos
        if pos['x'] == 21:
            print("WE REACHED COLUMN 21!")
            break

mgba.take_screenshot()
