import mgba
import time

print("--- NAVIGATING TO GATEHOUSE FROM (20, 14) ---")

def get_pos():
    return mgba.get_coordinates()

# We start at (20, 14) facing LEFT.
# 1. Walk to (22, 14): we need to face Right and take 2 steps.
# Press Right 3 times.
print("Step 1: Walking to (22, 14)")
mgba.press_buttons(["Right", "sleep 100", "Right", "sleep 100", "Right"])
time.sleep(1.0)
print("Position after Step 1:", get_pos())

# 2. Walk to (37, 14): we need to walk Right 15 steps.
# Since we are already facing Right, we press Right 15 times.
print("Step 2: Walking to (37, 14)")
for _ in range(15):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
print("Position after Step 2:", get_pos())

# 3. Walk UP Column 37 to Row 2: we need to walk UP 12 steps.
# Press Up 13 times (1 turn + 12 steps).
print("Step 3: Walking UP to Row 2")
mgba.press_buttons(["Up"])
time.sleep(0.4)
for _ in range(12):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
print("Position after Step 3:", get_pos())

# 4. Walk Left along Row 2 to Column 22: we need to walk Left 15 steps.
# Press Left 16 times (1 turn + 15 steps).
print("Step 4: Walking Left to Column 22")
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(15):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after Step 4:", get_pos())

# 5. Walk Down to Row 4: we need to walk Down 2 steps.
# Press Down 3 times (1 turn + 2 steps).
print("Step 5: Walking Down to Row 4")
mgba.press_buttons(["Down"])
time.sleep(0.4)
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
print("Position after Step 5:", get_pos())

# 6. Walk Left to Column 18: we need to walk Left 4 steps.
# Press Left 5 times (1 turn + 4 steps).
print("Step 6: Walking Left to Column 18")
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after Step 6:", get_pos())

# 7. Enter the Gatehouse at (18, 3)
# Press Up 2 times (1 turn + 1 step).
print("Step 7: Entering Gatehouse")
mgba.press_buttons(["Up", "sleep 200", "Up"])
time.sleep(1.5) # wait for map transition

pos_inside = get_pos()
print("Position inside Gatehouse:", pos_inside)

# 8. Speak to the clerk and enter the Safari Zone
if pos_inside and pos_inside['x'] < 10:
    print("Inside Gatehouse. Walking to clerk...")
    # Walk Up 2 steps to (3, 3)
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
print("Final Position:", get_pos())
