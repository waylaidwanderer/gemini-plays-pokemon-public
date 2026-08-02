import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F doors exploration from:", pos)

if pos['x'] == 24 and pos['y'] == 14:
    # 1. Walk Left 3 to (21, 14)
    print("Walking Left to Column 21...")
    for _ in range(3):
        pos = move(["Left"])
        
    # 2. Walk Up 1 to (21, 13)
    pos = move(["Up"])
    
    # 3. Walk Left 5 to (16, 13)
    print("Walking Left to Column 16...")
    for _ in range(5):
        pos = move(["Left"])
        
    # 4. Walk Down 1 to (16, 14)
    pos = move(["Down"])
    
    # 5. Walk Left 1 to (15, 14)
    pos = move(["Left"])
    
    # 6. Walk Down 2 to (15, 16) (DOWN spinner) to slide to (15, 18)
    print("Stepping onto (15, 16) DOWN spinner...")
    pos = move(["Down"])
    pos = move(["Down"])
    time.sleep(3.0)
    pos = mgba.get_coordinates()
    print("Position at (15, 18):", pos)

# We should be at (15, 18).
# Let's test walking Down to (15, 19) and Right to (16, 18)
if pos['x'] == 15 and pos['y'] == 18:
    print("Testing walking Down from (15, 18)...")
    new_pos = move(["Down"])
    if new_pos['y'] == 19:
        print("-> Down to (15, 19) is WALKABLE!")
        # Walk back Up
        move(["Up"])
    else:
        print("-> Down to (15, 19) is BLOCKED.")
        
    print("Testing walking Right from (15, 18)...")
    new_pos = move(["Right"])
    if new_pos['x'] == 16:
        print("-> Right to (16, 18) is WALKABLE! (Wait for potential spin/slide)")
        time.sleep(3.0)
        print("Position after Right:", mgba.get_coordinates())
    else:
        print("-> Right to (16, 18) is BLOCKED.")

mgba.take_screenshot()
