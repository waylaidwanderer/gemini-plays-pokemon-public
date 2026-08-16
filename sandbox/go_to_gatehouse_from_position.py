import mgba
import time

print("--- NAVIGATING TO GATEHOUSE FROM (18, 8) VIA COLUMN 37 ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (18, 8) facing UP.
# 1. Walk Down to (18, 9): 2 steps (1 turn + 1 step).
print("Step 1: Walking Down to (18, 9)")
mgba.press_buttons(["Down", "sleep 100", "Down"])
time.sleep(1.0)
print("Position after Step 1:", get_pos())

# 2. Walk Right to (37, 9): 19 steps.
# Since we are facing DOWN, we need 1 turn + 19 steps = 20 buttons.
print("Step 2: Walking Right to (37, 9)")
mgba.press_buttons(["Right"])
time.sleep(0.4)
for _ in range(19):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
print("Position after Step 2:", get_pos())

# 3. Walk UP Column 37 to Row 2: 7 steps.
# Since we are facing RIGHT, we need 1 turn + 7 steps = 8 buttons.
print("Step 3: Walking UP Column 37 to Row 2")
mgba.press_buttons(["Up"])
time.sleep(0.4)
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
print("Position after Step 3:", get_pos())

# 4. Walk Left along Row 2 to Column 22: 15 steps.
# Since we are facing UP, we need 1 turn + 15 steps = 16 buttons.
print("Step 4: Walking Left to Column 22")
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(15):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after Step 4:", get_pos())

# 5. Walk Down to Row 4: 2 steps.
# Since we are facing LEFT, we need 1 turn + 2 steps = 3 buttons.
print("Step 5: Walking Down to Row 4")
mgba.press_buttons(["Down"])
time.sleep(0.4)
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
print("Position after Step 5:", get_pos())

# 6. Walk Left to Column 18: 4 steps.
# Since we are facing DOWN, we need 1 turn + 4 steps = 5 buttons.
print("Step 6: Walking Left to Column 18")
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after Step 6:", get_pos())

# 7. Enter the Gatehouse at (18, 3)
# Since we are facing LEFT, we need 1 turn + 1 step = 2 buttons.
print("Step 7: Entering Gatehouse")
mgba.press_buttons(["Up", "sleep 100", "Up"])
time.sleep(1.5)

pos_inside = get_pos()
print("Position inside Gatehouse:", pos_inside)

# 8. Speak to the clerk and enter the Safari Zone
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
