import mgba
import time

print("--- SELF-CORRECTING CUT BUSH ROUTE ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 14) facing LEFT.
# 1. Walk to Column 26 on Row 14.
print("Step 1: Walking to Column 26")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 26:
        print("Arrived at Column 26!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 26!")

# 2. Face UP
mgba.press_buttons(["Up"])
time.sleep(0.4)

# 3. Use CUT
print("Step 2: Accessing POKEMON menu to use CUT...")
mgba.press_buttons(["Start"])
time.sleep(0.6)

# Force cursor to POKEDEX (top)
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)

# Press Down once to POKEMON, and A
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(1.0)

# Press Down once to highlight TRUFFLE (2nd slot), and A
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(1.0)

# Press Down once to highlight CUT (Option 2), and A
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(2.5) # wait for CUT animation and text

# Press A once to clear any residual CUT text box
mgba.press_buttons(["A"])
time.sleep(0.6)

print("Step 3: Walking through cut bush to Column 26 Row 4...")
# 4. Walk UP Column 26 to Row 4.
for _ in range(15):
    pos = get_pos()
    if pos and pos['y'] == 4:
        print("Arrived at Row 4!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

# 5. Walk Left to Column 18.
print("Step 4: Walking Left to Column 18")
for _ in range(15):
    pos = get_pos()
    if pos and pos['x'] == 18:
        print("Arrived at Column 18!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)

# 6. Enter the Gatehouse at (18, 3)
print("Step 5: Entering Gatehouse")
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
