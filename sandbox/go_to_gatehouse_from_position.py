import mgba
import time

print("--- NAVIGATING TO SAFARI ZONE ---")

def get_pos():
    return mgba.get_coordinates()

# 1. Walk from (5, 28) to (13, 28)
# We need to walk Right 8 steps.
print("Step 1: Walking to (13, 28)")
for _ in range(8):
    pos = get_pos()
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)

# 2. Walk UP Column 13 to Row 14
# We need to walk Up 14 steps.
print("Step 2: Walking UP Column 13 to Row 14")
for _ in range(14):
    pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)

# 3. Walk Right along Row 14 to Column 37
# We need to walk Right 24 steps (37 - 13 = 24).
print("Step 3: Walking Right along Row 14 to Column 37")
for _ in range(24):
    pos = get_pos()
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)

# 4. Walk Up Column 37 to Row 2
# We need to walk Up 12 steps (14 - 2 = 12).
print("Step 4: Walking UP Column 37 to Row 2")
for _ in range(12):
    pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)

# 5. Walk Left along Row 2 to Column 22
# We need to walk Left 15 steps (37 - 22 = 15).
print("Step 5: Walking Left along Row 2 to Column 22")
for _ in range(15):
    pos = get_pos()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

# 6. Walk Down to Row 4
# We need to walk Down 2 steps.
print("Step 6: Walking Down to Row 4")
for _ in range(2):
    pos = get_pos()
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)

# 7. Walk Left to Column 18
# We need to walk Left 4 steps.
print("Step 7: Walking Left to Column 18")
for _ in range(4):
    pos = get_pos()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

# 8. Enter the Gatehouse at (18, 3)
# We are facing Left at (18, 4), so we need to face Up and step Up into the door at (18, 3).
print("Step 8: Entering Gatehouse")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["Up"])
time.sleep(1.0) # wait for map transition

pos_after_gate = get_pos()
print("Position inside Gatehouse:", pos_after_gate)

# 9. Walk to the clerk inside the Gatehouse
# Inside the Gatehouse, we transition to (3, 5).
# The clerk is at (3, 2).
# Let's walk to (3, 3) facing UP.
if pos_after_gate and pos_after_gate['x'] < 10:
    print("Inside Gatehouse. Walking to clerk...")
    # Walk Up 2 steps to (3, 3)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Talk to clerk
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue (press A 12 times)
    print("Paying and entering Safari Zone...")
    for _ in range(12):
        mgba.press_buttons(["A"])
        time.sleep(0.6)
        
    time.sleep(2.0) # wait for warp into Safari Zone Center at (15, 25)

mgba.take_screenshot()
print("Final Position:", get_pos())
