import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    return pos

pos = mgba.get_coordinates()
print("Starting bottom-area exploration from:", pos)

if pos['x'] == 15 and pos['y'] == 18:
    # 1. Slide to (11, 20) stopper
    print("Walking Left to (13, 18) LEFT spinner...")
    pos = move(["Left"])
    pos = move(["Left"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position at stopper:", pos)

# We should be around Row 20 Column 11.
# Let's test Row 20, 21, 22, 23, 24
for y in range(20, 25):
    # Move to Column 11 on Row y
    pos = mgba.get_coordinates()
    if pos['y'] < y:
        print(f"Moving Down to Row {y}...")
        for _ in range(y - pos['y']):
            pos = move(["Down"])
    elif pos['y'] > y:
        print(f"Moving Up to Row {y}...")
        for _ in range(pos['y'] - y):
            pos = move(["Up"])
            
    # Walk to Column 11
    pos = mgba.get_coordinates()
    if pos['x'] > 11:
        for _ in range(pos['x'] - 11):
            pos = move(["Left"])
            
    # Try walking Right as far as possible
    pos = mgba.get_coordinates()
    print(f"Testing Row {pos['y']} going Right from Column {pos['x']}...")
    
    path = [pos]
    for i in range(15):
        old_pos = pos
        pos = move(["Right"])
        if pos == old_pos:
            break
        path.append(pos)
        
    print(f"Row {y} Path: {path}")

mgba.take_screenshot()
