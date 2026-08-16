import mgba
import time

print("--- USING CUT ON BUSH AT (26, 13) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 14) facing LEFT.
# 1. Walk to (26, 14): Right 7 times (1 turn + 6 steps).
print("Step 1: Walking to (26, 14)")
mgba.press_buttons(["Right"])
time.sleep(0.4)
for _ in range(6):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
print("Position after Step 1:", get_pos())

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

print("Step 3: Walking through cut bush to Gatehouse...")
# 4. Walk UP Column 26 to Row 4: we need to walk UP 10 steps (14 - 4 = 10).
# Since we are already facing UP, press Up 10 times.
for _ in range(10):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
print("Position after walking UP:", get_pos())

# 5. Walk Left to Column 18: Left 9 times (1 turn + 8 steps).
mgba.press_buttons(["Left"])
time.sleep(0.4)
for _ in range(8):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Position after walking Left:", get_pos())

# 6. Enter the Gatehouse at (18, 3)
# Since we are facing Left at (18, 4), press Up 2 times (1 turn + 1 step).
mgba.press_buttons(["Up", "sleep 200", "Up"])
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
