import mgba
import time

print("--- NAVIGATING TO GATEHOUSE FROM (20, 16) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 16).
# 1. Walk Right to (22, 16).
print("Step 1: Walking to (22, 16)")
for _ in range(2):
    pos = get_pos()
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)

# 2. Walk UP to (22, 14).
print("Step 2: Walking UP to (22, 14)")
for _ in range(2):
    pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)

# 3. Walk Right along Row 14 to Column 37.
print("Step 3: Walking Right along Row 14 to Column 37")
for _ in range(15):
    pos = get_pos()
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Right"])
        time.sleep(0.4)

# 4. Walk UP Column 37 to Row 2.
print("Step 4: Walking UP Column 37 to Row 2")
for _ in range(12):
    pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Up"])
        time.sleep(0.4)

# 5. Walk Left along Row 2 to Column 22.
print("Step 5: Walking Left along Row 2 to Column 22")
for _ in range(15):
    pos = get_pos()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

# 6. Walk Down to Row 4.
print("Step 6: Walking Down to Row 4")
for _ in range(2):
    pos = get_pos()
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Down"])
        time.sleep(0.4)

# 7. Walk Left to Column 18.
print("Step 7: Walking Left to Column 18")
for _ in range(4):
    pos = get_pos()
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    if get_pos() == pos:
        mgba.press_buttons(["Left"])
        time.sleep(0.4)

# 8. Enter the Gatehouse at (18, 3)
print("Step 8: Entering Gatehouse")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["Up"])
time.sleep(1.0) # wait for map transition

pos_after_gate = get_pos()
print("Position inside Gatehouse:", pos_after_gate)

# 9. Walk to the clerk inside the Gatehouse
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
