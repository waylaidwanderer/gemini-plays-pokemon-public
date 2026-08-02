import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting run to B4F from B1F:", pos)

if pos['x'] == 24 and pos['y'] == 15:
    # 1. Walk to (25, 15)
    pos = move(["Right"])
    
if pos['x'] == 25 and pos['y'] == 15:
    # Walk to B1F stairs at (23, 2)
    # Walk Up to Row 11 (4 steps)
    for _ in range(4):
        pos = move(["Up"])
    # Walk Left to Column 23 (2 steps)
    for _ in range(2):
        pos = move(["Left"])
    # Walk Up to Row 3 (8 steps)
    for _ in range(8):
        pos = move(["Up"])
    # Take stairs to B2F
    print("Taking stairs to B2F...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Spawning on B2F:", pos)

# We should be on B2F at (27, 8) (or (27, 9))
if pos['x'] == 27 and (pos['y'] == 8 or pos['y'] == 9):
    # 2. Walk to B3F stairs at (21, 8) on B2F
    # Walk Down to Row 14 (5 steps from Row 9)
    dist_y = 14 - pos['y']
    for _ in range(dist_y):
        pos = move(["Down"])
    # Walk Left to Column 21 (6 steps)
    for _ in range(6):
        pos = move(["Left"])
    # Walk Up to Row 8 (6 steps)
    for _ in range(6):
        pos = move(["Up"])
    # Take stairs to B3F
    print("Taking stairs to B3F...")
    pos = move(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Spawning on B3F:", pos)

# We should be on B3F at (25, 6) (or (21, 9) or (25, 7)?)
# Wait, let's verify spawn coordinate on B3F:
# When we took the B2F (21, 8) stairs in our previous run, we spawned at B3F (25, 6) (or (25, 7) or (21, 9)? The print said (21, 9) but then we were at (25, 6) after).
# Let's handle any B3F coordinates around (21-25, 6-9)
pos = mgba.get_coordinates()
if pos['x'] in [21, 22, 23, 24, 25] and pos['y'] in [6, 7, 8, 9]:
    print("Successfully on B3F!")
    # We want to go to B4F stairs at (19, 12) on B3F
    # Let's walk to (19, 12) on B3F
    # First, reposition to Row 7
    if pos['y'] < 7:
        for _ in range(7 - pos['y']):
            pos = move(["Down"])
    elif pos['y'] > 7:
        for _ in range(pos['y'] - 7):
            pos = move(["Up"])
            
    # Now we are on Row 7. Walk to Column 19
    pos = mgba.get_coordinates()
    if pos['x'] > 19:
        for _ in range(pos['x'] - 19):
            pos = move(["Left"])
    elif pos['x'] < 19:
        for _ in range(19 - pos['x']):
            pos = move(["Right"])
            
    # Now we are at (19, 7). Walk Down to Row 12 (5 steps)
    print("Walking Down to B4F stairs on B3F...")
    for _ in range(5):
        pos = move(["Down"])
        
    # Take stairs to B4F at (19, 12)
    print("Taking stairs to B4F...")
    pos = move(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Spawning on B4F:", pos)

mgba.take_screenshot()
