import mgba
import time

print("--- SELF-CORRECTING ROAD TO GATEHOUSE FROM (18, 9) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (18, 9) facing UP.
# 1. Walk Right along Row 9 to Column 37.
print("Step 1: Walking Right to Column 37")
for _ in range(25):
    pos = get_pos()
    if pos and pos['x'] == 37:
        print("Arrived at Column 37!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 37!")

# 2. Walk UP Column 37 to Row 2.
print("Step 2: Walking UP Column 37 to Row 2")
for _ in range(15):
    pos = get_pos()
    if pos and pos['y'] == 2:
        print("Arrived at Row 2!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 2!")

# 3. Walk Left along Row 2 to Column 22.
print("Step 3: Walking Left along Row 2 to Column 22")
for _ in range(20):
    pos = get_pos()
    if pos and pos['x'] == 22:
        print("Arrived at Column 22!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 22!")

# 4. Walk Down to Row 4.
print("Step 4: Walking Down to Row 4")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 4:
        print("Arrived at Row 4!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 4!")

# 5. Walk Left to Column 18.
print("Step 5: Walking Left to Column 18")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 18:
        print("Arrived at Column 18!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 18!")

# 6. Enter the Gatehouse at (18, 3)
print("Step 6: Entering Gatehouse")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["Up"])
time.sleep(1.5)

pos_inside = get_pos()
print("Position inside Gatehouse:", pos_inside)

# 7. Speak to the clerk and enter the Safari Zone
if pos_inside and pos_inside['x'] < 10:
    print("Inside Gatehouse. Walking to clerk...")
    mgba.press_buttons(["Up", "sleep 100", "Up"])
    time.sleep(1.0)
    
    # Talk to clerk
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue
    print("Paying and entering Safari Zone...")
    for _ in range(12):
        mgba.press_buttons(["A"])
        time.sleep(0.6)
        
    time.sleep(2.0) # wait for warp

mgba.take_screenshot()
print("Final Position inside Safari:", get_pos())
