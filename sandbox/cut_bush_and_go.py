import mgba
import time

print("--- FINISHING CUT FROM PARTY MENU ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (26, 14).
# We are in the party menu, cursor is pointing at NIDORAN (index 5).
# 1. Highlight TRUFFLE (index 1) by pressing Up 4 times.
print("Step 1: Highlighting TRUFFLE")
for _ in range(4):
    mgba.press_buttons(["Up"])
    time.sleep(0.2)

# Select TRUFFLE
mgba.press_buttons(["A"])
time.sleep(1.0)

# 2. Highlight CUT (Option 2 in submenu) by pressing Down once, and select A.
print("Step 2: Selecting CUT")
mgba.press_buttons(["Down"])
time.sleep(0.2)
mgba.press_buttons(["A"])
time.sleep(2.5) # wait for CUT animation

# Press A once to clear any residual CUT text box
mgba.press_buttons(["A"])
time.sleep(0.6)

print("Step 3: Walking through cut bush to Column 26 Row 4...")
# 3. Walk UP Column 26 to Row 4.
for _ in range(15):
    pos = get_pos()
    if pos and pos['y'] == 4:
        print("Arrived at Row 4!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

# 4. Walk Left to Column 18.
print("Step 4: Walking Left to Column 18")
for _ in range(15):
    pos = get_pos()
    if pos and pos['x'] == 18:
        print("Arrived at Column 18!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)

# 5. Enter the Gatehouse at (18, 3).
print("Step 5: Entering Gatehouse")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["Up"])
time.sleep(1.5)

pos_inside = get_pos()
print("Position inside Gatehouse:", pos_inside)

# 6. Speak to the clerk and enter the Safari Zone
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
