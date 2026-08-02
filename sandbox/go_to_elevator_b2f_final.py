import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting go_to_elevator_b2f_final from {pos}")

if pos['x'] == 11 and pos['y'] == 20:
    # 1. Walk Left 9 steps to (2, 20)
    print("Walking Left to Column 2...")
    for _ in range(9):
        pos = move(['Left'])
        
    # 2. Walk Up 11 steps to (2, 9)
    print("Walking Up to Row 9...")
    for _ in range(11):
        pos = move(['Up'])

if pos['x'] == 2 and pos['y'] == 9:
    # 3. Walk to (2, 7)
    pos = move(['Left'])   # (1, 9)
    pos = move(['Up'])     # (1, 8)
    pos = move(['Up'])     # (1, 7)
    pos = move(['Right'])  # (2, 7)
    
    # 4. Walk to (7, 7) using the safe path
    pos = move(['Right'])  # (3, 7)
    pos = move(['Right'])  # (4, 7)
    pos = move(['Right'])  # (5, 7)
    pos = move(['Down'])   # (5, 8)
    pos = move(['Down'])   # (5, 9)
    pos = move(['Right'])  # (6, 9)
    pos = move(['Right'])  # (7, 9)
    pos = move(['Up'])     # (7, 8)
    pos = move(['Up'])     # (7, 7)
    
    # 5. Try walking Right from (7, 7) to Column 21 on Row 7!
    print("Testing if we can walk Right on Row 7...")
    for _ in range(14):
        next_pos = move(['Right'])
        if next_pos['x'] == pos['x']:
            print("Blocked going Right on Row 7!")
            break
        pos = next_pos
        
    # 6. Walk Up to (21, 3) (if we reached Column 21)
    if pos['x'] == 21:
        print("We reached Column 21! Walking Up to Row 3...")
        for _ in range(4):
            pos = move(['Up'])
            
        # Stand at (21, 3) and face UP
        print("Turning UP...")
        mgba.press_buttons(['Up'])
        time.sleep(0.3)
        
        # Press A to use Lift Key
        print("Pressing A to use Lift Key...")
        mgba.press_buttons(['A'])
        time.sleep(1.0)
        mgba.take_screenshot()
        
        # Walk UP into elevator
        print("Walking UP into elevator...")
        pos = move(['Up'])
        time.sleep(2.0)
        print(f"New position: {mgba.get_coordinates()}")

mgba.take_screenshot()
